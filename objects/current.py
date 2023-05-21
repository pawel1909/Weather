from fun.date import date
from data.api import mgr, lon, lat
from data.debug import DEBUG

class NowWeather():
    def __init__(self, lat = lat, lon = lon):
        try:
            call = mgr.one_call(lat, lon)
        except:
            if DEBUG == 1:
                print("mgr.one_call failes")
                print("Creating empty object")
                call = None
        self._one_call_now = call.forecast_daily
        self._current = call.current
        self._hourly = call.forecast_hourly
        self._start = 0
        self._end = len(self._one_call_now)

    # region iteracja
    def __iter__(self):
        return self
    
    def __next__(self):
        self._start += 1
        if self._start < self._end:
            return self._one_call_now[self._start]
        raise StopIteration
    # endregion iteracja

    def currentWeather(self):
        return self._current
    
    def hour(self):
        return [i for i in self._hourly]