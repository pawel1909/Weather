import qrcode



def qrGenerator(tekst):
    '''Prosty generator kodów QR
    
    Zwraca: qrcode z czymkolwiek bedzie w tekscie stringa xD
    '''
    wiki_losowe = "https://pl.wikipedia.org/wiki/Specjalna:Losowa_strona"
    i = 4

    if type(tekst) != type(""):
        tekst = wiki_losowe
        i = 3

    qr = qrcode.QRCode(version=1,box_size=i,border=1)

    qr.add_data(tekst)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    return img