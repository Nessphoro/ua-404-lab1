import requests

r = requests.get("https://raw.githubusercontent.com/Nessphoro/ua-404-lab1/master/main.py")

print(r.text)
