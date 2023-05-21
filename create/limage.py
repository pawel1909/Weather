import os
icodir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'icons')

from data.fonts import ROBOTO12, ROBOTO18, ROBOTO24, ROBOTO36
from PIL import Image, ImageDraw
from objects.api import Weather_obj

from fun.translate import dayToPL, monthToPL
from data.icons import icons
from data.date import HOUR
from data.debug import DEBUG

def leftImg(currentWeather: Weather_obj):
    """Kafelek główny. Lewa strona ekranu. Temperatura bieżąca.

    Args:
        currentWeather (Weather_obj): obiekt pogody
    """
    WIDTH = 180
    HEIGHT = 290
    day = str(currentWeather.getDate()["day"][1])
    dayNr = currentWeather.getDate()["dayNr"]
    month = currentWeather.getDate()["month"][1]
    temp = currentWeather.getTemperature("day" if HOUR > 8 and HOUR < 22 else "night")
    humidity = currentWeather.getHumidity()
    pressure = currentWeather.getPressure()
    windSpeed = currentWeather.getWindSpeed()
    sunrise = currentWeather.getSunrise()
    sunset = currentWeather.getSunset()
    icon = currentWeather.getIconID()
    status = currentWeather.getDetailedStatus()
    c_month = f"{dayNr} {month}"

    try:
        ico = icons[str(icon)]
    except:
        if (DEBUG == 1):
            print("Ikona w lewym obrazku nie została znaleziona")
            print(icon)
        icon = "tornado.png"
    
    # Create icon and get size
    try:
        weatherImg = Image.open(os.path.join(icodir, ico))
    except:
        weatherImg = Image.open(os.path.join(icodir, "tornado.png"))
    ico_w, ico_h = weatherImg.size
    icon_x = int((WIDTH - ico_w) / 2)

    # Create image for left side
    img = Image.new('1', (WIDTH, HEIGHT), 255)
    draw = ImageDraw.Draw(img)

    # Get size of elements
    c_month_x, c_month_y = draw.textsize(c_month, font = ROBOTO24)
    c_month_x = int(WIDTH - c_month_x) / 2
    day_x, day_y = draw.textsize(day, font = ROBOTO24)
    day_x = int(WIDTH - day_x) / 2
    temp_x, temp_y = draw.textsize(temp, font = ROBOTO36)
    temp_x = int(WIDTH - temp_x) / 2
    status_x, status_y = draw.textsize(status, font = ROBOTO18)
    status_x = int(WIDTH - status_x) / 2
    humidity_x, humidity_y = draw.textsize(humidity, font = ROBOTO18)
    humidity_x = int(WIDTH - humidity_x) / 2
    pressure_x, pressure_y = draw.textsize(pressure, font = ROBOTO18)
    pressure_x = int(WIDTH - pressure_x) / 2
    wind_x, wind_y = draw.textsize(windSpeed, font = ROBOTO18)
    wind_x = int(WIDTH - wind_x) / 2
    sunrise_x, sunrise_y = draw.textsize(sunrise, font = ROBOTO12)
    sunrise_x = int(WIDTH - sunrise_x) / 2
    sunset_x, sunset_y = draw.textsize(sunset, font = ROBOTO12)
    sunset_x = int(WIDTH - sunset_x) / 2

    y = 0

    # Draw image
    draw.text((day_x, y), day, font = ROBOTO24)
    y += day_y
    draw.text((c_month_x, y), c_month, font = ROBOTO24)
    y += c_month_y
    draw.text((sunset_x, y), sunset, font = ROBOTO12)
    y += sunset_y
    img.paste(weatherImg, (icon_x, y))
    y += ico_h
    draw.text((temp_x, y), temp, font = ROBOTO36)
    y += temp_y
    if status_x < WIDTH:
        draw.text((status_x, y), status, font = ROBOTO18)
        y += status_y + 10
    else:
        status_x, status_y = draw.textsize(status, font = ROBOTO12)
        status_x = int(WIDTH - status_x) / 2
        draw.text((status_x, y), status, font = ROBOTO12)
        y += status_y + 10
    draw.text((pressure_x, y), pressure, font = ROBOTO18)
    y += pressure_y + 10
    draw.text((wind_x, y), windSpeed, font = ROBOTO18)
    y += wind_y + 10
    draw.text((sunrise_x, y), sunrise, font = ROBOTO12)

    if DEBUG == 1:
        print("Główny obraz utowrzony")
        print()
    return img

