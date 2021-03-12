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
    
    Input:
        links (list)
    Output:
        info (dict)
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
                    replace('&amp;', "&")
            restaurant['zip_code'] = d['address']['postalCode']

            if 'priceRange' in d:                               
                price = re.findall(r'[0-9]+', d['priceRange'])
                #Average of price upper and lower bounds
                if len(price) == 2:
                    restaurant['price'] = (float(price[1]) +\
                             float(price[0])) / 2
                else:
                    restaurant['price'] = price[0]
            else:
                restaurant['price'] = 0

            restaurant['cuisine'] = d['servesCuisine']

            restaurant['num_review'] = len(d["review"])
            
            reviews  = d["review"]
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
