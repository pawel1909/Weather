import os

import matplotlib.pyplot as plt
from data.date import HOUR
from .date import rawData

def makePlot(array):
    """Tworzenie wykresu temperatur przewidywanych przez API 

    Args:
        array (OWM.forecast_hourly): lista pogody w w przyszłych godzinach
    """
    x = [rawData(item.ref_time).hour for item in array][:8]
    y = [int(item.temperature('celsius')["temp"]) for item in array][:8]


    x1 = [1,2,3,4,5,6,7,8]

    ax = plt.subplot()
    ax.tick_params(axis = "x", direction = "in", pad = 3)

    # Ukrycie bocznuch linii
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.yticks([])

    # Określenie rozmiaru wykresu oraz anulowanie wyciecia osi x
    fig1 = plt.gcf()
    fig1.set_size_inches(6, 1.2)
    fig1.subplots_adjust(bottom=0.15)

    xt = ["Teraz" if item == (HOUR + 1) else (str(item) + ":00") for item in x]
    plt.xticks(ticks=x1, labels=xt)

    # Rysowanie wykresu
    plt.plot(x1, y, 'o:k')
    plt.ylim(ymin = min(y) - 2)
    plt.ylim(ymax = max(y) + 2)

    for x, y in zip(x1,y):
        l = f"{y}{chr(176)}C"
        plt.annotate(l, (x, y), textcoords = "offset points", xytext = (0, 10), ha = 'center')
    p = os.path.dirname(__file__)
    a = os.path.join(p, os.pardir)
    a = os.path.abspath(a)
    pathToPlot = f"{a}/images/plot.png"
    plt.savefig(pathToPlot, dpi = 100)