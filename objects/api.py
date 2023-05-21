# funkcja do konwersji daty
from fun.date import date, rawData, retTime
# Funkcja do tłumaczenia. API zwraca wyniki w języku angielskim
from fun.translate import dayToPL, monthToPL
# DEBUG
from data.debug import DEBUG



class Weather_obj():
    def __init__(
            self,
            date,
            temperature_day,
            temperature_night,
            temp_min,
            temp_max,
            humidity,
            pressure,
            wind_speed,
            status,
            detailed_status,
            sunset_time,
            sunrise_time,
            icon_id):
        self.__date = date
        self.__temperatureDay = f"{temperature_day}{chr(176)}C"
        self.__temperatureNight = f"{temperature_night}{chr(176)}C"
        self.__minMaxTemp = f"{int(temp_min)}{chr(175)}C ~ {int(temp_max)}{chr(176)}C"
        self.__humidity = humidity
        self.__pressure = pressure
        self.__windSpeed = f"Wiart: {wind_speed}m/s"
        self.__status = status
        self.__detailedStatus = detailed_status
        self.__sunset = sunset_time
        self.__sunrise = sunrise_time
        self.__iconID = icon_id
        

    # Zwraca słownik z różnymi formatami daty TODO jest sens robić dla każdego oddzielną funkcję?
    def getDate(self):
        return {
            "str": date(self.__date),
            "day": dayToPL(rawData(self.__date).strftime("%a")),
            "dayNr": rawData(self.__date).strftime("%d"),
            "month": monthToPL(rawData(self.__date).strftime("%b")),
            "intDay": rawData(self.__date).strftime("%w"),
            "intMonth": rawData(self.__date).strftime("%m")
        }
    
    # Zwraca temperature
    def getTemperature(self,timeOfTheDay = "day"):
        """Zwraca temperaturę

        Args:
            timeOfTheDay (str, optional): Dodaj "night" jeśli po 22. Defaults to "day".

        Returns:
            string: tekst z temperaturą i znakiem stopni Celciusza
        """
        if timeOfTheDay == "day":
            return self.__temperatureDay
        else:
            return self.__temperatureNight
        
    def getMinMaxTemp(self):
        """Zwraca zakres temperatur

        Returns:
            string: x ~ x
        """
        return self.__minMaxTemp
    
    def getStatus(self):
        """Zwraca tekst statusu dla pogody

        Returns:
            string: status
        """
        return self.__status
    
    def getDetailedStatus(self):
        """Zwraca tekst szczegółowy statusu

        Returns:
            string: status szczegółowy
        """
        return (self.__detailedStatus[0].upper() + self.__detailedStatus[1:])
    
    def getHumidity(self):
        """Wilgotność powietrza

        Returns:
            string: wilgotność z api
        """
        return f"Wilgotność: {self.__humidity}%"

    def getPressure(self):
        """ciśnienie

        Returns:
            string: _description_
        """
        return f"Ciśnienie {self.__pressure}hPa"
    
    def getRawPressure(self):
        """czysta liczba ciśnienia

        Returns:
            int: prawdopodobnie
        """
        return self.__pressure

    def getWindSpeed(self):
        """prędkość wiatru

        Returns:
            string: podczas generowania obiektu tworzy się słowo TODO sprawdzić, czy lepiej jest stworzyćstringa w metodzie, czy nie
        """
        return self.__windSpeed

    def getSunrise(self):
        return f"Wschód słońca: {retTime(self.__sunrise)}"

    def getSunset(self):
        return f"Zachód słońca: {retTime(self.__sunset)}"

    def getIconID(self):
        """id ikony z API

        Returns:
            int: ikona znajduje się na stronie API TODO ściągać obrazy bezpośrednio ze strony?
        """
        return str(self.__iconID)
    
    def __str__(self):
        """Tekstowa reprezentacja obiektu

        Returns:
            string: do debugu
        """
        return f'Data: {self.getDate()},{self.getTemperature()},{self.getMinMaxTemp()},{self.getStatus()},{self.getDetailedStatus()},{self.getHumidity()},{self.getPressure()},{self.getWindSpeed()},{self.getSunrise()},{self.getSunset()},{self.getIconID()}'
