import os
icodir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'icons')

from PIL import Image, ImageDraw

from data.icons import icons
from objects.api import Weather_obj
from data.date import HOUR
from data.debug import DEBUG
from data.fonts import ROBOTO9, ROBOTO16, ROBOTO18, ROBOTO14, ROBOTO12


def partImage(currentWeather: Weather_obj):
    """boczne obrazy

    Args:
        currentWeather (Weather_obj): _description_
    """

    WIDTH = 155
    HEIGHT = 250

    day = str(currentWeather.getDate()["day"][1])
    dayNr = currentWeather.getDate()["dayNr"]
    month = currentWeather.getDate()["month"][1]
    c_month = f"{dayNr} {month}"
    temp = currentWeather.getTemperature("day" if int(HOUR) > 8 and int(HOUR) < 22 else "night")
    minMax = currentWeather.getMinMaxTemp()
    humidity = currentWeather.getHumidity()
    pressure = currentWeather.getPressure()
    windSpeed = currentWeather.getWindSpeed()
    sunrise = currentWeather.getSunrise()
    sunset = currentWeather.getSunset()
    icon = currentWeather.getIconID()
    status = currentWeather.getDetailedStatus()


    # get icon and size
    try:
        ico = icons[icon]
    except:
        ico = "tornado.png"
    
    try:
        weatherImg = Image.open(os.path.join(icodir, ico))
    except:
        ico = "tornado.png"
        weatherImg = Image.open(os.path.join(icodir, ico))

    ico_w, ico_h = weatherImg.size
    icon_x = int((WIDTH - ico_w) / 2)

    # Create image
    img = Image.new('1', (WIDTH, HEIGHT), 255)
    draw = ImageDraw.Draw(img)

    # Get size of elements
    c_month_x, c_month_y = draw.textsize(c_month, font = ROBOTO18)
    c_month_x = int(WIDTH - c_month_x) / 2
    day_x, day_y = draw.textsize(day, font = ROBOTO18)
    day_x = int(WIDTH - day_x) / 2
    temp_x, temp_y = draw.textsize(minMax, font = ROBOTO18)
    temp_x = int(WIDTH - temp_x) / 2
    status_x, status_y = draw.textsize(status, font = ROBOTO14)
    temp = status_x
    status_x = int(WIDTH - status_x) / 2
    humidity_x, humidity_y = draw.textsize(humidity, font = ROBOTO16)
    humidity_x = int(WIDTH - humidity_x) / 2
    pressure_x, pressure_y = draw.textsize(pressure, font = ROBOTO16)
    pressure_x = int(WIDTH - pressure_x) / 2
    wind_x, wind_y = draw.textsize(windSpeed, font = ROBOTO16)
    wind_x = int(WIDTH - wind_x) / 2
    sunrise_x, sunrise_y = draw.textsize(sunrise, font = ROBOTO9)
    sunrise_x = int(WIDTH - sunrise_x) / 2
    sunset_x, sunset_y = draw.textsize(sunset, font = ROBOTO9)
    sunset_x = int(WIDTH - sunset_x) / 2
    y = 0
    
    # Draw text
    draw.text((day_x, 0), day, font = ROBOTO18)
    y += day_y
    draw.text((c_month_x, y), c_month, font = ROBOTO18)
    y += c_month_y + 10
    img.paste(weatherImg, (icon_x, y))
    y += ico_h + 10
    draw.text((temp_x, y), minMax, font = ROBOTO18)
    y += temp_y + 10
    if temp < WIDTH:
        draw.text((status_x, y), status, font = ROBOTO14)
        y += status_y
    else:
        status_x, status_y = draw.textsize(status, font = ROBOTO12)
        status_x = int(WIDTH - status_x) / 2
        draw.text((status_x, y), status, font = ROBOTO12)
        y += status_y
    draw.text((pressure_x, y), pressure, font = ROBOTO16)
    y += pressure_y + 10
    draw.text((wind_x, y), windSpeed, font = ROBOTO16)
    y += wind_y + 10
    draw.text((sunrise_x, y), sunset, font = ROBOTO9)
    y += sunrise_y + 10
    draw.text((sunset_x, y), sunrise, font = ROBOTO9)

    if DEBUG == 1:
        print("Pomyślnie utworzono część prawego obrazu")
        print(ico)

    return img

def rightImage(wList: list):
    WIDTH = 620
    HEIGHT = 250

    img = Image.new('1', (WIDTH, HEIGHT), 255)

    x = 0
    for w in wList:
        item = partImage(w)
        img.paste(item, (x, 0))
        x += 155
    if DEBUG == 1:
        print("Pomyślnie utworzono prawy obrazek")
    return img