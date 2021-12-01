import os
import sys

obj = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'objects')

if os.path.exists(obj):
    sys.path.append(obj)

from weather_obj import Weather_obj
from teraz import NowWeather


weather = NowWeather()

#Lista obiektów pogodowych dotycząca 7 następnych dni
objList = []

currentWeather = Weather_obj(
    weather.currentWeather().ref_time,
    int(weather.currentWeather().temperature('celsius')['temp']),
    0,
    0,
    0,
    weather.currentWeather().humidity,
    weather.currentWeather().pressure['press'],
    weather.currentWeather().wind().get('speed'),
    weather.currentWeather().status,
    weather.currentWeather().detailed_status,
    weather.currentWeather().sset_time,
    weather.currentWeather().srise_time,
    weather.currentWeather().weather_icon_name
)

for item in weather:
    temp = item.temperature('celsius')
    obj = Weather_obj(
        item.ref_time,
        temp["day"],
        temp["night"],
        temp["min"],
        temp["max"],
        item.humidity,
        item.pressure['press'],
        item.wind().get('speed', None),
        item.status,
        item.detailed_status,
        item.sset_time,
        item.srise_time,
        item.weather_icon_name)
    objList.append(obj)


# for i in objList:
#     print(i)