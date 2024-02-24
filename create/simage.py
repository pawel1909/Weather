import os

from PIL import Image, ImageDraw

from data.fonts import SHADOW24


icodir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'icons')

def specialImage(text: str):
    WIDTH = 150
    HEIGHT = 160

    specialImg = Image.new('1', (WIDTH, HEIGHT), 255)
    draw = ImageDraw.Draw(specialImg)

    

    kira = Image.open(os.path.join(icodir, 'kira.bmp'))
    specialImg.paste(kira, (0, 40))

    # x, y = draw.textsize(text, font=SHADOW24)
    # draw.text(((int(WIDTH - x) / 2, 0)), text, font=SHADOW24)

    return specialImg