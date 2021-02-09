#!/usr/bin/python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# Test Part of Warm Up Challange

for myFarm in farms:
    actualFarmName = str({myFarm['name']})

    if actualFarmName == "{'NE Farm'}":
        print(f"<<< Test (First Part): {myFarm['agriculture']} >>>")

# Trial Part of Warm Up Challenge

inputFarm = str(input("Please enter farm name: "))

for myFarm in farms:
    actualFarmName = str({myFarm['name']})

    if actualFarmName == "{'" + inputFarm + "'}":
        print(f"<<< Trial (Second Part): {myFarm['agriculture']} >>>")

# Challenge Part of Warm Up Challenge

inputFarm = str(input("Please enter farm name: "))

for myFarm in farms:
    actualFarmName = str({myFarm['name']})

   # Need to add a second loop to iterate to the items in agriculture and not print veggies (IF Statement)

