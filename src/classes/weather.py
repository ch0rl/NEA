"""Base class for the weather functionality"""


# My functions
from ..helpers import *

# Builtins
import json
import re

# Not builtin
try:
    import requests
except ImportError as e:
    logException("Weather", e)
    print("Uninstalled package, try `pip install requests`")
    quit()


class Weather:
    LOCATION_RE = (
        r"^[a-zA-Z' ]+$|"  # City
        r"^-?[0-9.]+,-?[0-9.]+$|"  # Lat,long
        r"^[a-zA-Z]{2}\d{2} \d[a-zA-Z]{2}$|"  # Postcode
        r"^(\d{1,3}\.){3}\d{1,3}$"  # IP
    )

    def __init__(self):
        logInfo("Weather", "Weather started")
        self.last_output = None

    @staticmethod
    def form_nice_string(forecast: dict) -> str:
        """Forms 'nice' (printable) string from the forecast
        
        :param forecast: Raw forecast data from the API
        :return: A string representing the forecast
        """

        try:
            data = forecast["current"]
            location = forecast["location"]["name"]
            last_updated = data["last_updated"].split()
            # All units will be metric
            temp = data["temp_c"]
            condition = data["condition"]["text"]
            wind_speed = data["wind_kph"]
        except KeyError as e:
            logException("Weather", e)
            return None
        else:
            # All data fetched
            return (
                f"Weather in {location} at {last_updated[1]}\n"
                f"It is currently {temp} degrees, with wind speeds of {wind_speed}\n"
                f"The weather is generally {condition}\n"
            )
    
    def weather(self, location: str = None) -> str:
        """Get weather forecast at location, over `days`
        
        :param location: The location of the forecast, one of:
            - city, coords, postcode, IP
            if not provided, auto-ip will be used
        :return: Printable string of the forecast, None if error
        """

        # Check paramaters
        if location is None:
            logError("Weather", "Bad inputs", "No location provided, using IP")
            location = "auto:ip"
        elif not re.match(self.LOCATION_RE, location):
            logError("Weather", "Bad location", "Location does not fit regex (invalid), using IP")
            location = "auto:ip"
        
        # Retrieve key
        with open("settings/api-keys.json", 'r') as f:
            try:
                key = json.load(f)["Weather"]
            except KeyError as e:
                key = None
                logException("Weather", e)
        
        if key:
            # Get data
            try:
                resp = requests.get(
                    f"http://api.weatherapi.com/v1/current.json?key={key}&q={location}"
                )
            except requests.exceptions.ConnectionError as e:
                # Not connected
                logException("Weather", e)
                return None
            else:
                if resp.status_code == 200:
                    # 200 = all good
                    output = self.form_nice_string(resp.json())
                    self.last_output = output
                    return output
        else:
            logError("Weather", "No API key", "No API key found for weather API")
            return None

