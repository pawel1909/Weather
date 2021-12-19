import sys
import os
icodir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'icons')
fontdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')

func = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'Fun')

dat = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'Data')

if os.path.exists(dat):
    sys.path.append(dat)

if os.path.exists(func):
    sys.path.append(func)

from functions.language import *

from Listy import icondict

from PIL import Image,ImageDraw,ImageFont
# from app import currentWeather
import datetime



def leftImg(currentWeather, w = 180, h = 300):
    """
    zwraca: Wypełniony danymi, pobranymi z API, box
    """
    currentHour = datetime.datetime.now().strftime("%H")
    # Fonty użyte w boxie
    roboto36 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 36)
    roboto24 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 24)
    roboto18 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 18)
    roboto12 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 12)
    roboto9 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 9)

    # Rozmiary okienka
    width = w
    height = h

    # Dane
    date = datetime.datetime.now()
    ID ,month = [date.strftime("%d"), monthToPL(date.strftime("%b"))[1]]
    date_day, date_month = [dayToPL(date.strftime("%a"))[1], f"{ID} {month}"]
    temp = currentWeather.getTemperature("day" if int(currentHour) > 8 and int(currentHour) < 20 else "night")
    humidity = currentWeather.getHumidity()
    pressure = currentWeather.getPressure()
    windSpeed = currentWeather.getWindSpeed()
    sunrise = currentWeather.getSunrise()
    sunset = currentWeather.getSunset()
    icon = currentWeather.getIconID()
    status = currentWeather.getDetailedStatus()

    # chwilowe rozwiązanie zniknie po zrobieniu i zlinkowaniu wsyzstkich obrazów
    try:
        ico = icondict.icons[str(icon)]
    except:
        print("Błąd lewego obrazka")
        print(icon)
        ico = "tornado.png"
    weatherImg = Image.open(os.path.join(icodir, ico)) # zamienić 'wind.bmp' na icon
    
    

    # Stworzenie Kafelka
    img = Image.new('1', (width, height), 255)
    draw = ImageDraw.Draw(img)

    # zdobycie rozmiarów obrazka
    wi, he = weatherImg.size
    weather_img_x = int((width - wi) / 2)
    he += 10

    # Wklejenie elementów do głównego Kafelka


    


    month_x, month_y = draw.textsize(date_month, font = roboto24)
    day_x, day_y = draw.textsize(date_day, font = roboto24)
    temp_x, temp_y = draw.textsize(temp, font = roboto36)
    status_x, status_y = draw.textsize(status, font = roboto18)
    humidity_x, humidity_y = draw.textsize(humidity, font = roboto18)
    wind_x, wind_y = draw.textsize(windSpeed, font = roboto18)
    sunrise_x, sunrise_y = draw.textsize(sunrise, font = roboto12)
    sunset_x, sunset_y = draw.textsize(sunset, font = roboto12)

    img.paste(weatherImg, (weather_img_x, (sunrise_y + day_y + month_y + 10)))

    # Dodanie tekstu
    draw.text((int(width - day_x) / 2, 0), date_day, font = roboto24)
    draw.text((int(width - month_x) / 2, day_y), date_month, font = roboto24)
    draw.text((int((width - sunset_x) / 2), (day_y + month_y)), sunset, font = roboto12)
    draw.text((int((width - temp_x) / 2), (day_y + he + month_y + sunset_y)), temp, font = roboto36)
    if status_x < width:
        draw.text((int((width - status_x) / 2), (day_y + he + temp_y + 10 + month_y + sunset_y)), status, font = roboto18)
    else:
        status_x, status_y = draw.textsize(status, font = roboto12)
        draw.text((int((width - status_x) / 2), (day_y + he + temp_y + 10 + month_y + sunset_y)), status, font = roboto12)
    draw.text((int((width - humidity_x) / 2), (day_y + he + temp_y + status_y + 20 + month_y + sunset_y)), humidity, font = roboto18)
    draw.text((int((width - wind_x) / 2), (day_y + he + temp_y + status_y + humidity_y + 30 + month_y + sunset_y)), windSpeed, font = roboto18)
    draw.text((int((width - sunrise_x) / 2), (day_y + he + temp_y + status_y + humidity_y + wind_y + sunset_y + 40 + month_y)), sunrise, font = roboto12)
    

    return img





    
### END OF FILE ###