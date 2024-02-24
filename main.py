#!/usr/bin/python3
# -*- coding:utf-8 -*-

import logging
import time


from src.app import makeImg
from lib import epd7in5_V2

from data.date import MINUTE, HOUR


def main():
    # img = leftImg(currentWeather=currentWeather)
    # im = img.save("test.png")

    # print(currentWeather)
    
    container = makeImg()
    person = makeImg(0)
    
    # im = container.save("test.png")
    im = container.save("test.png")

    try:
        epd = epd7in5_V2.EPD()

        if HOUR == 21 and MINUTE > 30:
            logging.info("init and Clear")
            epd.init()
            epd.Clear()
            logging.info("creating screen")
            epd.display(epd.getbuffer(person))
            logging.info("Going to sleep")
            epd.sleep()
            time.sleep(10)
        
        logging.info("init and Clear")
        epd.init()
        epd.Clear()

        logging.info("creating screen")
        epd.display(epd.getbuffer(container))

        logging.info("Going to sleep")
        epd.sleep()
    except IOError as e:
        logging.info(e)
    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd7in5_V2.epdconfig.module_exit()
        exit()

    

if __name__ == '__main__':
    main()