import FercCalcs
import weather as w
import json

lat = '30.27' 
lon = '-97.74'

print ( f"Getting weather for lat [{lat}] long [{lon}] ")

conditions = w.getWeather( lat, lon )
print (conditions)

conditions = w.getNewWeather( lat, lon )

print(conditions)
# print (conditions)

# json_obj = json.loads(conditions)

# location = json_obj["location"]
# forecast = json_obj["forecast"]

# forecast_json = json.loads( forecast )
#for f in  forecast_json["forecastday"] :
#    print( f )
#    print( f"Forecast: {f}")

# forecastday = json_obj["forecastday"]

# print( json_obj )
# print( forecast )

