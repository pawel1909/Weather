import sys
import os
icodir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'icons')
fontdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')

listdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'Listy')
from PIL import Image,ImageDraw,ImageFont

dat = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'Data')

if os.path.exists(dat):
    sys.path.append(dat)

# from app import currentWeather
import datetime
from app import objList

from Listy import icondict

currentHour = datetime.datetime.now().strftime("%H")

def leftImg(currentWeather, w = 155, h = 250):
    """
    zwraca: Wypełniony danymi, pobranymi z API, box
    """

    # Fonty użyte w boxie
    roboto36 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 18)
    roboto18 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 16)
    roboto9 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 9)

    # wymiary
    width = w
    height = h
    const = 60

    # Dane
    date = currentWeather.getDate()
    temp = currentWeather.getTemperature("day" if int(currentHour) > 8 and int(currentHour) < 20 else "night")
    minMax = currentWeather.getMinMaxTemp()
    humidity = currentWeather.getHumidity()
    pressure = currentWeather.getPressure()
    windSpeed = currentWeather.getWindSpeed()
    sunrise = currentWeather.getSunrise()
    sunset = currentWeather.getSunset()
    icon = currentWeather.getIconID()
    status = currentWeather.getDetailedStatus()
    # chwilowe rozwiązanie zniknie po zrobieniu i zlinkowaniu wsyzstkich obrazów
    try:
        ico = icondict.icons[icon]
    except:
        ico = "tornado.png"
    weatherImg = Image.open(os.path.join(icodir, ico)) # zamienić 'wind.bmp' na icon
    

    # Stworzenie Kafelka
    img = Image.new('1', (width, height), 255)
    draw = ImageDraw.Draw(img)

    # zdobycie rozmiarów obrazka
    wi, he = weatherImg.size
    weather_img_x = int((width - wi) / 2)
    weather_img_y = he + 10

    # Dzień tygodnia
    day = date["day"][1]
    day_x, day_y = draw.textsize(day, font = roboto36)
    a , b = date["month"][0], date["dayNr"]
    month = f"{b} {a}"
    month_x, month_y = draw.textsize(month, font = roboto36)

    

    # Wklejenie elementów do głównego Kafelka

    temp_x, temp_y = draw.textsize(minMax, font = roboto36)
    status_x, status_y = draw.textsize(status, font = roboto18)
    humidity_x, humidity_y = draw.textsize(humidity, font = roboto18)
    wind_x, wind_y = draw.textsize(windSpeed, font = roboto18)
    sunrise_x, sunrise_y = draw.textsize(sunrise, font = roboto9)
    sunset_x, sunset_y = draw.textsize(sunset, font = roboto9)


    img.paste(weatherImg, (weather_img_x, (day_y + month_y + 10)))
    # Dodanie tekstu
    draw.text((int(width - day_x) / 2, 0), day, font = roboto36)
    draw.text(((int(width - month_x) / 2), (day_y)), month, font = roboto36)
    draw.text((int((width - temp_x) / 2), (he + day_y + month_y + 10)), minMax, font = roboto36)
    draw.text((int((width - status_x) / 2), (he + temp_y + day_y + month_y + 20)), status, font = roboto18)
    draw.text((int((width - humidity_x) / 2), (he + temp_y + status_y + day_y + month_y + 30)), humidity, font = roboto18)
    draw.text((int((width - wind_x) / 2), (he + temp_y + status_y + humidity_y + day_y + month_y + 40)), windSpeed, font = roboto18)
    draw.text((int((width - sunrise_x) / 2), (he + temp_y + status_y + humidity_y + wind_y + day_y + month_y + 50)), sunset, font = roboto9)
    draw.text((int((width - sunset_x) / 2), (he + temp_y + status_y + humidity_y + wind_y + sunrise_y + day_y + month_y + 60)), sunrise, font = roboto9)
    

    return img


l = objList

wList = []

for w in l:
    wList.append(leftImg(w))

wList = wList[:4]




    
### END OF FILE ###