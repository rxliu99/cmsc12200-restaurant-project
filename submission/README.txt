********************************** Project Documentation ********************************

Introduction:
        This project is carried out in fulfillment of the course requirement for 
        CMSC 12200 (Computer Science with Applications II) at the University of Chicago.
        The goal of this project is to offer future restaurant-owners in Chicago 
        1) information about the current restaurants in the area or cuisine of interest and
        2) information about the price of current restaurants.


Description:
        This project aims to provide restaurant-owners information on various restaurants in Chicago 
        through obtaining average costs, rating, cuisine and address for restaurants. We also obtain 
        average rent per square foot for Chicago housings as well as average personal income at each 
        zipcode address. To achieve this, we crawl relevant data from Yelp and RENTCafé, and then we 
        calculate the average spendings across restaurants, average rent and average income for each 
        Chicago neighborhood. To obtain better understanding of elements such as different variable 
        correlations, distributions, and potential outliers, we fit a multiple linear regression model 
        on the response variable average restaurant price and two predictor variables average rent and 
        income. Additionally, we create a 3D graph to obtain scatterplot and best-fit restaurant prices, 
        as the regression model provides us the optimal restaurant price. 


Users:
        Users can choose either general or price information based on their preferences, and will be able
        to search information based on cuisine type or area, or both. 


Data Sources:
        Yelp - Data for individual restaurants with price, rating and address info
        RENTCafé - Data for Chicago housing with rent and zipcode info


Files:
        link_crawler.py         -- Crawler that obtains the url to individual restaurants
                                   in Chicago from Yelp

        restaurant_crawler.py   -- Crawler that obtains the restaurant name, zipcode, price, 
                                   cuisine, number of reviews, and average rating from Yelp

        housing_crawler.py      -- Crawler that obtains the average rent and average income
                                   of a Chicago zipcode (collected from info.csv) from RENTCafé

        manage.py               -- Run three crawlers to obtain desired csv and text files 
                                   for interaction use

        regression.py           -- Conduct multiple linear regression of the variables average 
                                   rent, average income, and average restaurant price

        search.py               -- Implement the search function of the software, namely mapping
                                   data retrived from Yelp.com and Rentcafe.com to inputs specified 
                                   by the user

        interface.py            -- Text-based user interface implementation

        final.csv               -- csv written by manage.py that includes restaurant name, 
                                   zipcode, price, cuisine, number of reviews, average rating,
                                   housing price, and median income

        info.csv                -- csv written by manage.py that includes restaurant name, 
                                   zipcode, price, cuisine, number of reviews, and average rating from Yelp

        links.txt               -- links return by link_crawler.py and written by manage.py

        README.txt              -- This file


<<<<<<< HEAD
The project can be divided into 2 steps, both of which can be ran by the code provided in this folder.

Step 1 - Data Crawling:
=======
***************Project Documentation [FOR SUBMISSION]********************

Introduction:
        This project is carried out in fulfillment of the course requirement for 
        CMSC 12200 (Computer Science with Applications II) at the University of Chicago.
        The goal of this project is to offer future restaurant-owners in Chicago 
        1) information about the current restaurants in the area or cuisine of interest and
        2) information about the price of current restaurants.

Description:
        This project aims to provide restaurant-owners information on various restaurants in Chicago 
        through obtaining average costs, rating, cuisine and address for restaurants. We also obtain 
        average rent per square foot for Chicago housings as well as average personal income at each 
        zipcode address. To achieve this, we crawl relevant data from Yelp and RENTCafé, and then we 
        calculate the average spendings across restaurants, average rent and average income for each 
        Chicago neighborhood. To obtain better understanding of elements such as different variable 
        correlations, distributions, and potential outliers, we fit a multiple linear regression model 
        on the response variable average restaurant price and two predictor variables average rent and 
        income. Additionally, we create a 3D graph to obtain scatterplot and best-fit restaurant prices, 
        as the regression model provides us the optimal restaurant price. 

Users:
        Users can choose either general or price information based on their preferences, and will be able
        to search information based on cuisine type or area, or both. 

Data Sources:
        Yelp - Data for individual restaurants with price, rating and address info
        RENTCafé - Data for Chicago housing with rent and zipcode info

Files:
        links_crawler.py        -- Crawler that obtains the url to individual restaurants
                                   in Chicago from Yelp
        restaurant_crawler.py   -- Crawler that obtains the price, rating, cuisine and
                                   address of restaurants in Chicago from Yelp
        housing_crawler.py      -- Crawler that obtains the average rent and average income
                                   of a Chicago zipcode from RENTCafé
        regression.py           -- Multiple linear regression of the variables average rent, 
                                   average income, and average restaurant price
        manage.py               -- File to scrape data and read df from final.csv
        interface.py            -- Text-based user interface implementation
        README.txt              -- This file
>>>>>>> 50cec6aa495890ce9f314e858676e5f27ba26318

        For user convenience, we saved links.txt, info.csv and final.csv (all returned by scrape_data 
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
        A. A Chicago zipcode       | 1. Number of restaurants in the zipcode
                                   | 2. Average Rating of different cuisines in the zipcode
                                   | 3. Average price of different cuisines in the zipcode
                                   | 4. The optimal restaurant price obtained by the regression model
                                             
        B. A cuisine               | 1. Number of restaurants of the cuisine
                                   | 2. Average rating of the cuisine in different zipcodes
                                   | 3. Average price of the cuisine in different zipcodes

        C. A zipcode and a cuisine | 1. Number of restaurants of the cuisine in the zipcode
                                   | 2. Average rating of the cuisine in the zipcode
                                   | 3. Average price of the cuisine in the zipcode

        D. "Outliers"              | 1. The zipcodes whose average restaurant prices are the outliers
                                   |    in the regression model
                                   | 2. The average restaurant price of each of the zipcodes
                                   | 3. The optimal restaurant price according to the regression model
                                   | 4. The suggested price range for opening potential restaurants
        
        E. "Graph"                 | The 3D graph containing the scatter plot of the zipcodes and a plane
                                   | of the best-fit restaurant prices

Contributors:
        Julie Fan
        Caroline Jiang
        Michelle Liu
        Laurinda Zhang
