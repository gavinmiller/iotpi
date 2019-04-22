### CONSTANTS CONFIGURATION ###
import os

### CAMERA CONSTANTS ###
defaultImagePath = os.getcwd() + "/images/"

### SERVER REQUEST CONSTANTS ###
serverIP = "192.168.43.58"
serverPort = "80"

### DO NOT CHANGE ###
serverURL = "http://" + serverIP + ":" + serverPort + "/"
dvlaURL = serverURL + "dvla?licensePlate="
authURL = serverURL + "vehicledb/getvehicle?licensePlate="
addURL = serverURL + "vehicledb/addvehicle?licensePlate="
exitURL = serverURL + "vehicledb/exitvehicle?licensePlate="
messageURL = serverURL + "message?msg="
advMessageURL = serverURL + "displayadvanced?"
getVacanciesURL = serverURL + "getvacancies"
