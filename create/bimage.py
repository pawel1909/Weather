import os



from PIL import Image, ImageDraw

from fun.qrGenerator import qrGenerator
from data.debug import DEBUG


imgdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'images')

def bottomImage():
    WIDTH = 650
    HEIGHT = 120
    

    bImage = Image.new('1', (WIDTH, HEIGHT), 255)
    write = ImageDraw.Draw(bImage)

    write.line((0, 0, 600, 0), fill = 0)
    write.line((0, 150, 0, 0), fill = 0)

    try:
        plot = Image.open(os.path.join(imgdir, "plot.png"))
        bImage.paste(plot, (0, 0))
    except:
        pass
    

    qr = qrGenerator()

    bImage.paste(qr, (549, 19))

    if DEBUG == 1:
        print("Stworzono tekst dolny")
    return bImage


