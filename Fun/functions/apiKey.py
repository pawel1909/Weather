from pyowm import OWM
from pyowm.utils.config import get_default_config


filename = os.path.join('/home/pi/Keys', 'owm.txt')

API_KEY = ""
with open(filename) as f:
    API_KEY = f.read()

config_dict = get_default_config()
config_dict["language"] = 'pl'

owm = OWM(API_KEY)
mgr = owm.weather_manager()