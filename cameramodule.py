from picamera import PiCamera
from time import sleep
import datetime
import os

camera = PiCamera()

defaultPath = "/home/pi/Desktop/Coursework/images/"

def takePhoto(savePath = defaultPath):
    todaysPath = savePath + str(datetime.datetime.now().date()) + "/"
    if not os.path.exists(todaysPath):
        os.makedirs(todaysPath)
        
    finalPath = todaysPath + str(datetime.datetime.now().time()) + ".jpg"
    #camera.start_preview()
    #sleep(10)
    camera.capture(finalPath)
    #camera.stop_preview()

    return finalPath


