from random import choice

def iloscSlow(zdanie):
    lista_Slow = zdanie.split()
    z = ""
    i = len(lista_Slow)
    x = 0
    print(i / 2)
    if i <= 5:
        for slowo in lista_Slow:
            z += slowo + " "
    if i > 5:
        for slowo in lista_Slow:
            if x < int(i / 2):
                z += slowo + " "
                x += 1
            elif x == int(i / 2):
                z += "\n" + slowo + " "
                x += 1
            else:
                z += slowo + " "

    

    return z

glupie = [
    "Nigdy nie cofaj się Wstecz!",
    "2 + 2 * 2 = 6",
    "Jeśli coś może pójść źle, to pójdzie.",
    "Jeśli wróg jest w zasięgu, ty również.",
    ""
]

wiadomosc_Daty = {
    "palecPiotrka": "Tego dnia piotrek z 10 palców, zrobił 9",
    "urodzinyMamy": [""]

}

print(choice(glupie))