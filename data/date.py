from datetime import datetime, date

data = datetime.now()
DAY = int(data.strftime("%d"))
MONTH = int(data.strftime("%m"))
YEAR = int(data.strftime("%Y"))
HOUR = int(data.hour)
MINUTE = int(data.minute)

DAYNAME = data.strftime("%a")


d = date.today()
s = date(2023, 8, 12)

SLUB = (s - d).days