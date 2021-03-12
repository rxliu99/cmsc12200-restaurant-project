#   CMSC 12200 Winter 21 Project
#   Foodie
#
#    Implementing the search function of the software
#    Mapping data retrived from Yelp.com and Rentcafe.com 
#    to inputs specified by the user
#
############################################################

import sqlite3
import os
import pandas as pd
import numpy as np
import math


class Restaurants:
    def __init__(self, db_file):
        '''
        Constructs a Restaurant class from a db_file
        '''
        self.db = db_file


    def area_division(self, area):
        '''
        Returns a sliced dataframe specific to the input zip code
        '''
        area_sliced = self.db[self.db["zip_code"] == area]

        return area_sliced


    def cuisine_division(self, cuisine):
        '''
        Returns a sliced dataframe specific to the input cuisine type
        '''    
        cuisine_sliced = self.db[self.db["cuisine"] == cuisine]

        return cuisine_sliced


    def double_division(self, cuisine, area):
        '''
        Returns a sliced dataframe specific to the input cuisine type
        and the input zip code
        '''    
        sliced = self.area_division(area)
        double_sliced = sliced[sliced["cuisine"] == cuisine]

        return double_sliced


    def rank_rating(self, dataframe, name, categories):
        '''
        Rank the ratings of restraunts under different categories

        Inputs:
        dataframe (db_file): the dataframe to be used
        name (string): name of the categories
        categories (list): a list of categories to be ranked
        '''
        ranking = []
        for category in categories:
            new_df = dataframe[dataframe[name] == category]
            ratings = new_df["rating"].tolist()
            if ratings:
                avg_rating = np.mean(new_df["rating"].tolist())
                avg_rating = round(avg_rating, 2)
                ranking.append((avg_rating, category))
        ranking.sort(reverse = True)

        return ranking


    def get_avg_price(self, dataframe, name, categories):
        '''
        Rank the prices of restraunts under different categories

        Inputs:
        dataframe (db_file): the dataframe to be used
        name (string): name of the categories
        categories (list): a list of categories to be ranked
        '''
        avg_prices = []
        for category in categories:
            new_df = dataframe[dataframe[name] == category]
            prices = new_df["price"].tolist()

            clean_prices = []
            for price in prices:
                if np.isnan(price) == False:
                    clean_prices.append(price)
            if len(clean_prices) != 0:
                avg_price = np.mean(clean_prices)
                avg_price = round(avg_price, 2)
                avg_prices.append((avg_price, category))
        avg_prices.sort(reverse = True)

        return avg_prices


    def single_return(self, cuisine = None, area = None):
        '''
        Returns related info when either cuisine type or area is specified

        Inputs:
        cuisine (str): a cuisine type
        area (int): a zip code

        Returns:
        related information about the number of restaurants, rating and prices
        '''
        if cuisine and not area:
            all_info = self.cuisine_division(cuisine)
            areas = set(self.db["zip_code"].tolist())
            ranking = self.rank_rating(all_info, "zip_code", areas)
            prices = self.get_avg_price(all_info, "zip_code", areas)
        elif area and not cuisine:
            all_info = self.area_division(area)
            cuisines = set(self.db["cuisine"].tolist())
            ranking = self.rank_rating(all_info, "cuisine", cuisines)
            prices = self.get_avg_price(all_info, "cuisine", cuisines)
        
        num_rest = len(all_info)

        return num_rest, ranking, prices


    def double_return(self, cuisine, area):
        '''
        Returns related info when both cuisine type and area are specified

        Inputs:
        cuisine (str): a cuisine type
        area (int): a zip code

        Returns:
        related information about the number of restaurants,
        average rating and average prices
        '''
        all_info = self.double_division(cuisine, area)
        num_rest = len(all_info)
        prices = all_info["price"].tolist()
        clean_prices = []

        for price in prices:
            if np.isnan(price) == False:
                clean_prices.append(price)

        if len(clean_prices) != 0:
            avg_price = np.mean(clean_prices)
            avg_price = round(avg_price, 2)

        else:
            avg_price = None

        ratings = all_info["rating"].tolist()
        if len(ratings) != 0:
            avg_rating = np.mean(ratings)
            avg_rating = round(avg_rating, 2)
        else:
            avg_rating = None

        return num_rest, avg_price, avg_rating




