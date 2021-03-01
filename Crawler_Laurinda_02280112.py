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

    for link in links:
        restaurant = {}
        request = util.get_request(url)
        text = util.read_request(request)
        soup = bs4.BeautifulSoup(text, "html5lib")
        tag = soup.find('script', type='application/ld+json')
        d = json.loads(tag.text)

        restaurant['name'] = d['name']
        restaurant['price_range'] = d['priceRange']         #'$11-30'
        restaurant['cuisine'] = d['servesCuisine']          #'Italian'
        restaurant['num_review'] = len(d["review"])         # Num of reviews
        
        reviews  = d["review"]
        rating = 0
        for review in reviews:
            rating += review['reviewRating']['ratingValue']
        restaurant['rating'] = rating/len(d["review"])

        info.append(restaurant)

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