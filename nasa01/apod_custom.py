#!/usr/bin/env python3
import requests
from pprint import pprint as pp # part of the standard libray
# import webbrowser

## define some constants
NASAAPI = 'https://api.nasa.gov/planetary/apod?' # this is our API to call
MYKEY = 'api_key=QOYAXEu1mKJdcT1fmMaNdfvKqrdr8XFYdyWiIl0m' ## this is our api key

def main():
    """run-time code"""

    ## Part : Code Customization 01

    myDate = input("Date to retrieve APOD for (YYYY-MM-DD format): ")

    nasaapiobj = requests.get(NASAAPI + MYKEY + "&date=" + myDate) # call the webservice
    nasaread = nasaapiobj.json() # parse the JSON blob returned

    # pp(nasaread) # this is pretty print in action

    ## Part : Code Customization 02
    hdChoice = input("Do you wish to print the HD URL (y/n): ")

    if hdChoice == "y":
        print("")
        print(f"APOD HDURL: {nasaread['hdurl']}")   
    else:
        print("")
        print(f"HD URL not displayed")

    ## Part : Code Customization 03
    print("")
    print(f"APOD Date: {nasaread['date']}")           # Display the date 
    print(f"APOD Title: {nasaread['title']}")          # Display the title
    print("")
    print(f"APOD Explanation: {nasaread['explanation']}")    # Display the Explanation
    print("")

main()

