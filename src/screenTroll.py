#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
import os

fontdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
icodir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'icons')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import time
from random import choice
from PIL import Image,ImageDraw,ImageFont
import traceback
from main_image import leftImg
# pobranie obiektu pogodowego z dzisiejszą pogodą
from app import currentWeather
# pobranie listy pogody w następnych dniach
from daily_images import wList

logging.basicConfig(level=logging.DEBUG)

def trollingContainer(width = 800, height = 480):
    """ 
        Tutaj jest metoda, tworząca dziwne rzeczy xD

    """

    container = Image.new('1', (width, height), 255)

    shadowFont = ImageFont.truetype(os.path.join(fontdir, 'Shadow.ttf'), 24)
    roboto24 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 24)
    roboto36 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 36)
    roboto40 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 40)
    draw = ImageDraw.Draw(container)

    
    kto = choice(["pawel", "piter", "elwira"])

    img = Image.open(os.path.join(icodir, f'{kto}.bmp'))
    container.paste(img, (0, 0))
    x, y = img.size
    textBox_x = width - x
    textContainer = Image.new('1', (textBox_x, (height)), 255)
    textDraw = ImageDraw.Draw(textContainer)


    if kto == "piter":
        ### KROPKA i inne podstawowe
        kropka = u"\u2022"
        poszukiwany = "Poszukiwany!"
        poszukiwany_tekst = "Czy widziałeś tego człowieka?"
        cechySzczegolne = "Cechy szczególne."
        nagroda = "Nagroda 1000 Cebulionów"

        cecha1 = "Mętny wzrok"
        cecha2 = "Ciemne nienawistne oczy"
        cecha3 = "Woń alkoholu unosząca się dookoła"

        #wymiary
        x1, y1 = textDraw.textsize(poszukiwany, font = roboto40)
        x2, y2 = textDraw.textsize(poszukiwany_tekst, font = shadowFont)
        x3, y3 = textDraw.textsize(cechySzczegolne, font = roboto36)
        x4, y4 = textDraw.textsize(cecha1, font = shadowFont)
        x5, y5 = textDraw.textsize(cecha2, font = shadowFont)
        x6, y6 = textDraw.textsize(nagroda, font = roboto36)


        ### POSZUKIWANY ###
        textDraw.text((int((textBox_x - x1) / 2), 0), poszukiwany, font = roboto40, fill = 0)
        ### --------------- ###
        textDraw.line(((80, 44), ((textBox_x - 80), 44)), fill = 0, width = 4)
        ### Czy Widziałeś tego człowieka?
        textDraw.text((100, (y1 + 10)), poszukiwany_tekst, font = shadowFont, fill = 0)
        ### Cechy szczególne ###
        textDraw.text((int((textBox_x - x3) / 2), (y1 + y2 + 20)), cechySzczegolne, font = roboto36, fill = 0)
        ### --------------- ###
        textDraw.line(((80, (y1 + y2 + y3 + 24)), ((textBox_x - 80), (y1 + y2 + y3 + 24))), fill = 0, width = 3)
        ### pierwsza ###
        textDraw.text((100, (y1 + y2+ y3 + 30)), kropka, font = roboto40, fill = 0)
        textDraw.text((130, (y1 + y2+ y3 + 30)), cecha1, font = shadowFont, fill = 0)
        ### drUga ###
        textDraw.text((100, (y1 + y2+ y3 + y4 + 30)), kropka, font = roboto40, fill = 0)
        textDraw.text((130, (y1 + y2+ y3 + + y4 + 30)), cecha2, font = shadowFont, fill = 0)
        ### czecia ###
        textDraw.text((100, (y1 + y2+ y3 + y4 + y5 + 30)), kropka, font = roboto40, fill = 0)
        textDraw.text((130, (y1 + y2+ y3 + y4 + y5 + 30)), cecha3, font = shadowFont, fill = 0)
        # textDraw.text((0, 36), msg2, font = shadowFont, fill = 0)
        textDraw.text((100, 400), nagroda, font = roboto24, fill = 0)
    elif kto == "pawel":
        ### KROPKA i inne podstawowe
        kropka = u"\u2022"
        poszukiwany = "Poszukiwany!"
        poszukiwany_tekst = "Czy widziałeś tego człowieka?"
        cechySzczegolne = "Cechy szczególne."
        nagroda = "Nagroda 100 Cebulionów"

        cecha1 = "Siwe włosy"
        cecha2 = "Ciemne nienawistne oczy"
        cecha3 = "Codziennie coraz większy brzuch."

        #wymiary
        x1, y1 = textDraw.textsize(poszukiwany, font = roboto40)
        x2, y2 = textDraw.textsize(poszukiwany_tekst, font = shadowFont)
        x3, y3 = textDraw.textsize(cechySzczegolne, font = roboto36)
        x4, y4 = textDraw.textsize(cecha1, font = shadowFont)
        x5, y5 = textDraw.textsize(cecha2, font = shadowFont)
        x6, y6 = textDraw.textsize(nagroda, font = roboto36)


        ### POSZUKIWANY ###
        textDraw.text((int((textBox_x - x1) / 2), 0), poszukiwany, font = roboto40, fill = 0)
        ### --------------- ###
        textDraw.line(((80, 44), ((textBox_x - 80), 44)), fill = 0, width = 4)
        ### Czy Widziałeś tego człowieka?
        textDraw.text((100, (y1 + 10)), poszukiwany_tekst, font = shadowFont, fill = 0)
        ### Cechy szczególne ###
        textDraw.text((int((textBox_x - x3) / 2), (y1 + y2 + 20)), cechySzczegolne, font = roboto36, fill = 0)
        ### --------------- ###
        textDraw.line(((80, (y1 + y2 + y3 + 24)), ((textBox_x - 80), (y1 + y2 + y3 + 24))), fill = 0, width = 3)
        ### pierwsza ###
        textDraw.text((100, (y1 + y2+ y3 + 30)), kropka, font = roboto40, fill = 0)
        textDraw.text((130, (y1 + y2+ y3 + 30)), cecha1, font = shadowFont, fill = 0)
        ### drUga ###
        textDraw.text((100, (y1 + y2+ y3 + y4 + 30)), kropka, font = roboto40, fill = 0)
        textDraw.text((130, (y1 + y2+ y3 + + y4 + 30)), cecha2, font = shadowFont, fill = 0)
        ### czecia ###
        textDraw.text((100, (y1 + y2+ y3 + y4 + y5 + 30)), kropka, font = roboto40, fill = 0)
        textDraw.text((130, (y1 + y2+ y3 + y4 + y5 + 30)), cecha3, font = shadowFont, fill = 0)
        # textDraw.text((0, 36), msg2, font = shadowFont, fill = 0)
        textDraw.text((100, 400), nagroda, font = roboto24, fill = 0)
    elif kto == "elwira":
        ### KROPKA i inne podstawowe
        kropka = u"\u2022"
        poszukiwany = "Kącik poetycki"
        poszukiwany_tekst = "Znane i mniej znane cytaty"
        nagroda = "Nagroda 100 Cebulionów"

        cecha1 = "Czuję, że gdzieś idę"
        cecha2 = "A to działa wgl?"
        cecha3 = "Obyś sobie walnął mordą w twarz"

        #wymiary
        x1, y1 = textDraw.textsize(poszukiwany, font = roboto40)
        x2, y2 = textDraw.textsize(poszukiwany_tekst, font = shadowFont)
        x4, y4 = textDraw.textsize(cecha1, font = shadowFont)
        x5, y5 = textDraw.textsize(cecha2, font = shadowFont)
        x6, y6 = textDraw.textsize(nagroda, font = roboto36)


        ### POSZUKIWANY ###
        textDraw.text((int((textBox_x - x1) / 2), 0), poszukiwany, font = roboto40, fill = 0)
        ### --------------- ###
        textDraw.line(((60, 44), ((textBox_x - 60), 44)), fill = 0, width = 4)
        ### Czy Widziałeś tego człowieka?
        textDraw.text((80, (y1 + 10)), poszukiwany_tekst, font = shadowFont, fill = 0)
        ### pierwsza ###
        textDraw.text((100, (y1 + y2 + 30)), kropka, font = roboto40, fill = 0)
        textDraw.text((130, (y1 + y2 + 30)), cecha1, font = shadowFont, fill = 0)
        ### drUga
        textDraw.text((100, (y1 + y2 + y4 + 30)), kropka, font = roboto40, fill = 0)
        textDraw.text((130, (y1 + y2 + + y4 + 30)), cecha2, font = shadowFont, fill = 0)
        ### czecia
        textDraw.text((100, (y1 + y2 + y4 + y5 + 30)), kropka, font = roboto40, fill = 0)
        textDraw.text((130, (y1 + y2 + y4 + y5 + 30)), cecha3, font = shadowFont, fill = 0)

    
    

    container.paste(textContainer, (x, 0))

    return container

# moduł nieużywany w końcowej wersji ?
### END OF FILE ###