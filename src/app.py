import os
import sys
# ### Z JAKIEGOS POWODU TO MUSI BYĆ TUTAJ !!!! ###
# # import matplotlib
# import matplotlib.pyplot as plt
# from functions.fun import rawData
# ### BEZSENSUUUU ###
obj = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'objects')

if os.path.exists(obj):
    sys.path.append(obj)

from weather_obj import Weather_obj
from teraz import NowWeather
from functions.plottwist import makePlot
# from functions.plottwist import makePlot


weather = NowWeather()

#Lista obiektów pogodowych dotycząca 7 następnych dni
objList = []
hList = weather.hour()

currentWeather = Weather_obj(
    weather.currentWeather().ref_time,
    int(weather.currentWeather().temperature('celsius')['temp']),
    0,
    0,
    0,
    weather.currentWeather().humidity,
    weather.currentWeather().pressure['press'],
    weather.currentWeather().wind().get('speed'),
    weather.currentWeather().status,
    weather.currentWeather().detailed_status,
    weather.currentWeather().sset_time,
    weather.currentWeather().srise_time,
    weather.currentWeather().weather_icon_name
)

for item in weather:
    temp = item.temperature('celsius')
    obj = Weather_obj(
        item.ref_time,
        temp["day"],
        temp["night"],
        temp["min"],
        temp["max"],
        item.humidity,
        item.pressure['press'],
        item.wind().get('speed', None),
        item.status,
        item.detailed_status,
        item.sset_time,
        item.srise_time,
        item.weather_icon_name)
    objList.append(obj)

makePlot(hList)

# x = [rawData(item.ref_time).hour for item in hList]
# y = [int(item.temperature('celsius')["temp"]) for item in hList]
# x1 = x[:8]
# y1 = y[:8]
# x2 = [1,2,3,4,5,6,7,8]
# fig, ax = plt.subplots()
# ax.tick_params(axis = "x", direction = "in", pad = 3)
# # Ukrycie linii po bokach
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['left'].set_visible(False)
# plt.yticks([])
# # Określenie rozmiaru wykresu, oraz zapobiegnięcie wycięcia opisu osi x
# figa = plt.gcf()
# figa.set_size_inches(6,1.2)
# figa.subplots_adjust(bottom = 0.15)
# #stworzenie osi x z godzinami
# xt = [(str(item) + ":00") for item in x[:8] ]
# plt.xticks(ticks=[1,2,3,4,5,6,7,8], labels=xt)
# # Narysowanie wykresu
# plt.plot(x2,y[:8], 'o:k')
# plt.ylim(ymin = min(y[:9]) - 2)
# plt.ylim(ymax = max(y[:9]) + 2)
# #podpisanie punktów na wykresie
# for x, y in zip(x2,y1):
#     l = f"{y}{chr(176)}C"
#     plt.annotate(l, (x, y), textcoords = "offset points", xytext = (0, 10), ha = 'center')

# plt.savefig("/home/pi/WeatherStation/icons/xxx.png", dpi = 100)
# makePlot(hList)

# for i in objList:
#     print(i)

### END OF FILE ###