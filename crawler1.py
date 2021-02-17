# Crawling data from Yelp

import re
import util
import bs4
import queue
import json
import sys
import csv


url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Chicago%2C%20IL&start=0'
request = util.get_request(url)
text = util.read_request(request)
soup = bs4.BeautifulSoup(text, "html5lib")