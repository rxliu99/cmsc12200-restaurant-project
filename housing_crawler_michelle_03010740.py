#This is a crawler aiming at getting information from rentcafe.com

import bs4
import re

#To do:
#figure out how to get rental_link_chicago
#write code for finding the size of each apartment
#determine the best way to save the information (and what to save)
#save the information into a csv file

def get_apart_link(soup):
    '''
    Obtain the apartment names and the link of the apartments.

    Inputs:
        soup: a beautifulsoup object

    Returns: a dictionary that maps the name of apartment to its link
    '''
    apart_dict = {}
    tag_list = soup.find_all('div', class_='item-information')
    for item in tag_list:
	    target_portion = item.find('div', class_='item-header')
	    apart_name = target_portion.find(‘h2’).find(‘a’).contents
	    apart_link = target_portion.find(‘h2’).find(‘a’)[‘href’]
	    apart_dict[apart_name] = apart_link

    return apart_dict

def get_average_rent(soup):
    '''
    Obtain the average rent of a zipcode.

    Inputs:
        soup: a beautifulsoup object
    
    Returns: a tuple of zipcode and average rent
    '''
    zipcode = 0
    average_rent = 0
    tag_list_b = soup.find_all(‘script’, type=‘application/ld+json’)
    for item in tag_list_b:
	    text = item[0].contents[0]
	    target_text = re.findall('The average rent in \d{5} is \$\d,\d{3}', text)
        zipcode = re.findall('\d{5}', target_text)
	    average_rent = re.findall('\d,\d{3}', target_text)

    return zipcode, average_rent

def go(rental_link_chicago):
    '''
    Main function

    Inputs:
        rental_link_chicago: a list of links obtained from inputing different
            zipcodes to the search bar of rentcafe.com
    '''
    apart_dict_chicago = {}
    average_rent_chicago = {}
    for link in rental_link_chicago:
        html = open(link).read
        soup = bs4.BeautifulSoup(html)
        zipcode, average_rent = get_average_rent(soup)
        apart_dict = get_apart_link(soup)
        apart_dict_chicago[zipcode] = apart_dict
        average_rent_chicago[zipcode] = average_rent

    return apart_dict_chicago, average_rent_chicago