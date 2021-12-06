# Plik używany do czegoś innego, niż sugeruje nazwa
# Mój własny plik sprawdzania konfiguracji

from PIL import ImageDraw, ImageFont, Image
import sys
import os


import qrcode

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

x = "test"
y = ["test", "test"]

print(type(x))
print(type(y))

if type(x) == type(""):
    print("Tak")

print("#" * 10)

#stworzenie instancji qrKoda
qr = qrcode.QRCode(version=1,box_size=10,border=5)

qr.add_data("Dupa, Cycki, Dupa")
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('xD.png')

### END OF FILE ###