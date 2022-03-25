#region importy
import sys
import os
import datetime

func = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'Fun')

if os.path.exists(func):
    sys.path.append(func)

from functions.fun import *
from functions.language import *

#endregion importy

# zmiana języka na polski

# region DEBUG
DEBUG = 0

# endregion DEBUG


# endregion API_KEY

# region obiektPogody
class Weather_obj():
    def __init__(
        self, 
        date,
        temperature_day,
        temperature_night, 
        temp_min, 
        temp_max,
        humidity,
        pressure,
        wind_speed,
        status,
        detailed_status,
        sset_time,
        sunrise_time,
        icon_id):
            self.__date = date
            self.__temperatureDay = f"{temperature_day}{chr(176)}C"
            self.__temperatureNight = f"{temperature_night}{chr(176)}C"
            self.__minMaxTemp = f"{int(temp_min)}{chr(176)}C ~ {int(temp_max)}{chr(176)}C"
            self.__humidity = humidity
            self.__pressure = pressure
            self.__windSpeed = f"Wiatr: {wind_speed}m/s"
            self.__status = status
            self.__detailed_status = detailed_status
            self.__sunset = sset_time
            self.__sunrise = sunrise_time
            self.__icon_ID = icon_id
    
    def getDate(self):
        return {
            "str": date(self.__date),
            "day": dayToPL(rawData(self.__date).strftime("%a")),
            "dayNr": rawData(self.__date).strftime("%d"),
            "month": monthToPL(rawData(self.__date).strftime("%b")),
            "intDay": rawData(self.__date).strftime("%w"),
            "intMonth": rawData(self.__date).strftime("%m")
        }

    def getTemperature(self,timeOfTheDay = "day"):
        if timeOfTheDay == "day":
            return self.__temperatureDay
        else:
            return self.__temperatureNight

    def getMinMaxTemp(self):
        return self.__minMaxTemp
    
    def getStatus(self):
        return self.__status

    def getDetailedStatus(self):
        return (self.__detailed_status[0].upper() + self.__detailed_status[1:])

    def getHumidity(self):
        return f"Wilgotność: {self.__humidity}%"

    def getPressure(self):
        return f"Ciśnienie {self.__pressure}hPa"
    
    def getRawPressure(self):
        return self.__pressure

    def getWindSpeed(self):
        return self.__windSpeed

    def getSunrise(self):
        return f"Wschód słońca: {retTime(self.__sunrise)}"

    def getSunset(self):
        return f"Zachód słońca: {retTime(self.__sunset)}"

    def getIconID(self):
        return str(self.__icon_ID)


    def __str__(self):
        return f'Data: {self.getDate()},{self.getTemperature()},{self.getMinMaxTemp()},{self.getStatus()},{self.getDetailedStatus()},{self.getHumidity()},{self.getPressure()},{self.getWindSpeed()},{self.getSunrise()},{self.getSunset()},{self.getIconID()}'


# endregion obiektPogody

### END OF FILE ###