#This file aims at completing the multiple linear regression with the data
#crawled from Yelp.com and Rentcafe.com

import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

df_final = pd.read_csv('final_0313.csv')
df_by_zipcode = df_final.groupby('zip_code')['price'].mean().reset_index()
df_by_zipcode = df_by_zipcode[df_by_zipcode['price'].notna()]
df_housing = df_final[["zip_code", "housing_price", "median_income"]]
df_housing = df_housing.drop_duplicates()
zipcode_info = df_by_zipcode.merge(df_housing, on='zip_code')


def linear_regression(zipcode_info):
    '''
    Treat average rent and average income as the predictor variables and 
    consider the average restaurant price as the response variable. 
    Then, perform multiple linear regression.

    Input:
        zipcode_info: the pandas dataframe created by reading the csv file

    Returns: a tuple of intercept and coefficients, where coefficients is
        a list of two floats
    '''
    X = zipcode_info[['housing_price', 'median_income']]
    Y = zipcode_info['price']

    regression = linear_model.LinearRegression()
    regression.fit(X, Y)

    intercept = regression.intercept_
    coefficients = regression.coef_

    return intercept, coefficients


def find_outliers(zipcode_info):
    '''
    Find the outliers in the restaurant price based on the regression model.

    Inputs:
        zipcode_info: the pandas dataframe created by reading the csv file
    
    Returns: a list of zipcodes for which the restaurant price is an outlier
    '''
    outliers = []
    code_residule = []

    intercept, coefficients = linear_regression(zipcode_info)

    for _, row in zipcode_info.iterrows():
        predict_res_price = intercept +\
                        coefficients[0] * row['housing_price'] +\
                        coefficients[1] * row['median_income']
        residule = row['price'] - predict_res_price
        code_residule.append((row['zip_code'], residule))

    residules = [i[1] for i in code_residule]
    mean = np.mean(residules)
    std = np.std(residules)

    for zip_code, residule in code_residule:
        std_residule = (residule - mean) / std
        if abs(std_residule) > 2:
            outliers.append(zip_code)
    
    outliers = list(set(outliers))

    return outliers


def scatterplot(zipcode_info):
    '''
    Create a 3D scatter plot of 1) the data crawled from the websites and
    2) the best-fit line obtained by the multiple linear regression.

    Inputs:
        zipcode_info: the pandas dataframe created by reading the csv file
    '''
    intercept, coefficients = linear_regression(zipcode_info)

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.set(xlabel='Average rent ($/square feet)', ylabel='Average income ($)',\
           zlabel='Average restaurant price ($)',\
           title='Relationship between rent, income, and restaurant price')
    
    rent_array = zipcode_info['housing_price'].values
    income_array = zipcode_info['median_income'].values
    X, Y = np.meshgrid(rent_array, income_array)

    res_price_array = zipcode_info['price'].values
    intercept, coefficients = linear_regression(zipcode_info)
    predict_res_price = intercept + coefficients[0] * X + coefficients[1] * Y
    
    ax.plot_surface(X, Y, predict_res_price)
    
    ax.scatter3D(rent_array, income_array, res_price_array)

    plt.show()

#x = linear_regression(zipcode_info)
#print(x)
#y = find_outliers(zipcode_info)
#print(y)
#scatterplot(zipcode_info, x[0], x[1])