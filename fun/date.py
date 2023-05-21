import datetime

# Funkcja zwracająca date w czytelnym formacie
def date(timestamp: int):
    return datetime.datetime.fromtimestamp(timestamp).date()


# TODO jeszcze nie wiem
def retTime(timestamp: int):
    time = datetime.datetime.fromtimestamp(timestamp)
    ftime = datetime.timedelta(hours=1)
    x = time + ftime
    return x.time()

# Ten sam czytelny format ale niesformatowany
def rawData(timestamp: int):
    return datetime.datetime.fromtimestamp(timestamp)