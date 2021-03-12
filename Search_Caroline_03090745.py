#from math import radians, cos, sin, asin, sqrt
import sqlite3
import os
import pandas as pd
import numpy as np
import math

####delete
csv_path = "final.csv"
info = pd.read_csv(csv_path, header = 0, index_col = 0)

'''
print(info)
new_info =info[info["zip_code"] == 60622]
print(new_info)
'''
class Restaurants:
    def __init__(self, db_file):
        self.db = db_file


    def area_division(self, area):
        area_sliced = self.db[self.db["zip_code"] == area]
        #print(area_sliced)

        return area_sliced


    def cuisine_division(self, cuisine):
        cuisine_sliced = self.db[self.db["cuisine"] == cuisine]

        return cuisine_sliced


    def double_division(self, cuisine, area):
        sliced = self.area_division(area)
        double_sliced = sliced[sliced["cuisine"] == cuisine]

        return double_sliced


    def rank_rating(self, dataframe, name, categories):
        #print(dataframe)
        ranking = []
        for category in categories:
            #print(name)
            #print(category)
            new_df = dataframe[dataframe[name] == category]
            ratings = new_df["rating"].tolist()
            if ratings:
                avg_rating = np.mean(new_df["rating"].tolist())
                avg_rating = round(avg_rating, 2)
                ranking.append((avg_rating, category))
        ranking.sort(reverse = True)

        return ranking


    def get_avg_price(self, dataframe, name, categories):
        avg_prices = []
        for category in categories:
            new_df = dataframe[dataframe[name] == category]
            prices = new_df["price"].tolist()

            if len(prices) != 0:
                avg_price = np.nanmean(prices)
                avg_price = round(avg_price, 2)
                avg_prices.append((avg_price, category))
        avg_prices.sort(reverse = True)

        return avg_prices


    def single_return(self, cuisine = None, area = None):
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
        all_info = self.double_division(cuisine, area)
        num_rest = len(all_info)
        prices = all_info["price"].tolist()

        if len(prices) != 0:
            avg_price = np.nanmean(prices)
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

#x = Restaurants(info)
#y = x.double_return("Italian", 60622)
#print(y)



