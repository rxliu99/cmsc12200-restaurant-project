#This is a crawler aiming at getting avg rent from rentcafe.com

import bs4
import re
import util
import json
import csv
import sys
import queue
import numpy as np


def get_links(lst_zipcode):
    '''
    Create links that correspond to searching specific zipcodes on rentcafe
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
        housing_links: a list of links obtained from inputing different
            zipcodes to the search bar of rentcafe.com
    Output: 
        csv file that saves information of average housing rent in chicago
    '''
    # a dictionary with zipcode as keys, avg rent price as values
    d = {}

    # start from the first zip_code...
    for link in housing_links:
        zip_code = np.int64(link[-5:])
        d[zip_code] = []
        request = util.get_request(link)
        text = util.read_request(request)
        soup = bs4.BeautifulSoup(text, "html5lib")
        pages_to_crawl = []
        # collect all subpages under this zipcode
        tags = soup.find('ul', class_="pagination")
        if tags is None:
            pages_to_crawl = [link]
        else:
            pages = tags.find_all('a', href=True)
            for a in pages:
                pages_to_crawl.append(a['href'])

        for url in pages_to_crawl:
            print(url)
            request = util.get_request(url)
            text = util.read_request(request)
            soup = bs4.BeautifulSoup(text, "html5lib")
            property_tags = soup.find_all('div', class_='item-information')
    
            for item in property_tags:
                d[zip_code].append(find_adj_price(item))
            
        d[zip_code] = np.mean([x for x in d[zip_code] if x != 0])
        
    return d
   

def find_adj_price(item):
    '''
    Input:
        an item-information tag for a property
    Output:
        bath-beds adjusted price index
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


'''
        with open(rental_link_chicago, 'w', newline="") as f:
            for zipcode_val in average_rent_chicago.keys():
                for avg_rent in average_rent_chicago[zipcode]:
                    f.write("%s|%s\n"%(zipcode_val. avg_rent)
                    # citation for the 3 lines above: https://www.tutorialspoint.com/How
                     # -to-save-a-Python-Dictionary-to-CSV-file



housing_links = ['https://www.rentcafe.com/apartments-for-rent/us/il/cook-county/60608',
 'https://www.rentcafe.com/apartments-for-rent/us/il/cook-county/60706',
 'https://www.rentcafe.com/apartments-for-rent/us/il/cook-county/60642',
 'https://www.rentcafe.com/apartments-for-rent/us/il/cook-county/60611',
 'https://www.rentcafe.com/apartments-for-rent/us/il/cook-county/60610',
 'https://www.rentcafe.com/apartments-for-rent/us/il/cook-county/60614',
 'https://www.rentcafe.com/apartments-for-rent/us/il/cook-county/60647',
 'https://www.rentcafe.com/apartments-for-rent/us/il/cook-county/60616',
 'https://www.rentcafe.com/apartments-for-rent/us/il/cook-county/60617',
 'https://www.rentcafe.com/apartments-for-rent/us/il/cook-county/60618',
 'https://www.rentcafe.com/apartments-for-rent/us/il/cook-county/60651',
 'https://www.rentcafe.com/apartments-for-rent/us/il/cook-county/60622',
 'https://www.rentcafe.com/apartments-for-rent/us/il/cook-county/60654',
 'https://www.rentcafe.com/apartments-for-rent/us/il/cook-county/60657',
 'https://www.rentcafe.com/apartments-for-rent/us/il/cook-county/60661',
 'https://www.rentcafe.com/apartments-for-rent/us/il/cook-county/60603',
 'https://www.rentcafe.com/apartments-for-rent/us/il/cook-county/60607']


 d = {'60608': 651.3594079989433,
 '60706': 529.1048120720031,
 '60642': 1100.8205656642476,
 '60611': 1282.6057161809783,
 '60610': 1176.4588865012627,
 '60614': 1007.0407958721607,
 '60647': 823.6626264280893,
 '60616': 998.164818375335,
 '60617': 437.0625528572675,
 '60618': 662.8823957034,
 '60651': 475.92579309765733,
 '60622': 907.9714573031821,
 '60654': 1176.1860352195345,
 '60657': 900.1663655564432,
 '60661': 1259.30324370023,
 '60603': 1311.5895460415904,
 '60607': 1045.4380014381861}

 '''