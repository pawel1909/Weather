import sys
import os
icodir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'icons')
fontdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')

func = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'Fun')

if os.path.exists(func):
    sys.path.append(func)

from functions.language import *

from PIL import Image,ImageDraw,ImageFont
# from app import currentWeather
import datetime

currentYear = datetime.datetime.now().strftime("%Y")

def topImg(y):
    """
    zwraca: Wypełniony danymi, pobranymi z API, box
    """
    roboto36 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 36)
    width = 800
    height = y

    topBox = Image.new('1', (width, height), 255)

    draw = ImageDraw.Draw(topBox)

    text = f"Dargowo {currentYear}"
    x, y = draw.textsize(text, font = roboto36)

    blackBox = Image.new('1', (int((2 * x)), (y + 6)), 0)
    dr = ImageDraw.Draw(blackBox)
    dr.text(((x / 2), 0), text, font = roboto36, fill = 1)

    topBox.paste(blackBox, (int((width - 2 * x) / 2), int((height - y) / 2)))




    return topBox





    
