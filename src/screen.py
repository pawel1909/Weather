#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
import os
import datetime
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
icodir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'icons')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from main_image import leftImg
# pobranie obiektu pogodowego z dzisiejszą pogodą
from app import currentWeather
# pobranie listy pogody w następnych dniach
from daily_images import wList
# Pobranie topBox
from topText import topImg
# STÓPKIIII xD
from footer import footer

logging.basicConfig(level=logging.DEBUG)


def trollingContainer():
    """ 
        Tutaj jest metoda, tworząca dziwne rzeczy xD

    """
    container = Image.new('1', (epd.width, epd.height), 255)

    shadowFont = ImageFont.truetype(os.path.join(fontdir, 'Shadow.ttf'), 36)
    draw = ImageDraw.Draw(container)

    img = Image.open(os.path.join(icodir, 'pawel_kupa.bmp'))

    x, y = img.size

    container.paste(img, (0, 0))

    textContainer = Image.new('1', ((epd.width - x), (epd.height)), 255)
    textDraw = ImageDraw.Draw(textContainer)

    msg = "Poszukiwany"
    msg2 = "Czy widziałeś tego cżłowieka?"
    msg3 = "Nagroda 10000 Cebulionów"

    textDraw.text((0, 0), msg, font = shadowFont, fill = 0)
    textDraw.text((0, 36), msg2, font = shadowFont, fill = 0)
    textDraw.text((0, 400), msg3, font = shadowFont, fill = 0)

    container.paste(textContainer, (x, 0))

    return container

def container(main_weather_img, side_images = []):
    """
    return: zwraca kontener wypełniony treścią
    """
    x = 180
    y = 60
    container = Image.new('1', (epd.width, epd.height), 255)

    #tutaj wypełnisz to treścią
    img = main_weather_img
    container.paste(img, (0, y))

    # Pogoda na później
    for i in side_images:
        item = i
        container.paste(item, (x, (y + 20)))
        x += 155

    # dodanie zdjęcia Kiry w lewym rogu
    kira = Image.open(os.path.join(icodir, 'kira2.bmp'))
    container.paste(kira, (0, 380))

    # Nagłówek
    top = topImg()
    container.paste(top, (0 , 0))

    # stupki
    f = footer()
    container.paste(f, (200, 370))

    return container

try:
    epd = epd7in5_V2.EPD()

    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    if False:
        logging.info("Trolling Container on the way!!!!!")
        troll = trollingContainer()
        epd.display(epd.getbuffer(troll))

        logging.info("Goto Sleep...")
        epd.sleep()
        time.sleep(20)

        logging.info("init and Clear")
        epd.init()
        epd.Clear()

    
    
    logging.info("creating container")
    con = container(leftImg(currentWeather), side_images = wList)
    epd.display(epd.getbuffer(con))

    
    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5_V2.epdconfig.module_exit()
    exit()

### END OF FILE ###