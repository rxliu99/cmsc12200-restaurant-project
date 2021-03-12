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
        links (list): a list of links returned by link_crawler.py
        
    Output:
        info (dict): a dictionary of restaurant info
    '''
    info = []

    for url in links:
        print("start at", url)
        restaurant = {}
        request = util.get_request(url)
        if request is not None:
            text = util.read_request(request)
            soup = bs4.BeautifulSoup(text, "html5lib")
            tag = soup.find('script', type='application/ld+json')

            if tag is not None:
                d = json.loads(tag.text)
        
                restaurant['restaurant_name'] = d['name'].replace('&apos;',"'").\
                        replace('&amp;', "&")
                restaurant['zip_code'] = d['address']['postalCode']

                if 'priceRange' in d:
                    if d['priceRange'] == "Above $61":
                        restaurant['price'] = 70
                    elif d['priceRange'] == "Under $10":
                        restaurant['price'] = 5
                    else:
                        price = re.findall(r'[0-9]+', d['priceRange'])
                        #Average of price upper and lower bounds
                        restaurant['price'] = (float(price[1]) +\
                                    float(price[0])) / 2
                else:
                    restaurant['price'] = None

                restaurant['cuisine'] = d['servesCuisine'].replace('&amp;', "&")

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
                print("the link gives an empty tag")
        else:
            print("empty request", url)

    return info
