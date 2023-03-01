import FercCalcs
import weather as w

lat = '30.27' 
lon = '-97.74'

print ( f"Getting weather for lat [{lat}] long [{lon}] ")

conditions = w.getWeather( lat, lon )
print (conditions)

conditions = w.getNewWeather( lat, lon )

print (conditions)