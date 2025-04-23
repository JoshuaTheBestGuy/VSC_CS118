"""
My Weather Forecast
"""

from urllib.request import urlopen
from json import load, dump

def get_content(url:str) -> dict:
    """ Get some info from the web """
    try:
        with urlopen(url) as file:
            return load(file)
    except OSError as err:
        print(f"Error: {err}")
        return {}

gps = get_content("https://ipinfo.io/json").get("loc").split(',')
latitude, longitude = gps

grid = get_content(f"https://api.weather.gov/points/{latitude},{longitude}")
gridID = grid.get("properties").get("gridId")
gridX = grid.get("properties").get("gridX")
gridY = grid.get("properties").get("gridY")

#with open ("grid.json", "w") as file:
#    dump(grid, file)

forecast = get_content(f"https://api.weather.gov/gridpoints/{gridID}/{gridX},{gridY}/forecast")
periods = forecast.get("properties").get("periods")

for p in periods:
    print(f"\n{p.get("name")}\n{p.get("detailedForecast")}\n")
