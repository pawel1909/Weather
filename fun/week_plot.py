import os
import json
import random

import matplotlib.pyplot as plt

from data.date import DAYNAME, HOUR, YEAR, MONTH, DAY

# funkcja do sprawdzenia poprawności kodu i wygenerowania plików
def test():
    for i in range(2023, 2026):
        for j in range(1, 13):
            for d in range(1, 3):
                for h in range(0, 25):
                    temp = random.randint(0, 33)
                    name = f"Dzien{d}"
                    createWeekFile(temperature=temp, year=i, month=j, day=d, dayname=name, hour=h)


def createWeekFile(temperature, year = YEAR, month= MONTH, day = DAY, dayname = DAYNAME, hour = HOUR):
    path = f"{os.path.dirname(os.path.abspath(__name__))}/plot/{year}_data.json"
    copy_path = f"{os.path.dirname(os.path.abspath(__name__))}/plot/{year}_data_copy.json"

    
    # TODO dodać metodę sprawdzającą, czy  kopia jest nowsza po tym odkomentować poniższe
    
    
    # Creates file copy. In case something went wrong.
    if(os.path.exists(path)):
        with open(path, 'r') as f1:
            with open(copy_path, 'w') as f2:
                t = json.load(f1)
                t = json.dumps(t)
                f2.write(t)
    

    
    
    if(os.path.exists(path)):
        with open(path, 'r') as f:
            temp = json.load(f)

            if not(f"{month}" in temp):
                temp.update({f"{month}": {}})
            if not(f"{day}" in temp[f"{month}"]):
                temp[f"{month}"].update({f"{day}": {"name": dayname}})
            

            if(hour == 6):
                a = temp[f"{month}"]
                b = temp[f"{month}"][f"{day}"]
                b.update({"rano": temperature})
                a[f"{day}"] = b
                temp[f"{month}"] = a
            elif(hour == 12):
                a = temp[f"{month}"]
                b = temp[f"{month}"][f"{day}"]
                b.update({"poludnie": temperature})
                a[f"{day}"] = b
                temp[f"{month}"] = a
            elif(hour == 18):
                a = temp[f"{month}"]
                b = temp[f"{month}"][f"{day}"]
                b.update({"wieczor": temperature})
                a[f"{day}"] = b
                temp[f"{month}"] = a
            elif(hour == 0):
                a = temp[f"{month}"]
                b = temp[f"{month}"][f"{day}"]
                b.update({"noc": temperature})
                a[f"{day}"] = b
                temp[f"{month}"] = a
        with open(path, 'w') as f:
            temp = json.dumps(temp)
            f.write(temp)
    else:
        with open(path, 'w') as f:
            temp = {}
            a = {}
            b ={}
            b["name"] = dayname
            a[f"{day}"] = b
            temp[f"{month}"] = a
            if(hour == 6):
                a = temp[f"{month}"]
                b = temp[f"{month}"][f"{day}"]
                b.update({"rano": temperature})
                a[f"{day}"] = b
                temp[f"{month}"] = a
            elif(hour == 12):
                a = temp[f"{month}"]
                b = temp[f"{month}"][f"{day}"]
                b.update({"poludnie": temperature})
                a[f"{day}"] = b
                temp[f"{month}"] = a
            elif(hour == 18):
                a = temp[f"{month}"]
                b = temp[f"{month}"][f"{day}"]
                b.update({"wieczor": temperature})
                a[f"{day}"] = b
                temp[f"{month}"] = a
            elif(hour == 0):
                a = temp[f"{month}"]
                b = temp[f"{month}"][f"{day}"]
                b.update({"noc": temperature})
                a[f"{day}"] = b
                temp[f"{month}"] = a
            temp = json.dumps(temp)
            f.write(temp)
    