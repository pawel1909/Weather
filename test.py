# /solar_api/GetAPIVersion.cgi

import requests
from requests.auth import HTTPBasicAuth

user = 'wiolettapapiernik@o2.pl'
password = 'Dargowo8!'

url = "https://www.solarweb.com/PvSystems/Realtime?pvSystemId=7da5022a-5df0-4b90-9380-58dcb5d40ca7"

# Fill in your details here to be posted to the login form.
payload = {
    'username': user,
    'inUserPass': password
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post(url, data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    print(p.text)

    # An authorised request.
    # r = s.get('A protected web page url')
    # print(r.text)

with open("t.txt", 'w') as f:
    f.write(p.text)

# print(res.content)

# rj = res.json()
from datetime import datetime

now = datetime.now().hour

print(now)