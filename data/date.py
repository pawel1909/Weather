from datetime import datetime

date = datetime.now()
DAY = int(date.strftime("%d"))
MONTH = int(date.strftime("%m"))
YEAR = int(date.strftime("%Y"))
HOUR = int(date.hour)
MINUTE = int(date.minute)

DAYNAME = date.strftime("%a")

print(DAYNAME)