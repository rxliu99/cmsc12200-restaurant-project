#This file aims at completing the multiple linear regression with the data
#crawled from Yelp.com and Rentcafe.com

#The capitalized variable names in this file will be changed when the final csv is created
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


#Might need to add a function to get the ideal csv from the two individual csv
#files from the two crawlers

#zipcode_info = pd.read_csv('CSV_FILE_NAME') -- should be the output of the function above

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
    X = zipcode_info[['RENT', 'INCOME']]
    Y = zipcode_info['RES_PRICE']

    regression = linear_model.LinearRegression()
    regression.fit(X, Y)

    intercept = regression.intercept_
    coefficients = regression.coefficient_

    return intercept, coefficients

def find_outliers(zipcode_info):
    '''
    Find the outliers in the restaurant price based on the regression model.

    Inputs:
        zipcode_info: the pandas dataframe created by reading the csv file
    
    Returns: a list of zipcodes for which the restaurant price is an outlier
    '''
    outliers = []

    zipcode = zipcode_info['ZIPCODE'].values
    res_price = zipcode_info['RES_PRICE'].values
    intercept, coefficients = linear_regression(zipcode_info)
    predict_res_price = intercept +\
                        coefficients[0] * rent_array +\
                        coefficients[1] * income_array
    
    residule = res_price - predict_res_price
    mean = mean(residule)
    std = std(residule)
    standardized_residule = (residule - mean) / std

    array = np.concatneate((zipcode, standardized_residule), axis=1)
    dataframe = pd.DataFrame(array, columns=['zipcode', 'residule'])

    for row in dataframe.iterrows():
        zipcode, residule = row
        if abs(residule) > 3:
            outliers.append(zipcode)

    return outliers

def scatterplot(zipcode_info, intercept, coefficients):
    '''
    Create a 3D scatter plot of 1) the data crawled from the websites and
    2) the best-fit line obtained by the multiple linear regression.

    Inputs:
        zipcode_info: the pandas dataframe created by reading the csv file
    '''
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.set(xlabel='Average rent ($/square feet)', ylabel='Average income ($)',\
           zlabel='Average restaurant price ($)',\
           title='Relationship between rent, income, and restaurant price')
    
    rent_array = zipcode_info['RENT'].values
    income_array = zipcode_info['INCOME'].values
    res_price_array = zipcode_info['RES_PRICE'].values
    intercept, coefficients = linear_regression(zipcode_info)
    predict_res_price = intercept +\
                        coefficients[0] * rent_array +\
                        coefficients[1] * income_array
    
    ax.plot3D(rent_array, income_array, predict_res_price)
    
    ax.scatter3D(rent_array, income_array, res_price_array)

    #fig.savefig('relationship.png')
    plt.show()

