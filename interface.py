from Search_Caroline_03090745 import Restaurants 
import pandas as pd

csv_path = "info.csv"
info = pd.read_csv(csv_path, header = 0, index_col = 0)
restaurants = Restaurants(info)

print("Seeking to open a restaurant in Chicago but dishearted by the lack of information?")
print("Welcome to Foodies' restraunt assistant bot.")
###not implemented yet
print("Enter 'quit' at any time to quit.")
while True:
    print("What do you have in mind right now?")
    str = input("A. An area    B. A cuisine type    C.Both an area and a cuisine type\n")
    if str == "A":
        while True:
            print("Which area do you want to search for?")
            str2 = input("Please enter a Chicago zip code:\n")
            if str2.isdigit() == False: 
                print("Please enter a valid zip code of Chicago.")
            elif int(str2) not in info["zip_code"].tolist():
                print("Please enter a valid zip code of Chicago.")
            else:
                returns = restaurants.single_return(None, int(str2))
                print("Number of restaurants in " + str2 + ":")
                print(returns[0])
                print("Ratings of different cuisines in " + str2 + ":")
                print(returns[1])
                print("Average prices of different cuisines in " + str2 + ":")
                print(returns[2])
                str3 = input("Do you want to search another area? Y/N\n")
                if str3 == "N":
                    break
        break

    elif str == "B":
        while True:
            print("Which cuisine do you want to search for?")
            print("Please enter a cuisine type:")
            all_types = "; ".join(set(info["cuisine"].tolist()))
            ###change to case insensitive
            ###breakfast and brunch
            str2 = input("You can enter one of the following:\n" + all_types + "\n")
            if str2 not in info["cuisine"].tolist():
                print("Please enter a valid cuisine type.")
            else:
                returns = restaurants.single_return(str2, None)
                print("Number of restaurants with " + str2 + " cuisine:")
                print(returns[0])
                print("Ratings of different areas under " + str2 + " cuisine:")
                print(returns[1])
                print("Average prices of different areas under " + str2 + " cuisine:")
                print(returns[2]) 
                str3 = input("Do you want to search another cuisine type? Y/N\n")
                if str3 == "N":
                    break
        break

    elif str == "C":
        while True:
            print("Which cuisine do you want to search for?")
            print("Please enter a cuisine type:")
            all_types = "; ".join(set(info["cuisine"].tolist()))
            ###change to case insensitive
            ###breakfast and brunch
            str2 = input("You can enter one of the following:\n" + all_types + "\n")
            if str2 not in info["cuisine"].tolist():
                print("Please enter a valid cuisine type.")
                pass
            ###Not workig
            print("Which area do you want to search for?")
            str3 = input("Please enter a Chicago zip code:")
            if int(str3) not in info["zip_code"].tolist():
                print("Please enter a valid zip code of Chicago.")
                pass
            returns = restaurants.double_return(str2, str3)
            print("Number of restaurants with " + str2 + "cuisine in " + str3 + ":")
            print(returns[0])
            print("Average price of restaurants with " + str2 + "cuisine in " + str3 + ":")
            print(returns[1])
            print("Average rating of restaurants with " + str2 + "cuisine in " + str3 + ":")
            print(returns[2])
            ###When nothing is returned
            str4 = ("Do you want to search another pair of cuisine type and area? Y/N")
            if str4 == "N":
                break
        break

    else:
        print("Please enter either A or B.")

