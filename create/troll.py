import os

from PIL import Image

imgdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'images')

def troll():
    WIDTH = 800
    HEIGHT = 480

    containter = Image.new('1', (WIDTH, HEIGHT), 255)
    img = Image.open(os.path.join(imgdir, 'son.bmp'))
    containter.paste(img)

    return containter