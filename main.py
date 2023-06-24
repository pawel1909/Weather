import logging

from PIL import Image

from src.app import makeImg
from data.date import HOUR, MINUTE
from lib import epd7in5_V2


def main():
    # img = leftImg(currentWeather=currentWeather)
    # im = img.save("test.png")

    # print(currentWeather)
    state = 1
    
    container = makeImg(state)
    
    im = container.save("test.png")

    # try:
    #     epd = epd7in5_V2.EPD()
    #     logging.info("init and Clear")
    #     epd.init()
    #     epd.Clear()

    #     logging.info("creating screen")
    #     epd.display(epd.getbuffer(container))

    #     logging.info("Going to sleep")
    #     epd.sleep()
    # except IOError as e:
    #     logging.info(e)
    # except KeyboardInterrupt:
    #     logging.info("ctrl + c:")
    #     epd7in5_V2.epdconfig.module_exit()
    #     exit()

    

if __name__ == '__main__':
    main()