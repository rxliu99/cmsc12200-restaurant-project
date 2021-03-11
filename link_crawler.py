# Crawling restaurant links from Yelp

import re
import util
import bs4
import queue
import json
import sys
import csv
import pandas as pd
import numpy as np
import time
import random


def get_restaurant_links():
'''
Start from searching "Restaurant", "Chicago" on yelp main page,
and collect all restaurant links from 24 pages
'''

    page_suffix = [i for i in range(0, 231, 10)]
    url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Chicago%2C%20IL&start='
    url_list = []

    for suffix in page_suffix:
        page_url = url + str(suffix)
        url_list.append(page_url)

    links = []
    count = 0

    for url in url_list:
        count += 1
        print(count)
    
        request = util.get_request(url)
        text = util.read_request(request)

        soup = bs4.BeautifulSoup(text, "html5lib")
        tags = soup.find_all('a', href=True, target="", role="")

        for tag in tags:  
            link = tag['href']
            link = util.convert_if_relative_url(url, link)
            link = util.remove_fragment(link)
            if link[-11:] == "Restaurants":
                if tag["name"] != '':
                    if link not in links:
                        links.append(link + "\n")
                        print(link)
        
        i = 5 + random.random() * 5
        time.sleep(i)

    return links