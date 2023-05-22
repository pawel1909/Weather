from objects.current import NowWeather
from objects.api import Weather_obj
from fun.plot import makePlot
from data.debug import DEBUG
from fun.week_plot import createWeekFile
from create.mImage import mainImage
from create.troll import troll



def makeImg(state: int):

    if state == 0:
        return troll()


    try:
        
        weather = NowWeather()

        objList = []
        hList = weather.hour()

        currentWeather = Weather_obj(
            weather.currentWeather().ref_time,
            int(weather.currentWeather().temperature('celsius')['temp']),
            int(weather.currentWeather().temperature('celsius')['temp']),
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

        wList = []
        for w in objList:
            wList.append(w)
        wList = wList[:4]

        container = mainImage(currentWeather, wList, "Ile mocy z paneli", 1)
        # Wstrzymane. Wymaga przebudowy obiektu pogody aby otrzymać temperaturę w danym momencie.
        # createWeekFile(1)

        if(DEBUG == 1):
            print("Pomyślne utworzenie obiektu")
    except:
        weather = None
        currentWeather = None
        objList = []
        hList = []
        wList = []
        if(DEBUG == 1):
            print("Obiekty nie zostały stworzone, będzie soń")

    return container

        


# createWeekPlot(12)