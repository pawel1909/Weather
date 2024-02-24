from datetime import datetime

PATH_TO_DB = "/home/pi/Code/Python/django/Calc/WebCal/db.sqlite3"

MONTH_NAME = {
    'January': 'Styczeń',
    'February': 'Luty',
    'March': 'Marzec',
    'April': 'Kwiecień',
    'May': 'Maj',
    'June': 'Czerwiec',
    'July': 'Lipiec',
    'August': 'Sierpień',
    'September': 'Wrzesień',
    'October': 'Październik',
    'November': 'Listopad',
    'December': 'Grudzień'
}

DAY_NAME = {
    'Monday': 'Poniedziałek',
    'Tuesday': 'Wtorek',
    'Wednesday': 'Środa',
    'Thursday': 'Czwartek',
    'Friday': 'Piątek',
    'Saturday': 'Sobota',
    'Sunday': 'Niedziela'
}

class Holiday():
    def __init__(self, holiday):

        self._name = holiday[0]
        self._date = holiday[1]
        self._manager = holiday[2]
        self._description = holiday[5]
        self._isHoliday = holiday[3]
        self._coroku = holiday[4]
    
    def getName(self):
        return f"{self._name}"
    
    def getDescription(self):
        return f'{self._description}'
    
    def category(self):
        if self._isHoliday == 1:
            return "Holiday"
        elif self._coroku == 1:
            return "Coroku"
        else:
            return "Wydarzenie"

    def date(self) -> dict:
        date = self._date
        dateMonth = datetime(date).date().strftime('%B')
        montName = MONTH_NAME[dateMonth]
        dateDay = datetime(date).date().strftime('%A')
        dayName = DAY_NAME[dateDay]
        
        return {
            'MonthNumber': dateMonth,
            'MonthName': montName,
            'DayNumber': dateDay,
            'DayName': dayName,
        }

    def __str__(self) -> str:
        date = self._date
        dateMonth = datetime(date).date().strftime('%B')
        dateMonth = MONTH_NAME[dateMonth]
        dateDay = datetime().date(date).day
        return f"{self._name}  {dateDay} - {dateMonth}. Stworzone przez: {self._manager}"