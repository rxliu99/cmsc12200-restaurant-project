********************************** Project Documentation ********************************

Introduction:
        This project is carried out in fulfillment of the course requirement for 
        CMSC 12200 (Computer Science with Applications II) at the University of Chicago.
        The goal of this project is to offer future restaurant-owners in Chicago 
        1) information about the current restaurants in the area or cuisine of interest and
        2) information about the price of current restaurants.

Files:
        link_crawler.py         -- Crawler that obtains the url to individual restaurants
                                   in Chicago from Yelp

        restaurant_crawler.py   -- Crawler that obtains the restaurant name, zipcode, price, 
                                   cuisine, number of reviews, and average rating from Yelp

        housing_crawler.py      -- Crawler that obtains the average rent and average income
                                   of a Chicago zipcode from RENTCafé

        regression.py           -- Conduct multiple linear regression of the variables average 
                                   rent, average income, and average restaurant price

        manage.py               -- 

        interface.py            -- Text-based user interface implementation

        README.txt              -- This file


The project can be divided into 2 steps, both of which can be ran by the code provided in this folder.

Step 1 - Data Crawling:

        For user convenience, we saved links.txt (returned by line 22 in in scrape_data in manage.py), 
        info.csv (returned by line 30 in scrape_data in manage.py) and final.csv (returned by line 47 
        in manage.py) from our latest run. We strongly suggest the user directly move forward to step 2,
        where the interface automatically takes in pre-saved final.csv to return recommendations.

        To produce a new final.csv, you may call scrape_data in manage.py. The process involving visiting 
        a large amount of links and may more than 30 minutes to complete. The csv returned by this function
        depends on the link returned by Yelp, so the new final.csv might be different in lengths and/or 
        content as compared to the old final.csv. Notice that the outputs of this function will overwrite
        the default csv, so you may prefer to rename final.csv and info.csv if you wish to retain these 
        files for future reference. 

Step 2 - Interactions:

        After obtaining csv by running manage.py (alternatively, the user can use final.csv saved 
        in this folder), the user can enter text-based interface by running $ ipython3 interface.py
        (different command may apply depending on the version of python installed on your machine).

        The user can then select input based on idea in mind and the set of information they wish to see: 
   
        User input                 | Outputs
        -----------------------------------------------------------------------
        a. A Chicago zipcode       | 1. Number of restaurants in the zipcode
                                   | 2. Average Rating of different cuisines in the zipcode
                                   | 3. Average price of different cuisines in the zipcode
                                   | 4. The optimal restaurant price obtained by the regression model
                                             
        b. A cuisine               | 1. Number of restaurants of the cuisine
                                   | 2. Average rating of the cuisine in different zipcodes
                                   | 3. Average price of the cuisine in different zipcodes

        c. A zipcode and a cuisine | 1. Number of restaurants of the cuisine in the zipcode
                                   | 2. Average rating of the cuisine in the zipcode
                                   | 3. Average price of the cuisine in the zipcode

        d. "Outliers"              | 1. The zipcodes whose average restaurant prices are the outliers
                                   |    in the regression model
                                   | 2. The average restaurant price of each of the zipcodes
                                   | 3. The optimal restaurant price according to the regression model
        
        e. "Graph"                 | The 3D graph containing the scatter plot of the zipcodes and a plane
                                   | of the best-fit restaurant prices

Contributors:
        Julie Fan
        Caroline Jiang
        Michelle Liu
        Laurinda Zhang
