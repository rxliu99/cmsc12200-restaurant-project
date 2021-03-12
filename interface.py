from search_Caroline_03090745 import Restaurants 
import pandas as pd

csv_path = "final.csv"
info = pd.read_csv(csv_path, header = 0, index_col = 0)
restaurants = Restaurants(info)

#x = list(set(["apple", "apple", "banan", "cherry"]))
#x.sort()
#print(x)

all_cuisines = list(set(info["cuisine"].tolist()))
all_cuisines.sort()
#print(len(all_cuisines)) -- 55
zip_codes = set(info["zip_code"].tolist())
zip_codes = [str(i) for i in zip_codes]
zip_codes.sort()


def area_search():
    while True:
        print("Which area do you want to search for?")
        print("Please enter a Chicago zip code.")
        str2 = input("You can enter one of the following: " + "; ".join(zip_codes) + "\n")
        if str2 == "quit":
            break
        elif str2 not in zip_codes:
            print("Please enter a valid zip code of Chicago.")
        else:
            returns = restaurants.single_return(None, int(str2))
            print("Number of restaurants in " + str2 + ":")
            print(returns[0])
            print("Ratings of different cuisines in " + str2 + ":")
            print(returns[1])
            print("Average prices of different cuisines in " + str2 + ":")
            print(returns[2])
            print("Do you want to search another area?")
            str3 = input("Enter 'N' to quit and any other thing to continue.\n")
            if str3 == "N":
                break


def cuisine_search():
    while True:
        print("Which cuisine do you want to search for?")
        print("Please enter a cuisine type.")

        str2 = input("You can enter one of the following:\n" + "; ".join(all_cuisines) + "\n")
        if str2 == "quit":
            break
        elif str2 not in all_cuisines:
            print("Please enter a valid cuisine type.")
        else:
            returns = restaurants.single_return(str2, None)
            print("Number of restaurants with " + str2 + " cuisine:")
            print(returns[0])
            print("Ratings of different areas under " + str2 + " cuisine:")
            print(returns[1])
            print("Average prices of different areas under " + str2 + " cuisine:")
            print(returns[2]) 
            print("Do you want to search another cuisine type?")
            str3 = input("Enter 'N' to quit and any other thing to continue.\n")
            if str3 == "N" or str3 == "quit":
                break


def double_helper_area(cuisine):
    while True:
        print("Which area do you want to search for?")
        print("Please enter a Chicago zip code.")
        str2 = input("You can enter one of the following: " + "; ".join(zip_codes) + "\n")
        if str2 == "quit":
            break
        elif str2 not in zip_codes:
            print("Please enter a valid zip code of Chicago.")
        else:
            returns = restaurants.double_return(cuisine, int(str2))
            print("Number of restaurants with " + cuisine + "cuisine in " + str2 + ":")
            print(returns[0])
            print("Average price of restaurants with " + cuisine + "cuisine in " + str2 + ":")
            print(returns[1])
            print("Average rating of restaurants with " + cuisine + "cuisine in " + str2 + ":")
            print(returns[2])
            print("Do you want to search another pair of cuisine type and area?")
            str3 = input("Enter 'N' to quit and any other thing to continue.\n")
            if str3 == "N" or str3 == "quit":
                break
            else:
                double_search()
            break


def double_search():
    while True:
        print("Which cuisine do you want to search for?")
        print("Please enter a cuisine type.")

        str2 = input("You can enter one of the following:\n" + "; ".join(all_cuisines) + "\n")
        if str2 == "quit":
            break
        elif str2 not in all_cuisines:
            print("Please enter a valid cuisine type.")
        else:
            double_helper_area(str2)
            break


print("Seeking to open a restaurant in Chicago but dishearted by the lack of information?")
print("Welcome to Foodies' restraunt assistant bot.")
print("Enter 'quit' at any time to quit.")

while True:
    print("What do you have in mind right now?")
    str1 = input("A. An area    B. A cuisine type    C.Both an area and a cuisine type\n")
    if str1 == "A":
        area_search()
        break


    elif str1 == "B":
        cuisine_search()
        break

    elif str1 == "C":
        double_search()
        break

    elif str1 == "quit":
        break

    else:
        print("Please enter either A or B or C.")
