from PIL import Image, ImageDraw

from fun.holiday import holiday, holidaydb
from data.fonts import ROBOTO36
from data.debug import DEBUG

def topImage():
    """Tekst górny. Specjalny dla świąt zapisanych. 
    """

    WIDTH = 800
    HEIGHT = 60

    tImage = Image.new('1', (WIDTH, HEIGHT), 255)
    draw = ImageDraw.Draw(tImage)
    try:
        h = holidaydb()
        text = h[0]
        state = h[1]
    except Exception as e:
        print(e)
        try:
            h = holiday()
            text = h[0]
            state = h[1]
        except:
            text = "Coś poszło nie tak"
            state = 0

    x, y = draw.textsize(text, font=ROBOTO36)

    if state == 1:
        x, y = draw.textsize(text, font=ROBOTO36)
        x1 = 1.2 * x
        blackBox = Image.new('1', (int((x1)), (y + 6)), 0)
        dr = ImageDraw.Draw(blackBox)
        dr.text((int((x1 - x) / 2), 3), text, font = ROBOTO36, fill = 1)
        tImage.paste(blackBox, (int((WIDTH - x1) / 2), int((HEIGHT - y) / 2)))
    else:
        x, y = draw.textsize(text, font=ROBOTO36)
        blackBox = Image.new('1', (int((x * 2)), (y + 6)), 0)
        dr = ImageDraw.Draw(blackBox)
        dr.text(((x / 2), 3), text, font = ROBOTO36, fill = 1)
        tImage.paste(blackBox, (int((WIDTH - 2 * x) / 2), int((HEIGHT - y) / 2)))


    if DEBUG == 1:
        print("Pomyslnie stworzono tekst górny")
        print(text)
    return tImage


