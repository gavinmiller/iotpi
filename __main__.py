import cameramodule
import alprinteraction
import serverrequest

def takePhoto():
    newImage = cameramodule.takePhoto()

    print("Image stored in: " + newImage)

    return newImage

def scanImage(path):    
    #Interact with openalpr
    #plate = alprinteraction.scanImage("/home/pi/Desktop/Coursework/images/test/vk68udv.jpg")
    plate = alprinteraction.scanImage(path)
    return plate

def requestDvla(licensePlate):
    dvlaData = serverrequest.getDvlaData(licensePlate)
    return dvlaData

def getVehicleFromDB(licensePlate):
    vehicleData = serverrequest.getVehicle(licensePlate)
    return vehicleData

def authenticate():
    #image = takePhoto()
    #scannedPlate = scanImage(image)
    scannedPlate = scanImage("/home/pi/Desktop/Coursework/images/test/vk68udv.jpg")
    #scannedPlate = "VK68UDV"
    if scannedPlate:
        licensePlate = scannedPlate['plate']
        #dvlaData = requestDvla(licensePlate)
        vehicleDBData = getVehicleFromDB(licensePlate)
        
        if vehicleDBData and vehicleDBData['authorised']:
             print("License plate: " + licensePlate + " is authorised!")
             addEntryTime(licensePlate)
             return True
        else:
            print("License plate: " + licensePlate + " is NOT authorised!")
    else:
        print("No plate found in image: " + image)

    return False

def addEntryTime(licensePlate):
    allowedAccess = authenticate()

    if allowedAccess:
        response = serverrequest.vehicleEntry(licensePlate)
