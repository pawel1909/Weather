# Plik używany do czegoś innego, niż sugeruje nazwa
# Mój własny plik sprawdzania konfiguracji

from PIL import ImageDraw, ImageFont, Image
import sys
import os

import datetime

teraz = datetime.datetime.now()

# fontdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')

# im = Image.new('1', (100, 100), 255)

# draw = ImageDraw.Draw(im)

# roboto1 = ImageFont.truetype(os.path.join(fontdir, 'Roboto-Bold.ttf'), 36)



# w, h = draw.textsize('roboto 1', font = roboto1)

# print(w)

data = datetime.datetime(2021, 12, 1)

print(data.date() == teraz.date())


print(f"Data dzisiejsza: {teraz}\n")

filename = os.path.join('/home/pi/Keys', 'owm.txt')

API_KEY = ""
with open(filename) as f:
    API_KEY = f.read()

### END OF FILE ###