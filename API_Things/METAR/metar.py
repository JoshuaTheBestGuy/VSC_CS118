"""
This program will read the METAR from a user inputed airport.
Author: Joshua Hendrickson
"""

from json import load, dump#, loads
from urllib.request import urlopen
#from math import cos, sin

finished = False

def get_content(url:str) -> dict:
    """ Get some info from the web """
    try:
        with urlopen(url) as file:
            return load(file)
    except OSError as err:
        print(f"Error: {err}")
        return {}

while finished == False:
    if finished == False:
        airport = input("Please enter the airport you want to check: ")
        data = get_content(f"https://aviationweather.gov/api/data/metar?ids={airport}&format=json")
    if data == []:
        print(f"Your airport choice of {airport} is invalid, or does not have a METAR. Please select a new airport.")
    else:
        finished = True
        #print(data)
        break

with open ("API_Things/METAR/result.json", "w") as file:
    dump(data, file)

for p in data:
    raw_metar = p.get("rawOb")
    wind_speed = p.get("wspd")
    wind_gusts = p.get("wgst")
    wind_direction = p.get("wdir")
print(f"\nThe RAW metar is {raw_metar}.\nWinds are '{wind_direction}°' at '{wind_speed}' knots, with gusts of '{wind_gusts}' knots.")






# https://beeware.org/