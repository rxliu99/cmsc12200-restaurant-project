# Crawling data from Yelp

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


def get_loc_cook():
    with open(r"c:\Users\35653\Desktop\CS122\project\cook_county_zips.csv") as cook_zips:
        reader = csv.reader(cook_zips)

        city_state = [(row[4], row[5]) for row in reader]
        del city_state[0]
        city_state = set(city_state)

    return city_state


def get_cities():
    city_state = get_loc_cook()
    cook_cities = []
    for ele in city_state:
        cook_cities.append(ele[0])

    #print(cook_cities)
    #print(len(cook_cities))

    url = 'https://www.rentcafe.com/sitemaps/us/il/average-rent-market-trends/'
    request = util.get_request(url)
    text = util.read_request(request)

    soup = bs4.BeautifulSoup(text, "html5lib")
    tags = soup.find_all('a', href=True, target="", role="")


    cities = []
    count = 0
    for tag in tags: 
        if "title" in tag.attrs: 
            city = tag['title']
            if city[0 : 15] == "Average Rent in":
                #print(city)
                city = city[16 :]
                #print(city)
                count += 1
                if city in cook_cities:
                    cities.append(city)

    #print(count)
    #print(len(cities))

    return cities


def get_restaurant_links_cook():
    cities = get_cities()

    city_state = get_loc_cook()
    new_city_state = []
    for ele in city_state:
        if ele[0] in cities:
            new_city_state.append(ele)

    page_suffix = [i for i in range(0, 231, 10)]
    #print(city_state)

    url_list = []
    for city, state in city_state:
        html = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=" + city.replace(" ", "") + "%2C%20" + state
        for suffix in page_suffix:
            html_page = html + "&start=" + str(suffix)
            url_list.append(html_page)

    r'''
    with open(r"c:\Users\35653\Desktop\CS122\project\urls.txt", "w") as write_file:
        write_file.writelines(url_list)

        write_file.close()
    '''

    url_list = ["https://www.yelp.com/search?find_desc=Restaurants&find_loc=Lyons%2C%20IL&start=190"]
    for url in url_list:
        request = util.get_request(url)
        if request:

            text = util.read_request(request)

            soup = bs4.BeautifulSoup(text, "html5lib")
            tags = soup.find_all('a', href=True, target="", role="")

            # extract href links to restaurants
            links = []
            for tag in tags:  
                link = tag['href']
                link = util.convert_if_relative_url(url, link)
                link = util.remove_fragment(link)
                # Hardcoded filter
                if link[-11:] == "Restaurants":
                    if tag["name"] != '':
                        if link not in links:
                            links.append(link + "\n")
    return links


def get_restaurant_links_chicago():
    # start from searching "Restaurant", "Chicago" from yelp main page
    page_suffix = [i for i in range(0, 231, 10)]
    url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Chicago%2C%20IL&start='
    url_list = []

    for suffix in page_suffix:
        page_url = url + str(suffix)
        url_list.append(page_url)

    for url in url_list:
        print(url)

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
            # Hardcoded filter
            if link[-11:] == "Restaurants":
                if tag["name"] != '':
                    if link not in links:
                        links.append(link + "\n")
                        print(link)
        
        i = 5 + random.random() * 5
        time.sleep(i)

    return links


def get_rental_links():
    '''
    get rental links according to the zip codes of restaurants
    '''
    
    return None

#links = get_restaurant_links_chicago()
#with open(r"c:\Users\35653\Desktop\CS122\project\links3.txt", "w") as f:
#    f.writelines(links)
#    f.close()
