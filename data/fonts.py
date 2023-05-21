import os
import sys
# TODO dowiedzieć się, czy da sie inaczej dodać link do fontów
fontdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')

from PIL import ImageFont

fontdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')

ROBOTO40 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 40)
ROBOTO36 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 36)
ROBOTO24 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 24)
ROBOTO18 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 18)
ROBOTO16 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 16)
ROBOTO14 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 14)
ROBOTO12 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 12)
ROBOTO9 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 9)
ROBOTO6 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 6)

SHADOW36 = ImageFont.truetype(os.path.join(fontdir, 'Shadow.ttf'), 36)
SHADOW24 = ImageFont.truetype(os.path.join(fontdir, 'Shadow.ttf'), 24)
SHADOW9 = ImageFont.truetype(os.path.join(fontdir, 'Shadow.ttf'), 9)