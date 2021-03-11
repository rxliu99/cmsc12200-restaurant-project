#   CMSC 12200 - Winter 21
#   Project Name
#       Caroline Jiang
#       Julie Fan
#       Laurinda Zhang
#       Michelle Liu
############################################################

import link_crawler
import restaurant_crawler
#import rent_income_crawler
#import regression

def scrape_data():
    '''
    '''
    # link crawler
    links = link_crawler.get_restaurant_links()

    # Write 240 links to txt file
    with open(r"links.txt", "w") as f:
        f.writelines(links)
        f.close()

    # restaurant crawler
    df_restaurant = restaurant_crawler.get_info(links)

    # rent_income crawler

    # merge two dfs
    df_final = df_restaurant.merge(df_rent_income, on='zip_code')

    return df_final

def run_regression():


    # regression

    # selection


