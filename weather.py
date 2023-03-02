import requests 
import os

def getNewWeather ( lat, lon ) :

    url = "https://weatherapi-com.p.rapidapi.com/history.json"

    querystring = {"q":"Austin","dt":"2023-02-26","lang":"en"}

    # Get the Rapid API KEY
    x_rapidapi_key = os.getenv('X_RAPIDAPI_KEY')
    print(f"The API Key is: {x_rapidapi_key}")

    headers = {
        "X-RapidAPI-Key": str(x_rapidapi_key),
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)

    return response.text

def getWeather( lat, lon ):
    # Replace the latitude and longitude with the location you want to get weather data for 

    # URL for the National Weather Service API 
    url = f'https://api.weather.gov/points/{lat},{lon}' 

    # Make a request to the API to get the forecast URL for the location 
    response = requests.get(url) 
    json = response.json() 
    forecast_url = json['properties']['forecast'] 

    # Make a request to the API to get the current weather data for the location 

    response = requests.get(forecast_url) 
    json = response.json()
    current_conditions = json['properties']['periods'][0]['detailedForecast'] 

    return current_conditions