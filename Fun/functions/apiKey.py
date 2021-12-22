# Moduł pobierający dane z pliku, zawierającego apiKey,
# zawiera zmienną mgr, która zostaje użyta w obiektach pogody (teraz, weatherobj)
from pyowm import OWM
from pyowm.utils.config import get_default_config
import sys
import os


filename = os.path.join('/home/pi/Keys', 'owm.txt')

API_KEY = ""
with open(filename) as f:
    API_KEY = f.read()

config_dict = get_default_config()
config_dict["language "] = 'pl'

owm = OWM(API_KEY)
mgr = owm.weather_manager()
### END OF FILE ###