from picamera import PiCamera
from time import sleep
import datetime
import os

import config

camera = PiCamera()

defaultPath = config.defaultImagePath

#print(defaultPath)

def takePhoto(savePath = defaultPath):
    #todaysPath = savePath + str(datetime.datetime.now().date()) + "/" # USE THIS TO SAVE AND KEEP ALL IMAGES
    todaysPath = savePath
    if not os.path.exists(todaysPath):
        os.makedirs(todaysPath)
        
    #finalPath = todaysPath + str(datetime.datetime.now().time()) + ".jpg" # USE THIS TO SAVE AND KEEP ALL IMAGES
    finalPath = todaysPath + "temp.jpg"
    #camera.start_preview()
    #sleep(10)
    camera.capture(finalPath)
    #camera.stop_preview()

    return finalPath


