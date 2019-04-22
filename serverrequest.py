import requests
from datetime import datetime

import config

dvlaURL = config.dvlaURL
authURL = config.authURL
addURL = config.addURL
exitURL = config.exitURL
msgURL = config.messageURL
vacURL = config.getVacanciesURL

def getDvlaData(licensePlate):
    request = requests.get(dvlaURL + licensePlate)

    #print("Request: " + str(request))

    if not request.status_code == 404:
        data = request.json()

        #print("DATA: " + str(data))
        #print()
        #print("MOT: " + data['motDetails'])
        #print()
        #print("Tax: " + data['taxDetails'])

        return data #? Or just specific data

    return False

def getVehicle(licensePlate):
    request = requests.get(authURL + licensePlate)

    #print("Request: " + str(request))

    if not request.status_code == 404:
        data = request.json()
        #print("DATA: " + str(data))
        return data

    return False

def vehicleEntry(licensePlate):
    time = "&entryTime=" + str(datetime.now())
    request = requests.get(addURL + licensePlate + time)

    #print("Request: " + str(request))

    if not request.status_code == 404:
        data = request.json()
        if data:
            return data['success']

    return False

def vehicleExit(licensePlate):
    time = "&exitTime=" + str(datetime.now())
    request = requests.get(exitURL + licensePlate + time)

    #print("Request: " + str(request))

    if not request.status_code == 404:
        data = request.json()
        if data:
            return data['success']

    return False

def checkVacancies():
    #print("Checking vacancies...")
    request = requests.get(vacURL)

    if not request.status_code == 404:
        data = request.json()
        if data:
            return data['vacancies']

    return 0
    

def sendMessage(message):
    #print("Sending message: " + message)
    requests.get(msgURL + message)
    return
