from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict["language"] = 'pl'

api_key = "Your_Api_Key"
owm = OWM(api_key)
mgr = owm.weather_manager()