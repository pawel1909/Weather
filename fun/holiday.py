from data.holidays import HOLIDAYS
from data.date import DAY, MONTH, YEAR

def holiday(month = MONTH, day = DAY) -> list:
    l = []
    if month in HOLIDAYS:
        if day in HOLIDAYS[month]:
            l.append(HOLIDAYS[month][day])
            l.append(1)
            return l
        else:
            l.append(f"Dargowo {YEAR}")
            l.append(0)
            return l
    return l
