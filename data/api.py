# import modułu API
from pyowm import OWM
from pyowm.utils.config import get_default_config
# Pobranie danych z pliku w folderze KEYS TODO zrobić coś, zeby dane były gdzieś indziej?
import os
filename = os.path.join('/home/pi/Keys', 'owm.txt')

API_KEY = ""

lon, lat = 0, 0
with open(filename) as f:
    file = f.read()

file = file.split(',')
API_KEY = file[0].strip()
lat = float(file[1].strip())

lon = float(file[2].strip())

config_dict = get_default_config()
config_dict["language"] = 'pl'

owm = OWM(API_KEY)
mgr = owm.weather_manager()