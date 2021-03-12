#   CMSC 12200 Winter 21 Project
#   Foodie
#
#   Obtain a final csv file by crawling links, restaurant 
#       information, and rent & income information
#
############################################################

import link_crawler
import restaurant_crawler
import housing_crawler
import pandas as pd
import csv

def scrape_data():
    '''
    Scrape restaurant from Yelp and rent & income data from RentCafe
    Combine to produce a csv file for future use
    '''
    # crawl restaurant links
    restaurant_links = link_crawler.get_restaurant_links()

    # Write 240 links to txt file for future reference
    with open(r"links.txt", "w") as f:
        f.writelines(restaurant_links)
        f.close()

    # crawl restaurant info
    restaurant_info = restaurant_crawler.get_info(restaurant_links)
    # convert to pandas dataframe then write to csv
    df_restaurant = pd.DataFrame.from_dict(restaurant_info, orient='columns')
    df_restaurant.to_csv('info.csv', index=False)
    
    # convert zip_code column in info.csv to a list of zipcodes
    lst_zipcode = list(set(df_restaurant.zip_code))

    # crawl rent & income info
    housing_links = housing_crawler.get_links(lst_zipcode)
    housing_info = housing_crawler.go(housing_links)

    df_housing = pd.DataFrame.from_dict(housing_info, orient='index').reset_index()
    df_housing.columns = ['zip_code', 'housing_price', 'median_income']
    df_housing['zip_code'] = df_housing['zip_code'].astype(str)

    # merge two dfs
    df_final = df_restaurant.merge(df_housing, on='zip_code')
    
    # write final df to csv
    df_final.to_csv('final.csv', index=False)
