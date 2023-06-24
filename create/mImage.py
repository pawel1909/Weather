
from PIL import Image, ImageDraw

from objects.api import Weather_obj
from fun.translate import dayToPL, monthToPL
from data.icons import icons
from .bimage import bottomImage
from .limage import leftImg
from .rimage import rightImage
from .timage import  topImage
from .simage import specialImage
from .ktoimg import personImage
from data.date import MINUTE


def mainImage(currentWeather: Weather_obj, wList: list, text: str, state: int):

    WIDTH = 800
    HEIGHT = 480

    right = rightImage(wList)
    left = leftImg(currentWeather)
    top = topImage()
    bottom = bottomImage()
    special = specialImage(text)
    
    containter = Image.new('1', (WIDTH, HEIGHT), 255)

    # if True:
    #     x = personImage()
    #     containter.paste(x, (0, 0))
    #     return containter
    
    containter.paste(left, (0, 60))
    containter.paste(special, (0, 340))
    containter.paste(top, (0, 0))
    containter.paste(right, (180, 80))
    containter.paste(bottom, (150, 350))

    return containter