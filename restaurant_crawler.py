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
    Extract restaurants name, zipcode, price, 
        cuisine, num of reviews, average rating
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
    
            restaurant['name'] = d['name'].replace('&apos;',"'").\
                    replace('&amp;', "&")                       # Name: deal with ' and &
            restaurant['zip_code'] = d['address']['postalCode'] # Zipcode

            if 'priceRange' in d:
                price = re.findall(r'[0-9]+', d['priceRange'])  # Price
                if len(price) == 2:
                    restaurant['price'] = (float(price[1]) + float(price[0])) / 2
                else:
                    restaurant['price'] = price[0]
            else:
                restaurant['price'] = 0

            restaurant['cuisine'] = d['servesCuisine']          # Cuisine

            restaurant['num_review'] = len(d["review"])         # Num of reviews
            
            reviews  = d["review"]                              # Avg Rating
            if len(d['review']) != 0:
                rating = 0
                for review in reviews:
                    rating += review['reviewRating']['ratingValue']
                restaurant['rating'] = rating/len(d["review"])
            else:
                restaurant['rating'] = 0

            info.append(restaurant)
        
        else:
            print("empty tag", url)

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