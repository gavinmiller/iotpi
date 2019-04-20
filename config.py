### CONSTANTS CONFIGURATION ###
import os

### CAMERA CONSTANTS ###
defaultImagePath = os.getcwd() + "/images/"

### SERVER REQUEST CONSTANTS ###
serverURL = "http://192.168.1.16:8080/"
dvlaURL = serverURL + "dvla?licensePlate="
authURL = serverURL + "vehicledb/getvehicle?licensePlate="
addURL = serverURL + "vehicledb/addvehicle?licensePlate="
exitURL = serverURL + "vehicledb/exitvehicle?licensePlate="
