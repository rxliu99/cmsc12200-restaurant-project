from math import radians, cos, sin, asin, sqrt
import sqlite3
import os
import pandas as pd
import numpy as np

csv_path = "info_0306.csv"
info = pd.read_csv(csv_path, header = 0, index_col = 0)

'''
print(info)
new_info =info[info["zip_code"] == 60622]
print(new_info)
'''
class Restaurants:
    def __init__(self, db_file):
        self.db = db_file

    '''
    def execute_sql(self, sql, args = []):
        connection = sqlite3.connect(self.db)
        c = connection.cursor()
        ob = c.execute(sql, args)
        results = ob.fetchall()

        return results
    '''

    def area_division(self, area):
        area_sliced = self.db[self.db["zip_code"] == area]
        #print(area_sliced)

        return area_sliced


    def cuisine_division(self, cuisine):
        cuisine_sliced = self.db[self.db["cuisine"] == cuisine]

        return cuisine_sliced


    def double_division(self, cuisine, area):
        sliced = self.area_division(area)
        #print(sliced)
        double_sliced = sliced[sliced["cuisine"] == cuisine]

        return double_sliced


    def rank_rating(self, dataframe, name, categories):
        #print(dataframe)
        ranking = []
        for category in categories:
            #print(name)
            #print(category)
            new_df = dataframe[dataframe[name] == category]
            #rslt_df = dataframe[dataframe[name] == category]
            #print(new_df)
            ratings = new_df["rating"].tolist()
            if ratings:
                avg_rating = np.mean(new_df["rating"].tolist())
                ranking.append((avg_rating, category))
        ranking.sort(reverse = True)

        return ranking


    def get_avg_price(self, dataframe, name, categories):
        avg_prices = []
        for category in categories:
            new_df = dataframe[dataframe[name] == category]

            ###modify when csv price range data type is changed
            prices = new_df["price_range"].tolist()
            new_prices = []
            for price in prices:
                if price == "$11-30":
                    new_prices.append(20.5)
                elif price == "Above $61":
                    new_prices.append(70.0)
                elif price == "$31-60":
                    new_prices.append(45.5)
                elif price == "Under $10":
                    new_prices.append(5.0)

            if new_prices:
                avg_price = np.mean(new_prices)
                avg_prices.append((avg_price, category))
        avg_prices.sort(reverse = True)

        return avg_prices

    #以下三个合并
    def cuisine_return(self, cuisine):
        all_info = self.cuisine_division(cuisine)
        #print(all_info)
        areas = set(self.db["zip_code"].tolist())
        ranking = self.rank_rating(all_info, "zip_code", areas)
        prices = self.get_avg_price(all_info, "zip_code", areas)
        num_rest = len(all_info)

        return num_rest, ranking, prices


    def area_return(self, area):
        all_info = self.area_division(area)
        #print(all_info)
        cuisines = set(self.db["cuisine"].tolist())
        ranking = self.rank_rating(all_info, "cuisine", cuisines)
        prices = self.get_avg_price(all_info, "cuisine", cuisines)
        num_rest = len(all_info)

        return num_rest, ranking, prices


    def double_return(self, cuisine, area):
        all_info = self.double_division(cuisine, area)
        #print(all_info)
        num_rest = len(all_info)

        ###modify when csv price range data type is changed
        prices = all_info["price_range"].tolist()
        new_prices = []
        for price in prices:
            if price == "$11-30":
                new_prices.append(20.5)
            elif price == "Above $61":
                new_prices.append(70.0)
            elif price == "$31-60":
                new_prices.append(45.5)
            elif price == "Under $10":
                new_prices.append(5.0)

        if new_prices:
            #print(new_prices)
            avg_price = np.mean(new_prices)
        else:
            avg_price = None

        ratings = [all_info["rating"].tolist()]
        if ratings:
            avg_rating = np.mean(ratings)
        else:
            avg_rating = None

        return num_rest, avg_price, avg_rating


x = Restaurants(info)
result = x.cuisine_return("Italian")
print(result)
result = x.area_return(60614)
print(result)
result = x.double_return("Italian", 60622)
print(result)

