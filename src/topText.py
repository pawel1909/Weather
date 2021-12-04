import sys
import os
icodir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'icons')
fontdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')

func = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'Fun')

dat = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'Dates')

if os.path.exists(dat):
    sys.path.append(dat)

if os.path.exists(func):
    sys.path.append(func)

from functions.language import *
# import świąt, naprawdę nie wiem jak zrobić i zainicjować je łatwiej :/
from Daty.swieta import listaSwiat_Styczen, listaSwiat_Luty, listaSwiat_Marzec, listaSwiat_Kwiecien, listaSwiat_Maj, listaSwiat_Czerwiec, listaSwiat_Lipiec, listaSwiat_Sierpien, listaSwiat_Wrzesień, listaSwiat_Pazdziernik, listaSwiat_Listopad, listaSwiat_Grudzien

from PIL import Image,ImageDraw,ImageFont
# from app import currentWeather
import datetime
data = datetime.datetime.now()
currentYear = int(data.strftime("%Y"))
currentMonth = int(data.strftime("%m"))
currentDay = int(data.strftime("%d"))

def currentHoliday(month, day):

    try:
        if month == 1:
            holiday = listaSwiat_Styczen[day]
        elif month == 2:
            holiday = listaSwiat_Luty[day]
        elif month == 3:
            holiday = listaSwiat_Marzec[day]
        elif month == 4:
            holiday = listaSwiat_Kwiecien[day]
        elif month == 5:
            holiday = listaSwiat_Maj[day]
        elif month == 6:
            holiday = listaSwiat_Czerwiec[day]
        elif month == 7:
            holiday = listaSwiat_Lipiec[day]
        elif month == 8:
            holiday = listaSwiat_Sierpien[day]
        elif month == 9:
            holiday = listaSwiat_Wrzesień[day]
        elif month == 10:
            holiday = listaSwiat_Pazdziernik[day]
        elif month == 11:
            holiday = listaSwiat_Listopad[day]
        elif month == 12:
            holiday = listaSwiat_Grudzien[day]
        else:
            return KeyError()
    except KeyError:
        holiday = f"Dargowo {currentYear}"
    
    return holiday

def topImg(y = 60):
    """
    zwraca: Wypełniony danymi, pobranymi z API
            Zwraca miejscowość, gdy nie ma świąt i nazwe święta, gdy jakieś się znajdzie
    """
    roboto36 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 36)
    # Nazwane inaczej ze względu na testowanie czcionki
    holiday_Font = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 36)
    width = 800
    height = y

    topBox = Image.new('1', (width, height), 255)

    draw = ImageDraw.Draw(topBox)

    text = currentHoliday(currentMonth, currentDay)

    if text == f"Dargowo {currentYear}":
        x, y1 = draw.textsize(text, font = roboto36)

        blackBox = Image.new('1', (int((x * 2)), (y1 + 6)), 0)
        dr = ImageDraw.Draw(blackBox)
        dr.text(((x / 2), 3), text, font = roboto36, fill = 1)
        topBox.paste(blackBox, (int((width - 2 * x) / 2), int((height - y1) / 2)))
    else:
        x, y1 = draw.textsize(text, font = holiday_Font)
        x1 = 1.2 * x
        blackBox = Image.new('1', (int((x1)), (y1 + 6)), 0)
        dr = ImageDraw.Draw(blackBox)
        dr.text((int((x1 - x) / 2), 3), text, font = holiday_Font, fill = 1)
        topBox.paste(blackBox, (int((width - x1) / 2), int((height - y1) / 2)))
        

    # topBox.paste(blackBox, (int((width - 2 * x) / 2), int((height - y) / 2)))




    return topBox



if __name__ == "__main__":
    hol = currentHoliday(currentMonth, currentDay)
    print(hol)
    print(currentDay)

    
### END OF FILE ###