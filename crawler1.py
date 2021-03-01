# Crawling data from Yelp

import re
import util
import bs4
import queue
import json
import sys
import csv

# start from searching "Restaurant", "Chicago" from yelp main page
url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Chicago%2C%20IL&start=0'
request = util.get_request(url)
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
                links.append(link)



##### REFERENCE #####
'''
# All links
<a class=" link__09f24__1MGLa photo-box-link__09f24__28L0f link-color--blue-dark__09f24__tK18E link-size--default__09f24__QvrjA" href="/biz/boxcar-bettys-chicago-2?osq=Restaurants" target="" name="" rel="">
<a class=" link__09f24__1MGLa link-color--inherit__09f24__3Cplm link-size--default__09f24__QvrjA" href="/search?cflt=sandwiches&amp;find_desc=Restaurants&amp;find_loc=Chicago%2C+IL" target="" name="" rel="" role="link">

# Repeated links
'https://www.yelp.com/biz/the-delta-chicago?osq=Restaurants'
'https://www.yelp.com/biz/the-delta-chicago?hrid=qtOXI4YDVJNFHs4GvZqGuA&osq=Restaurants'

<a class=" link__09f24__1MGLa link-color--inherit__09f24__3Cplm link-size--inherit__09f24__3Javq" href="/biz/penumbra-chicago?osq=Restaurants" target="" name="Penumbra" rel="">
<a class=" link__09f24__1MGLa link-color--blue-dark__09f24__tK18E link-size--inherit__09f24__3Javq" href="/biz/penumbra-chicago?hrid=_DHfzbvVXSfBoHjJHAx8kg&amp;osq=Restaurants" target="" name="" rel="">
'''