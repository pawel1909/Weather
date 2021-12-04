import sys
import os

fontdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')

func = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'Fun')

if os.path.exists(func):
    sys.path.append(func)

from functions.language import *

from PIL import Image,ImageDraw,ImageFont
# from app import currentWeather
import datetime

currentHour = datetime.datetime.now().strftime("%H")

def footer(w = 600, h = 100):

    """
    # Tak jakby stopka

    zwraca: Wypełniony danymi, pobranymi z API, box
    """

    # Fonty użyte w boxie
    roboto36 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 36)
    roboto24 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 24)
    roboto18 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 18)
    roboto12 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 12)
    shadowFont = ImageFont.truetype(os.path.join(fontdir, 'Shadow.ttf'), 36)

    width = w
    height = h

    foot = Image.new('1', (width, height), 255)

    write = ImageDraw.Draw(foot)

    write.line((0, 0, 600, 0), fill = 0)
    write.line((0, 150, 0, 0), fill = 0)

    cytat = "Nigdy nie cofaj się wstecz!"
    cytat2 = "Nie wiem jeszcze"
    x, y = write.textsize(cytat, font = shadowFont)

    write.text((int((width - x) / 2), (int((height - y) / 2))), cytat, font = shadowFont, fill = 0)


    return foot





    
### END OF FILE ###