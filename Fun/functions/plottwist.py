# Metoda tworząca plik png z wykresem temperatur w 8 następujących po sobie godzinach
# Jeżeli zapytasz dlaczego zapisuje, to odpowiem, że nie było czasu, ale może teraz już umiesz xD

import os
import matplotlib
import matplotlib.pyplot as plt
from functions.fun import rawData
import datetime


def makePlot(arraj):
    
    '''
    Create plot of 
    '''
    # Wczytanie danych
    H = datetime.datetime.now().hour
    x = [rawData(item.ref_time).hour for item in arraj]
    y = [int(item.temperature('celsius')["temp"]) for item in arraj]

    x1 = x[:8]
    y1 = y[:8]
    x2 = [1,2,3,4,5,6,7,8]
    fig, ax = plt.subplots()
    ax.tick_params(axis = "x", direction = "in", pad = 3)

    # Ukrycie linii po bokach
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.yticks([])

    # Określenie rozmiaru wykresu, oraz zapobiegnięcie wycięcia opisu osi x
    figa = plt.gcf()
    figa.set_size_inches(6,1.2)
    figa.subplots_adjust(bottom = 0.15)

    #stworzenie osi x z godzinami


    # jedyny moment, w którym nie działa to godzina 23,
    # Nikt na to nie będzie patrzył o 23 xD
    xt = ["Teraz" if item == (H + 1) else (str(item) + ":00") for item in x1 ]
    plt.xticks(ticks=[1,2,3,4,5,6,7,8], labels=xt)

    # Narysowanie wykresu
    plt.plot(x2,y[:8], 'o:k')
    plt.ylim(ymin = min(y[:9]) - 2)
    plt.ylim(ymax = max(y[:9]) + 2)

    #podpisanie punktów na wykresie
    for x, y in zip(x2,y1):
        l = f"{y}{chr(176)}C"
        plt.annotate(l, (x, y), textcoords = "offset points", xytext = (0, 10), ha = 'center')

    # Get absolute path to icon directory in any machine
    pathToPlot = f"{os.path.dirname(os.path.abspath(__name__))}/icons/hourlyTemperaturePlot.png"
    # plt.savefig("/home/pi/WeatherStation/icons/xxx.png", dpi = 100)
    plt.savefig(pathToPlot, dpi = 100)

    
    

