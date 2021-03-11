#   CMSC 12200 - Winter 21
#   Project Name
#       Caroline Jiang
#       Julie Fan
#       Laurinda Zhang
#       Michelle Liu
############################################################

import link_crawler
import restaurant_crawler
import housing_crawler
#import regression
import pandas as pd
import csv

def scrape_data():
    '''
    '''
    # link crawler
    restaurant_links = link_crawler.get_restaurant_links()

    # Write 240 links to txt file
    with open(r"links.txt", "w") as f:
        f.writelines(restaurant_links)
        f.close()

    # restaurant crawler
    restaurant_info = restaurant_crawler.get_info(restaurant_links)
    # convert to df then write to csv
    df_restaurant = pd.DataFrame.from_dict(restaurant_info, orient='columns')
    df_restaurant.to_csv('info.csv', index=False)
    
    # convert zip_code col in info.csv to a list of zipcodes
    df_restaurant = pd.read_csv("info.csv", header=0)
    lst_zipcode = list(set(df_restaurant.zip_code))

    '''
    lst_zipcode = list(set(df_restaurant.zip_code))
    '''

    # rent crawler
    housing_links = housing_crawler.get_links(lst_zipcode)
    housing_info = housing_crawler.go(housing_links)

    df_housing = pd.DataFrame.from_dict(housing_info, orient='index').reset_index()
    df_housing.columns = ['zip_code', 'housing_price', 'median_income']

    # merge two dfs
    df_final = df_restaurant.merge(df_housing, on='zip_code')
    
    # write final df to csv
    df_final.to_csv('final.csv', index=False)


def run_regression():


    # regression

    # selection


