*****************Project roadmap[FOR REFERENCE]*****************

*Task1* [Done] Caroline links crawler - 240 links saved in chicago_links.py

*Task2* [Almost done] Laurinda restaurant info crawler - saved in info_0306.csv

        On a specific restaurant page, find the following:
        1. name
        2. zip_code
        3. price_range (some None)
        4. cuisine
        5. num_review
        6. rating (avg)

        Problems to solve:
        1. Sometimes cannot get 240 exact links - use the saved 240 links for now
        2. cralwer info sometime gives None tag; only 185/240

*Task3* [Done] Julie Rent crawler - crawler_housing_Edits2.py

*Task4* [Done] Final csv - final.csv

        1. merge csv from task 2 and 3 on zip_code 
        2. include 4 cols: zip_code, restaurant avg price, income, avg rent

*Task5* [Done] Michelle Multiple Linear Regression + Plot - regression_03120306.py

*Task6* [Progress] Text-based interface - interface.py



Outlier: give special rec on places with less restaurant
if select a zipcode, it's better to open a specific cuisine here


***************Project Documentation [FOR SUBMISSION]********************
Introduction:
        This project is carried out in fulfillment of the course requirement for 
        CMSC 12200 (Computer Science with Applications II) at the University of Chicago.
        The goal of this project is to offer future restaurant-owners in Chicago 
        1) information about the current restaurants in the area or cuisine of interest and
        2) information about the price of current restaurants.

Files:
        links_crawler.py        -- Crawler that obtains the url to individual restaurants
                                   in Chicago from Yelp
        restaurant_crawler.py   -- Crawler that obtains the price, rating, cuisine and
                                   address of restaurants in Chicago from Yelp
        housing_crawler.py      -- Crawler that obtains the average rent and average income
                                   of a Chicago zipcode from RENTCafé
        regression.py           -- Multiple linear regression of the variables average rent, 
                                   average income, and average restaurant price
        manage.py               -- 
        interface.py            -- Text-based user interface implementation
        README.txt              -- This file

Interactions:
        (1) The user chooses the set of information they wish to see: general information and
            price information.
     
        (2) General information
        User input                 | Outputs
        -----------------------------------------------------------------------
        a. A Chicago zipcode       | 1. Number of restaurants in the zipcode
                                   | 2. Average Rating of different cuisines in the zipcode
                                   | 3. Average price of different cuisines in the zipcode
                                             
        b. A cuisine               | 1. Number of restaurants of the cuisine
                                   | 2. Average rating of the cuisine in different zipcodes
                                   | 3. Average price of the cuisine in different zipcodes

        c. A zipcode and a cuisine | 1. Number of restaurants of the cuisine in the zipcode
                                   | 2. Average rating of the cuisine in the zipcode
                                   | 3. Average price of the cuisine in the zipcode

        (3) Price information
        User input                 | Outputs
        -----------------------------------------------------------------------
        a. A Chicago zipcode       | The optimal restaurant price obtained by the regression model
        
        b. "Outliers"              | 1. The zipcodes whose average restaurant prices are the outliers
                                   |    in the regression model
                                   | 2. The average restaurant price of each of the zipcodes
                                   | 3. The optimal restaurant price according to the regression model
        
        c. "Graph"                 | The 3D graph containing the scatter plot of the zipcodes and a plane
                                   | of the best-fit restaurant prices

Contributers:
        Julie Fan
        Caroline Jiang
        Michelle Liu
        Laurinda Zhang
