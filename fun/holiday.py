import sqlite3

from data.holidays import HOLIDAYS
from data.date import DAY, MONTH, YEAR, SLUB
from objects.holiday import Holiday


PATH_TO_DB = "/home/pi/Code/Python/django/Calc/WebCal/db.sqlite3"

def holiday(month = MONTH, day = DAY) -> list:
    """Stworzenie listy zawierającej nazwę wydarzenia oraz statusu, który daje informację,
        Czy dany dzień ma święta. 

    Args:
        month (_type_, optional): Numer miesiąca. Defaults to dzisiejszy miesiąc.
        day (_type_, optional): Numer dnia. Defaults to dzisiejszy dzień.

    Returns:
        list: 0: nazwa 1: status
    """
    l = []
    if month in HOLIDAYS:
        if day in HOLIDAYS[month]:
            l.append(HOLIDAYS[month][day])
            l.append(1)
            return l
        else:
            if SLUB > 0:
                l.append(f"Zostało {SLUB} dni.")
                l.append(0)
                return l
            else:
                l.append(f"Dargowo {YEAR}")
                l.append(0)
                return l
    return l

def holidaydb(month = MONTH, day = DAY) -> list:
    """Stworzenie listy zawierającej nazwę wydarzenia oraz statusu, który daje informację,
        Czy dany dzień ma święta. Pobiera dane z bazy danych. 

    Args:
        month (_type_, optional): Numer miesiąca. Defaults to dzisiejszy miesiąc.
        day (_type_, optional): Numer dnia. Defaults to dzisiejszy dzień.

    Returns:
        list: 0: nazwa 1: status
    """
    
    l= []
    conn = sqlite3.connect(PATH_TO_DB)
    cursor = conn.cursor()
    request = f"""
                select name, date, manager_id, isHoliday, coroku, description
                from events_events                
                where strftime('%m', date) = '{month:02}'
                and strftime('%d', date) = '{day:02}'
            """
    cursor.execute(request)
    res = cursor.fetchall()
    conn.close()

    if res:
        for item in res:
            h = Holiday(item)
            l.append(h)

    if l:
        a = l[0]
        for i in l:
            if i.category() == 'Wydarzenie':
                l = [i.getName(), 1]
                print(l)
                return l
        l = [l[0].getName(), 1]
        return l
    else:
        l=[f'Dargowo {YEAR}', 0]
        return l

