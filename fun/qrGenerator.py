from random import choices
import qrcode



def qrGenerator():
    '''Prosty generator kodów QR
    
    Zwraca: qrcode z czymkolwiek bedzie w tekscie stringa xD
    '''
    losowe = ["https://pl.wikipedia.org/wiki/Specjalna:Losowa_strona", "https://secretoftaste.blog/wylosuj-przepis/", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
    i = 3

    tekst = choices(losowe, weights = [44, 44, 2], k = 1)[0]

    qr = qrcode.QRCode(version=1,box_size=i,border=1)

    qr.add_data(tekst)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    return img