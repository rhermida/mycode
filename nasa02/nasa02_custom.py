#!/usr/bin/env python3

import requests ## 3rd party URL lookup


def calculate_moon_miles(thisAsteroidDistance):

    lunarAsteroidDistance = float(thisAsteroidDistance) / 238900

    return lunarAsteroidDistance

## define the main function
def main():

    # Part 1 : Code Customization 01 
    print("<<< Going Through Part 1 >>>")

    startDate = input("Please input Start Date (YYYY-MM-DD format): ")
    endDate = input("Please input Start Date (YYYY-MM-DD format): ")

    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = 'start_date=' + startDate  ## start date for data
    enddate = '&end_date=' + endDate ## create a mechanism to utilize enddate
    mykey = '&api_key=QOYAXEu1mKJdcT1fmMaNdfvKqrdr8XFYdyWiIl0m' ## replace this with our API key

    neourl = neourl + startdate + enddate + mykey
    neojson = (requests.get(neourl)).json()

    print("")
    print("Date and Asteroid Count Summary for each date:")
    
    for date in neojson["near_earth_objects"].keys():
       testCount = len(neojson['near_earth_objects'][date])
       print(f"  Date: {date} - Asteroid Count: {testCount}") 

    # Part 2 : Code Customization 02

    print("")
    print("<<< Going Through Part 2 >>>")

    for date in neojson["near_earth_objects"].keys():
        print(f"Date: {date}")
        for dict in neojson["near_earth_objects"][date]:

            asteroidDistance = dict['close_approach_data'][0]['miss_distance']['miles']
            lunarAsteroidDistance = calculate_moon_miles(asteroidDistance)
            print(f"  Asteroid {dict['name']} - Distance (miles): {asteroidDistance} - Distance in Lunas : {lunarAsteroidDistance}" )

    # Part 3 : Code Customization 03

    # Short of time ... je suis desolee


## call main
if __name__ == "__main__":
    main()

