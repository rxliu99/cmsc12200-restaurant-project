#This file is the regression portion of the interface

import pandas as pd
import regression

df_final = pd.read_csv('final_0313.csv')
df_by_zipcode = df_final.groupby('zip_code')['price'].mean().reset_index()
df_by_zipcode = df_by_zipcode[df_by_zipcode['price'].notna()]
df_housing = df_final[["zip_code", "housing_price", "median_income"]]
df_housing = df_housing.drop_duplicates()
info = df_by_zipcode.merge(df_housing, on='zip_code')
zip_codes = list(set(info["zip_code"].tolist()))
zip_codes = [str(i) for i in zip_codes]

def zipcode_price ():
    while True:
        print("----------------------------------------------------------------------------------------------------")
        print("Which area do you want to search for?")
        print("Please enter a Chicago zip code.")
        answer = input("You can enter one of the following: " + "; ".join(zip_codes) + "\n")
        if answer == "quit":
            break
        elif answer not in zip_codes:
            print("Oops! Please enter a valid zip code of Chicago from the list above.")
        else:
            intercept, coefficients = regression.linear_regression(info)

            rent = info.loc[info["zip_code"] == int(answer)].values.tolist()[0][2]
            income = info.loc[info["zip_code"] == int(answer)].values.tolist()[0][3]
            price = intercept +\
                    coefficients[0] * rent +\
                    coefficients[1] * income
            price = round(price, 2)
            print("The optimal restaurant price in " + answer + "is $" + str(price) + " .")
            answer2 = input("Do you want to search another area? Y/N\n")
            if answer2 == "N" or answer2 == "quit":
                break
            else:
                zipcode_price()
            break

def outlier():
    while True:
        lst = []
        intercept, coefficients = regression.linear_regression(info)
        outliers = regression.find_outliers(info)
        for outlier in outliers:
            price = info.loc[info["zip_code"] == int(outlier)].values.tolist()[0][1]
            rent = info.loc[info["zip_code"] == int(outlier)].values.tolist()[0][2]
            income = info.loc[info["zip_code"] == int(outlier)].values.tolist()[0][3]
            opt_price = intercept + coefficients[0] * rent + coefficients[1] * income
            price = round(price, 2)
            opt_price = round(price, 2)
            lst.append((int(outlier), price, opt_price))

        for item in lst:
            print("The area " + str(item[0]) + " is an outlier.")
            print("The current average restaurant price is $" + str(item[1]) + ".")
            print("The optimal restaurant price is $" + str(item[2]) + ".")
            if item[1] > item[2]:
                print("We recommend opening a restaurant with the price in the range $" \
                      + str(item[2]) + " - $" + str(item[1]) + " .")
            if item[1] < item[2]:
                print("We recommend opening a restaurant with the price in the range $" \
                      + str(item[1]) + " - $" + str(item[2]) + " .")
            print("Please note that the outliers might exist due to the lack of enough data.")
        break

def graph():
    while True:
        regression.scatterplot(info)
        break

print("Enter 'quit' at any time to quit.")

while True:
    print("Which piece of information would you like to see?")
    answer0 = input("A. Optimal price in an area    B. Outliers for price    C. Graph\n")
    if answer0 == "A":
        zipcode_price()
    elif answer0 == "B":
        outlier()
    elif answer0 == "C":
        graph()
    elif answer0 == "quit":
        break
    else:
        print("Please enter either A or B or C.")