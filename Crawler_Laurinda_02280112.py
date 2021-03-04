# Crawling restaurant data given links

import re
import util
import bs4
import queue
import json
import sys
import csv
import pandas as pd


def get_info(links):
    '''
    Extract restaurants info
    '''
    info = []

    for url in links:
        print("start at", url)
        restaurant = {}
        request = util.get_request(url)
        text = util.read_request(request)
        soup = bs4.BeautifulSoup(text, "html5lib")
        tag = soup.find('script', type='application/ld+json')
        if tag is not None:
            d = json.loads(tag.text)
    
            restaurant['name'] = d['name']                      # Name
            restaurant['zip_code'] = d['address']['postalCode'] # Zipcode

            if 'priceRange' in d:
                restaurant['price_range'] = d['priceRange']     # eg.'$11-30'
            else:
                restaurant['price_range'] = None

            restaurant['cuisine'] = d['servesCuisine']          # eg.'Italian'

            restaurant['num_review'] = len(d["review"])         # Num of reviews
            
            reviews  = d["review"]                              # Avg Rating
            rating = 0
            for review in reviews:
                rating += review['reviewRating']['ratingValue']
            restaurant['rating'] = rating/len(d["review"]

            info.append(restaurant)
        
        else:
            print("empty tag")

    return info

def load_to_df(info):
    '''
    Load restaurants info (list of dicts) to pandas dataframe
    '''
    return pd.DataFrame.from_dict(info, orient='columns')

def to_csv(df):
    '''
    Load pandas dataframe to csv
    '''
    return df.to_csv('info.csv', index=False)