import datetime
import time
import requests as r
from plyer import notification
covidData = None
try:
    covidData = r.get('https://corona-rest-api.herokuapp.com/Api/hungary/')
except:
    print("szar a net")
if covidData != None:
    data = covidData.json()['Success']

    while(True):
        notification.notify(
            title = "COVID19 statisztikák {}".format(datetime.date.today()),
            message = "Összes eset: {totalcases}\nMai esetek száma: {todaycases}\nMai halálok száma: {todaydeaths}\nAktív betegek száma: {active}".format(
                totalcases = data['cases'],
                todaycases = data['todayCases'],
                todaydeaths = data['todayDeaths'],
                active = data['active']),
            app_icon = "bell.ico",
            timeout = 50
        )
        time.sleep(60*60)
else:
    print("Nem létezik a weboldal.")