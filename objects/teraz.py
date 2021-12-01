
from pyowm import OWM
import os
import sys

func = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'Fun')

if os.path.exists(func):
    sys.path.append(func)

from functions.fun import *

from functions.apiKey import mgr

class NowWeather():
    
    def __init__(self, lat = 53.965923, lon = 19.669524):
        self.one_call_now = mgr.one_call(lat, lon).forecast_daily
        self.__Current = mgr.one_call(lat, lon).current
        self.start = 0
        self.end = len(self.one_call_now)
        # self.__temperature = self.one_call_now.temperature('celsius')
        # self.__humidity = self.one_call_now.humidity
        # self.__pressure = self.one_call_now.pressure
        # self.__sunrise = self.one_call_now.sunrise_time()
        # self.__sunset = self.one_call_now.sset_time
        # self.__wind = self.one_call_now.wind()
    
    # region iteracja
    #Dodaje możliwość użycia pętli for na tym obiekcie (dosyć użyteczne)
    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start < self.end:
            return self.one_call_now[self.start]
        raise StopIteration
    #endregion
    
    def currentWeather(self):
       return self.__Current

print("Witaj w objekcie zapytania api")
