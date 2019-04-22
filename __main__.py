import cameramodule
import alprinteraction
import serverrequest
import time

takePictureDelay = 5 # How often the process runs (roughly)

# Takes a photo with the camera and returns the path to that photo
# Stored under (directorylocation)/images/(todaysdate)/(currenttime).jpg
def takePhoto():
    newImage = cameramodule.takePhoto()

    print("Image stored in: " + newImage)

    return newImage

# Scans an image under the given path variable and returns the suspected
# number plate and the confidence in that plate, or false if it cannot
# find anything
def scanImage(path):    
    #Interact with openalpr
    plate = alprinteraction.scanImage(path)
    return plate

# Sends a request to the nodejs server asking for the data from a dvla search
# on the specified license plate
def requestDvla(licensePlate):
    dvlaData = serverrequest.getDvlaData(licensePlate)
    return dvlaData

# Gets any stored information from the nodejs server/db about the given license
# plate
def getVehicleFromDB(licensePlate):
    vehicleData = serverrequest.getVehicle(licensePlate)
    return vehicleData

# Adds an entry time to the database for the specified license plate
# and returns true or false if successful
def addEntryTime(licensePlate):
    response = serverrequest.vehicleEntry(licensePlate)
    return response

# Adds an exit time for a vehicle that has left the carpark
def addExitTime(licensePlate):
    response = serverrequest.vehicleExit(licensePlate)
    return response



# Returns true or false depending on whether or not there are vacancies in
# the carpark
# (Possibly modify the output to return more details about the vacancy,
# e.g. floor 1, left, floor 3 right etc)
def checkVacancies():
    return serverrequest.checkVacancies()

# Sends a message to the server to send to the display Pi
def sendMessage(message):
    serverrequest.sendMessage(message)
    return

# Begins the process to check a vehicle at the entry gate's license plate
# in order to grant entry or not
def authenticate():
    print("Beginning the authentication process")
    sendMessage("Taking photo, please wait")
    image = takePhoto()
    scannedPlate = scanImage(image)
    #scannedPlate = "VK68UDV" # TEST CODE
    if scannedPlate:
        licensePlate = scannedPlate['plate']
        #licensePlate = scannedPlate # TEST CODE
        vehicleDBData = getVehicleFromDB(licensePlate)
        
        if vehicleDBData and vehicleDBData['authorised']:
             print("License plate: " + licensePlate + " is authorised!")
             addEntryTime(licensePlate)
             return True
        else:
            print("License plate: " + licensePlate + " is NOT authorised!")
            sendMessage("You are not authorised to enter!")
    else:
        print("No plate found in image: " + image)

    return False


###############################
###### Main program flow ######
###############################
currentTimer = takePictureDelay

def main():
    global currentTimer
    print("Beginning countdown")
    # Sending countdown
    while currentTimer > 0:
        #print(currentTimer)
        sendMessage(str(currentTimer) + " seconds until next picture")
        currentTimer -= 1
        time.sleep(1)

    currentTimer = takePictureDelay
    
    if authenticate():
        print("")
        '''spacesLeft = checkVacancies()
        if spacesLeft > 0:
            sendMessage("Enter")
            
        else:
            sendMessage("Car park full")
        # Do something'''
    main()

main()
