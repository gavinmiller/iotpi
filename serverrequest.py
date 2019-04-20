import requests
from datetime import datetime

serverURL = "http://192.168.1.16:8080/"
dvlaURL = serverURL + "dvla?licensePlate="
authURL = serverURL + "vehicledb/getvehicle?licensePlate="
addURL = serverURL + "vehicledb/addvehicle?licensePlate="

def getDvlaData(licensePlate):
    request = requests.get(dvlaURL + licensePlate)

    print("Request: " + str(request))

    if request.status_code == 200:
        data = request.json()

        print("DATA: " + str(data))
        print()
        print("MOT: " + data['motDetails'])
        print()
        print("Tax: " + data['taxDetails'])

        return data #? Or just specific data

    return False

def getVehicle(licensePlate):
    request = requests.get(authURL + licensePlate)

    print("Request: " + str(request))

    if request.status_code == 200:
        data = request.json()
        print("DATA: " + str(data))
        return data

    return False

def vehicleEntry(licensePlate):
    time = "&entryTime=" + str(datetime.now())
    request = requests.get(addURL + licensePlate + time)

    print("Request: " + str(request))

    if request.status_code == 200:
        data = request.json()
        if data:
            return data['success']

        return False

vehicleEntry("VK68UDV")
vehicleEntry("AB74CDE")
