import os

from screen import container
from PIL import Image
from daily_images import wList
from app import currentWeather, hList
from main_image import leftImg
from functions.plottwist import makePlot


pathToPlot = os.path.dirname(os.path.dirname(__file__))
print("TEST "*5,"\n",pathToPlot)
makePlot(hList)
im = container(leftImg(currentWeather), side_images = wList)
im = im.save("test.png")
