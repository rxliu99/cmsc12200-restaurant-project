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
    df_restaurant.to_csv('info_0312.csv', index=False)
    
    
    # convert zip_code col in info.csv to a list of zipcodes
    lst_zipcode = list(set(df_restaurant.zip_code))

    '''
    lst_zipcode = list(set(df_restaurant.zip_code))
    '''

    # rent crawler
    housing_links = housing_crawler.get_links(lst_zipcode)
    housing_info = housing_crawler.go(housing_links)

    df_housing = pd.DataFrame.from_dict(housing_info, orient='index').reset_index()
    df_housing.columns = ['zip_code', 'housing_price', 'median_income']
    df_housing['zip_code'] = df_housing['zip_code'].astype(str)

    # merge two dfs
    df_final = df_restaurant.merge(df_housing, on='zip_code')
    
    # write final df to csv
    df_final.to_csv('final_0312.csv', index=False)

    # read df from final.csv and organize the df by zip_codes & avg price
    df_final = pd.read_csv('final_0312.csv')
    df_by_zipcode = df_final.groupby('zip_code')['price'].mean().reset_index()
    # Drop if price is None
    df_by_zipcode = df_by_zipcode[df_by_zipcode['price'].notna()]
    # Drop if housing_price is None
    df_by_zipcode = df_by_zipcode[df_by_zipcode['housing_price'].notna()]

    #######Try restaurant crawler#####
    import restaurant_crawler, chicago_links
    restaurant_info = restaurant_crawler.get_info(chicago_links.links())
    # will get a dictionary, then follow line 29-30 and save to csv