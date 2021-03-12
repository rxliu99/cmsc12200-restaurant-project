# Crawling avg rent and median income for each zip code on rentcafe.com

import bs4
import re
import util
import json
import csv
import sys
import queue
import numpy as np
import csv
import pandas as pd


def get_links(lst_zipcode):
    '''
    Create links that correspond to searching specific zipcodes on rentcafe

    Input:
        lst_zipcode (list): a list of zipcodes
    Output:
        housing_links (list): a list of links
    '''
    housing_links = []
    url = 'https://www.rentcafe.com/apartments-for-rent/us/il/cook-county/'
    
    for zipcode in lst_zipcode:
        new_url = url + str(zipcode)
        housing_links.append(new_url)

    return housing_links


def go(housing_links):
    '''
    Main function
    Inputs:
        housing_links (list): a list of links obtained from inputing different
            zipcodes to the search bar of rentcafe.com
    Output: 
        d (dict): a dictionary mapping each zipcode to a tuple (mean_price, income)
    '''
    # a dictionary with zipcode as keys, avg rent price as values
    d = {}

    # start from the first zip_code...
    for link in housing_links:
        zip_code = str(link[-5:])
        d[zip_code] = []
        request = util.get_request(link)
        text = util.read_request(request)
        soup = bs4.BeautifulSoup(text, "html5lib")

        # find median income under this zipcode
        li_tags = soup.find_all('li', class_="medium")
        income = np.int64(re.findall(r'\d+(?:,\d+)?', li_tags[2].text)[0].replace(',',''))

        # collect all subpages under this zipcode
        pages_to_crawl = []
        tags = soup.find('ul', class_="pagination")
        if tags is None:
            pages_to_crawl = [link]
        else:
            pages = tags.find_all('a', href=True)
            for a in pages:
                if a['href'] not in pages_to_crawl:
                    pages_to_crawl.append(a['href'])

        for url in pages_to_crawl:
            request = util.get_request(url)
            text = util.read_request(request)
            soup = bs4.BeautifulSoup(text, "html5lib")
            property_tags = soup.find_all('div', class_='item-information')
    
            for item in property_tags:
                d[zip_code].append(find_adj_price(item))
            
        d[zip_code] = (np.mean([x for x in d[zip_code] if x != 0]), income)
        
    return d
   

def find_adj_price(item):
    '''
    Find average rent adjusted by number of beds and baths
    
    Input:
        an item-information tag for a property
    Output:
        bath-beds adjusted avg price
    '''

    price_info = re.findall(r'\d+(?:,\d+)?', item.find('div',\
                     class_="price").text)
    # remove comma and convert to list of integers
    price = [int(x.replace(',','')) for x in price_info]
        
    # for those with price info, look into beds & bath info
    if price != []:
        avg_price = np.mean(price)

        details = item.find('ul', class_="property-basic-details")
        beds_info = re.findall(r'[0-9]+', details.find('li', \
                class_="data-beds").text.replace('Studio', '1'))
        
        # get avg num of beds for each property
        if len(beds_info) == 2:
            num_beds = (int(beds_info[1]) + int(beds_info[0])) / 2
        else:
            num_beds = int(beds_info[0])
        
        baths_info = details.find('li', class_="data-baths")
        if baths_info is None:
            num_baths = 0
            return avg_price / num_beds
        else: 
            baths_info = re.findall(r'[0-9]+', baths_info.text) 
            num_baths = np.mean([int(x) for x in baths_info])

            # incorporate num_baths into num_beds   
            bath_per_bed = num_baths / num_beds
            adj_num_beds = num_beds + bath_per_bed ** num_beds

            adj_price = avg_price / adj_num_beds
            return adj_price

    else:
        return 0