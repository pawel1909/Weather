from objects.current import NowWeather
import pyowm

w = NowWeather()
print(w.currentWeather().to_dict())