import pandas as pd
import regression
from search import Restaurants

#Load all necessary dataframes and lists
info = pd.read_csv("final.csv", header = 0, index_col = 0)
df_by_zipcode = info.groupby("zip_code")["price"].mean().reset_index()
df_by_zipcode = df_by_zipcode[df_by_zipcode["price"].notna()]
df_housing = info[["zip_code", "housing_price", "median_income"]]
df_housing = df_housing.drop_duplicates()
zipcode_info = df_by_zipcode.merge(df_housing, on="zip_code")
restaurants = Restaurants(info)

all_cuisines = list(set(info["cuisine"].tolist()))
all_cuisines.sort()
zip_codes = set(info["zip_code"].tolist())
zip_codes = [str(i) for i in zip_codes]
zip_codes.sort()

#Helper functions for the interface
def area_search():
    while True:
        print("----------------------------------------------------------------------------------------------------")
        print("Which area do you want to search for?")
        print()
        print("Please enter a Chicago zip code and hit enter.")
        print()
        str2 = input("You can enter one of the following: " + "; ".join(zip_codes) + "\n")
        print()
        if str2 == "quit":
            break
        elif str2 not in zip_codes:
            print("Oops! Please enter a valid zip code of Chicago from the list above.")
            print()
        else:
            print("====================================================================================================")
            print("Here's the search result for area with zipcode " + str2 + ":")
            print()
            returns = restaurants.single_return(None, int(str2))
            print("Number of restaurants in " + str2 + ":")
            print(returns[0])
            print()

            print("----------------------------------------------------------------------------------------------------")
            print("Ratings of different cuisines in " + str2 + ":")
            rank = 1
            for i in returns[1]:
                print("No. " + str(rank) + ": ")
                print("Cuisine Type: " + str(i[1]))
                print("Average Rating: " + str(i[0]))
                print(" ")
                rank += 1

            print("----------------------------------------------------------------------------------------------------")
            print("Average prices of different cuisines in " + str2 + ":")
            rank = 1
            for i in returns[2]:
                print("No. " + str(rank) + ": ")
                print("Cuisine Type: " + str(i[1]))
                print("Average Price: " + str(i[0]))
                print(" ")
                rank += 1

            print("----------------------------------------------------------------------------------------------------")
            print("Recommended price in area " + str2 + " is :")
            price = regression.predict_price(int(str2))
            print("$" + str(price))
            print()

            print("====================================================================================================")
            print("Do you want to search another area?")
            str3 = input("Enter 'quit' to quit and any other thing to continue.\n")
            if str3 == "quit":
                break

def cuisine_search():
    while True:
        print("----------------------------------------------------------------------------------------------------")
        print("Which cuisine do you want to search for?")
        print()
        print("Please enter a cuisine type and hit enter.")
        print()

        str2 = input("You can enter one of the following:\n" + "; ".join(all_cuisines) + "\n")
        print()
        if str2 == "quit":
            break
        elif str2 not in all_cuisines:
            print("Oops! Please enter a valid cuisine type from the list above.")
            print()
        else:
            print("====================================================================================================")
            print("Here's the search result for cuisine type " + str2 + ":")
            returns = restaurants.single_return(str2, None)
            print("Number of restaurants with " + str2 + " cuisine:")
            print(returns[0])

            print()
            print("----------------------------------------------------------------------------------------------------")
            print("Ratings of different areas under " + str2 + " cuisine:")
            print()
            rank = 1
            for i in returns[1]:
                print("No. " + str(rank) + ": ")
                print("Zipcode: " + str(i[1]))
                print("Average Price: " + str(i[0]))
                print(" ")
                rank += 1

            print("----------------------------------------------------------------------------------------------------")
            print("Average prices of different areas under " + str2 + " cuisine:")
            print()
            rank = 1
            for i in returns[2]:
                print("No. " + str(rank) + ": ")
                print("Zipcode: " + str(i[1]))
                print("Average Rating: " + str(i[0]))
                print(" ")
                rank += 1

            print("====================================================================================================")
            print("Do you want to search another cuisine type?")
            str3 = input("Enter 'quit' to quit and any other thing to continue.\n")
            if str3 == "quit":
                break

def double_helper_area(cuisine):
    while True:
        print("----------------------------------------------------------------------------------------------------")
        print("Which area do you want to search for?")
        print()
        print("Please enter a Chicago zip code and hit enter.")
        print()
        str2 = input("You can enter one of the following: " + "; ".join(zip_codes) + "\n")
        if str2 == "quit":
            break
        elif str2 not in zip_codes:
            print("Oops! Please enter a valid zip code of Chicago.")
            print()
        else:
            print("----------------------------------------------------------------------------------------------------")
            print("Here's the search result for " + cuisine + " type cuisine in " + str2 + ":")
            print()
            print("----------------------------------------------------------------------------------------------------")
            returns = restaurants.double_return(cuisine, int(str2))
            print("Number of restaurants with " + cuisine + " cuisine in " + str2 + ":")
            print(returns[0])
            print()
            print("Average price of restaurants with " + cuisine + " cuisine in " + str2 + ":")
            print(returns[1])
            print()
            print("Average rating of restaurants with " + cuisine + " cuisine in " + str2 + ":")
            print(returns[2])
            print("====================================================================================================")
            print("Do you want to search another pair of cuisine type and area?")
            str3 = input("Enter 'N' to quit and any other thing to continue.\n")
            if str3 == "N" or str3 == "quit":
                break
            else:
                double_search()
            break

def double_search():
    while True:
        print("----------------------------------------------------------------------------------------------------")
        print("Which cuisine do you want to search for?")
        print("Please enter a cuisine type and hit enter.")
        print()

        str2 = input("You can enter one of the following:\n" + "; ".join(all_cuisines) + "\n")
        print()
        if str2 == "quit":
            break
        elif str2 not in all_cuisines:
            print()
            print("Oops! Please enter a valid cuisine type.")
            print()
        else:
            double_helper_area(str2)
            break

def zipcode_price ():
    while True:
        print()
        print("====================================================================================================")
        print("Which area do you want to search for?")
        print("Please enter a Chicago zip code.")
        answer = input("You can enter one of the following: " + "; ".join(zip_codes) + "\n")
        if answer == "quit":
            break
        elif answer not in zip_codes:
            print("Oops! Please enter a valid zip code of Chicago from the list above.")
        else:
            intercept, coefficients = regression.linear_regression(info)

            rent = zipcode_info.loc[zipcode_info["zip_code"] == int(answer)]\
                   .values.tolist()[0][2]
            income = zipcode_info.loc[zipcode_info["zip_code"] == int(answer)]\
                     .values.tolist()[0][3]
            price = intercept +\
                    coefficients[0] * rent +\
                    coefficients[1] * income
            price = round(price, 2)

            print()
            print("----------------------------------------------------------------------------------------------------")
            print("The optimal restaurant price in " + answer + " is $" + str(price) + " .")
            print()
            print("----------------------------------------------------------------------------------------------------")
            print("Do you want to search another area?\n")
            answer2 = input("Enter 'quit' to quit and any other thing to continue.\n")
            if answer2 == "quit":
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
            price = zipcode_info.loc[zipcode_info["zip_code"] == int(outlier)]\
                    .values.tolist()[0][1]
            rent = zipcode_info.loc[zipcode_info["zip_code"] == int(outlier)]\
                   .values.tolist()[0][2]
            income = zipcode_info.loc[zipcode_info["zip_code"] == int(outlier)]\
                     .values.tolist()[0][3]
            opt_price = intercept + coefficients[0] * rent + coefficients[1] * income
            price = round(price, 2)
            opt_price = round(price, 2)
            lst.append((int(outlier), price, opt_price))

        for item in lst:
            print("----------------------------------------------------------------------------------------------------")
            print("The area " + str(item[0]) + " is an outlier.")
            print("The current average restaurant price is $" + str(item[1]) + ".")
            print("The optimal restaurant price is $" + str(item[2]) + ".")
            if item[1] > item[2]:
                print("We recommend opening a restaurant with the price in the range $" \
                      + str(item[2]) + " - $" + str(item[1]) + " .")
            if item[1] < item[2]:
                print("We recommend opening a restaurant with the price in the range $" \
                      + str(item[1]) + " - $" + str(item[2]) + " .")
            print()
        print("*Please note that the outliers might exist due to the lack of enough data.")
        break

def graph():
    while True:
        regression.scatterplot(info)
        break

#Interface
print("====================================================================================================")
print("Seeking to open a restaurant in Chicago but dishearted by the lack of information?")
print()
print("Welcome to Foodies' restraunt assistant bot, aiming to help you make informed decisions.")
print()
print("Enter 'quit' at any time to quit.")
print("====================================================================================================")
print()

while True:
    print("What idea you have in mind?")
    str = input("A. A neighborhood you have your eye on\nB. A cuisine you go crazy for\nC. You have both neighborhood and cuisine in mind\nD. Weirdly attracted to undiscovered business opportunities\nE. Just wanna check out the big picture across neighborhoods and cuisines")

    if str == "A":
        area_search()
    elif str == "B":
        cuisine_search
    elif str == "C":
        double_search()
    elif str == "D":
        outlier()
    elif str == "E":
        graph()
    elif str == "quit":
        break
    else:
        print("Oops! Please enter one of the following letters: A, B, C, D, E.")
