
#Zwraca tablię wraz z jego skrótem w języku polskim, pewnie da się to zrobić lepiej
def dayToPL(day):

    """
    Zwraca tablicę z nazwą dnia wraz z jego skrótem w języku polskim

    day == datetime()strf("%a")

        Zwraca: dayToPL(day)[0] - Skrót
                dayToPL(day)[1] - Pełną nazwę dnia
    """
    if day == "Mon":
        return ["Pon", "Poniedziałek"]
    elif day == "Tue":
        return ["Wt", "Wtorek"]
    elif day == "Wed":
        return ["Śr", "Środa"]
    elif day == "Thu":
        return ["Czw", "Czwartek"]
    elif day == "Fri":
        return ["Pt", "Piątek"]
    elif day == "Sat":
        return ["Sob", "Sobota"]
    elif day == "Sun":
        return ["Nd", "Niedziela"]
    

#zwraca to samo co wyżej tylko input jest miesiącem
def monthToPL(month):

    """
    Zwraca tablicę z nazwą miesiąca wraz z jego skrótem w języku polskim

    month == datetime().strf("%b")

        Zwraca: monthToPL(month)[0] - Skrót
                monthToPL(month)[1] - Pełną nazwę miesiąca
    """

    if month == "Jan":
        return ["Sty", "Styczeń"]
    elif month == "Feb":
        return ["Lut", "Luty"]
    elif month == "Mar":
        return ["Mar", "Marzec"]
    elif month == "Apr":
        return ["Kwi", "Kwiecień"]
    elif month == "May":
        return ["Maj", "Maj"]
    elif month == "Jun":
        return ["Cze", "Czerwiec"]
    elif month == "Jul":
        return ["Lip", "Lipiec"]
    elif month == "Aug":
        return ["Sie", "Sierpień"]
    elif month == "Sep":
        return ["Wrz", "Wrzesień"]
    elif month == "Oct":
        return ["Paz", "Październik"]
    elif month == "Nov":
        return ["Lis", "Listopad"]
    elif month == "Dec":
        return ["Gru", "Grudzień"]