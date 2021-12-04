import datetime

def date(timestamp: int):
    return datetime.datetime.fromtimestamp(timestamp).date()

def retTime(timestamp: int):
    time = datetime.datetime.fromtimestamp(timestamp)
    ftime = datetime.timedelta(hours=1)
    x = time + ftime
    return x.time()

def rawData(timestamp: int):
    return datetime.datetime.fromtimestamp(timestamp)

    ### END OF FILE ###