Crawler code structure:

*Starting from https://www.yelp.com/

Searching conditions:
1. Put "Restaurants" into Find
2. Put "city_name" from cook_county_zips.csv into Near

Or, default search "Restaurants" and "Chicago"
then extract links to all restaurants
    1. how to pick out links to restaurants


**On a specific restaurant page, find the following:

1. zip_code
#yelp_lecolonial.htm line 398, search for 60611, "postalCode":"60611"

2. price range
#yelp_lecolonial.htm line 398, "priceRange":"$31-60"

3. cuisine
#yelp_lecolonial.htm line 398, roll down till, "servesCuisine":"Vietnamese"

4. rating
Need to calculate the mean of "reviewValue"
#yelp_lecolonial.htm line 398, "review":[{"author":"Munsanje M.","datePublished":\
        "2021-01-24","reviewRating":{"ratingValue":5},"description":"xxxxxx"}, {xxx}]

5. num of reviews
Need to find the length of dict val corresponding to the key "review"
#yelp_lecolonial.htm line 398, "review":[{"author":"Munsanje M.","datePublished":\
    "2021-01-24","reviewRating":{"ratingValue":5},"description":"xxxx"}, {review#2 etc.}]