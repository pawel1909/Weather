from objects.current import NowWeather
from objects.api import Weather_obj
from fun.plot import makePlot
from fun.errorlog import createLog
from data.debug import DEBUG
from fun.week_plot import createWeekFile
from create.mImage import mainImage
from create.troll import troll
from create.ktoimg import personImage



def makeImg(status = 1):

    
    

    try:
        if status == 0:
            container = personImage()
            print("Dupa2")
            return container
        l = []
        e0 = "Poczatek"
        weather = NowWeather()
        e1 = "Weather created."
        objList = []
        hList = weather.hour()
        e2 = "H weather created"

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
        e3 = "Create W obj"

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
        e4 = "Create list 1"
    
        makePlot(hList)
        e5 = "Create plot"
        wList = []
        for w in objList:
            wList.append(w)
        wList = wList[:4]
        e6 = "Before create containter"
        
    
        container = mainImage(currentWeather, wList, "Ile mocy z paneli", 1)
        # Wstrzymane. Wymaga przebudowy obiektu pogody aby otrzymac temperature w danym momencie.
        # createWeekFile(1)
        e7 = "Create everything!!!!!!"
        if(DEBUG == 1):
            print("Pomyslne utworzenie obiektu")
    except:
        
        l = []
        try:
            l.append(e0)
        except:
            l.append("NIMA")
        try:
            l.append(e1)
        except:
            l.append("NIEMA")
        try:
            l.append(e2)
        except:
            l.append("NIEMA")
        try:
            l.append(e3)
        except:
            l.append("NIEMA")
        try:
            l.append(e4)
        except:
            l.append("NIEMA")
        try:
            l.append(e5)
        except:
            l.append("NIEMA")
        try:
            l.append(e6)
        except: 
            l.append("NIEMA")
        try:     
            l.append(e7)
        except:
            l.append("NIEMA")
        weather = None
        currentWeather = None
        objList = []
        hList = []
        wList = []
        createLog(l)
        if(DEBUG == 1):
            print("Obiekty nie zostaly stworzone, bedzie son")
        return troll()
    

    
    

    return container

        


# createWeekPlot(12)