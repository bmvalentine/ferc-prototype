import requests 

def getNewWeather ( lat, lon ) :

    url = "https://weatherapi-com.p.rapidapi.com/history.json"

    querystring = {"q":"Austin","dt":"2023-02-26","lang":"en"}

    headers = {
        "X-RapidAPI-Key": "32c38eab7fmsh449308994ef5d9ep15e6bcjsn68f4becec7b6",
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