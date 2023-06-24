import os
from random import choice
from PIL import Image, ImageDraw

from data.fonts import SHADOW24, ROBOTO24, ROBOTO36, ROBOTO40

imgdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'image')


def personImage():
    """Specjalny obraz pojawiajacy sie o konkretnej godzinie
    """
    
    WIDTH = 800
    HEIGHT = 480

    container = Image.new('1', (WIDTH, HEIGHT), 255)
    draw = ImageDraw.Draw(container)

    kto = choice(["pawel", "piter", "elwira"])

    img = Image.open(os.path.join(imgdir, f"{kto}.bmp"))

    container.paste(img, (0, 0))

    x, y = img.size

    textBox_x = WIDTH - x
    textContainer = Image.new('1', (textBox_x, HEIGHT), 255)
    textDraw = ImageDraw.Draw(textContainer)

    KROPKA = u"\u2022"

    if kto == "piter":
        poszukiwany = "Poszukiwany!"
        poszukiwany_tekst = "Czy widziałeś tego człowieka?"
        cechySzczegolne = "Cechy szczególne."
        nagroda = "Nagroda 1000 Cebulionów"

        cecha1 = "Mętny wzrok"
        cecha2 = "Ciemne nienawistne oczy"
        cecha3 = "Woń alkoholu unosząca się dookoła"

        #wymiary
        x1, y1 = textDraw.textsize(poszukiwany, font = ROBOTO40)
        x2, y2 = textDraw.textsize(poszukiwany_tekst, font = SHADOW24)
        x3, y3 = textDraw.textsize(cechySzczegolne, font = ROBOTO36)
        x4, y4 = textDraw.textsize(cecha1, font = SHADOW24)
        x5, y5 = textDraw.textsize(cecha2, font = SHADOW24)
        x6, y6 = textDraw.textsize(nagroda, font = ROBOTO36)

        ### POSZUKIWANY ###
        textDraw.text((int((textBox_x - x1) / 2), 0), poszukiwany, font = ROBOTO40, fill = 0)
        ### --------------- ###
        textDraw.line(((80, 44), ((textBox_x - 80), 44)), fill = 0, width = 4)
        ### Czy Widziałeś tego człowieka?
        textDraw.text((100, (y1 + 10)), poszukiwany_tekst, font = SHADOW24, fill = 0)
        ### Cechy szczególne ###
        textDraw.text((int((textBox_x - x3) / 2), (y1 + y2 + 20)), cechySzczegolne, font = ROBOTO36, fill = 0)
        ### --------------- ###
        textDraw.line(((80, (y1 + y2 + y3 + 24)), ((textBox_x - 80), (y1 + y2 + y3 + 24))), fill = 0, width = 3)
        ### pierwsza ###
        textDraw.text((100, (y1 + y2+ y3 + 30)), KROPKA, font = ROBOTO40, fill = 0)
        textDraw.text((130, (y1 + y2+ y3 + 30)), cecha1, font = SHADOW24, fill = 0)
        ### drUga ###
        textDraw.text((100, (y1 + y2+ y3 + y4 + 30)), KROPKA, font = ROBOTO40, fill = 0)
        textDraw.text((130, (y1 + y2+ y3 + + y4 + 30)), cecha2, font = SHADOW24, fill = 0)
        ### czecia ###
        textDraw.text((100, (y1 + y2+ y3 + y4 + y5 + 30)), KROPKA, font = ROBOTO40, fill = 0)
        textDraw.text((130, (y1 + y2+ y3 + y4 + y5 + 30)), cecha3, font = SHADOW24, fill = 0)
        # textDraw.text((0, 36), msg2, font = shadowFont, fill = 0)
        textDraw.text((100, 400), nagroda, font = ROBOTO24, fill = 0)

    elif kto == "pawel":
        poszukiwany = "Poszukiwany!"
        poszukiwany_tekst = "Czy widziałeś tego człowieka?"
        cechySzczegolne = "Cechy szczególne."
        nagroda = "Nagroda 100 Cebulionów"

        cecha1 = "Siwe włosy"
        cecha2 = "Ciemne nienawistne oczy"
        cecha3 = "Codziennie coraz większy brzuch."

        #wymiary
        x1, y1 = textDraw.textsize(poszukiwany, font = ROBOTO40)
        x2, y2 = textDraw.textsize(poszukiwany_tekst, font = SHADOW24)
        x3, y3 = textDraw.textsize(cechySzczegolne, font = ROBOTO36)
        x4, y4 = textDraw.textsize(cecha1, font = SHADOW24)
        x5, y5 = textDraw.textsize(cecha2, font = SHADOW24)
        x6, y6 = textDraw.textsize(nagroda, font = ROBOTO36)

        ### POSZUKIWANY ###
        textDraw.text((int((textBox_x - x1) / 2), 0), poszukiwany, font = ROBOTO40, fill = 0)
        ### --------------- ###
        textDraw.line(((80, 44), ((textBox_x - 80), 44)), fill = 0, width = 4)
        ### Czy Widziałeś tego człowieka?
        textDraw.text((100, (y1 + 10)), poszukiwany_tekst, font = SHADOW24, fill = 0)
        ### Cechy szczególne ###
        textDraw.text((int((textBox_x - x3) / 2), (y1 + y2 + 20)), cechySzczegolne, font = ROBOTO36, fill = 0)
        ### --------------- ###
        textDraw.line(((80, (y1 + y2 + y3 + 24)), ((textBox_x - 80), (y1 + y2 + y3 + 24))), fill = 0, width = 3)
        ### pierwsza ###
        textDraw.text((100, (y1 + y2+ y3 + 30)), KROPKA, font = ROBOTO40, fill = 0)
        textDraw.text((130, (y1 + y2+ y3 + 30)), cecha1, font = SHADOW24, fill = 0)
        ### drUga ###
        textDraw.text((100, (y1 + y2+ y3 + y4 + 30)), KROPKA, font = ROBOTO40, fill = 0)
        textDraw.text((130, (y1 + y2+ y3 + + y4 + 30)), cecha2, font = SHADOW24, fill = 0)
        ### czecia ###
        textDraw.text((100, (y1 + y2+ y3 + y4 + y5 + 30)), KROPKA, font = ROBOTO40, fill = 0)
        textDraw.text((130, (y1 + y2+ y3 + y4 + y5 + 30)), cecha3, font = SHADOW24, fill = 0)
        # textDraw.text((0, 36), msg2, font = shadowFont, fill = 0)
        textDraw.text((100, 400), nagroda, font = ROBOTO24, fill = 0)


    elif kto == "elwira":
        poszukiwany = "Kącik poetycki"
        poszukiwany_tekst = "Znane i mniej znane cytaty"
        nagroda = "Nagroda 100 Cebulionów"

        cecha1 = "Czuję, że gdzieś idę"
        cecha2 = "A to działa wgl?"
        cecha3 = "Obyś sobie walnął mordą w twarz"

        #wymiary
        x1, y1 = textDraw.textsize(poszukiwany, font = ROBOTO40)
        x2, y2 = textDraw.textsize(poszukiwany_tekst, font = SHADOW24)
        x4, y4 = textDraw.textsize(cecha1, font = SHADOW24)
        x5, y5 = textDraw.textsize(cecha2, font = SHADOW24)
        x6, y6 = textDraw.textsize(nagroda, font = ROBOTO36)

        ### POSZUKIWANY ###
        textDraw.text((int((textBox_x - x1) / 2), 0), poszukiwany, font = ROBOTO40, fill = 0)
        ### --------------- ###
        textDraw.line(((60, 44), ((textBox_x - 60), 44)), fill = 0, width = 4)
        ### Czy Widziałeś tego człowieka?
        textDraw.text((80, (y1 + 10)), poszukiwany_tekst, font = SHADOW24, fill = 0)
        ### pierwsza ###
        textDraw.text((100, (y1 + y2 + 30)), KROPKA, font = ROBOTO40, fill = 0)
        textDraw.text((130, (y1 + y2 + 30)), cecha1, font = SHADOW24, fill = 0)
        ### drUga
        textDraw.text((100, (y1 + y2 + y4 + 30)), KROPKA, font = ROBOTO40, fill = 0)
        textDraw.text((130, (y1 + y2 + + y4 + 30)), cecha2, font = SHADOW24, fill = 0)
        ### czecia
        textDraw.text((100, (y1 + y2 + y4 + y5 + 30)), KROPKA, font = ROBOTO40, fill = 0)
        textDraw.text((130, (y1 + y2 + y4 + y5 + 30)), cecha3, font = SHADOW24, fill = 0)

    container.paste(textContainer, (x, 0))

    return container