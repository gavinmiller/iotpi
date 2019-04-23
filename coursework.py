from sense_hat import SenseHat
sense = SenseHat()




blue = (0, 0, 255)
yellow = (255, 255, 0)
red = (255,0,0)
black = (255,255,255)
green = (0,255,0)
white=(0,0,0)
amber=(231,194,81)



def clearSense():
    sense.clear
    
def printMessage(str):
  sense.show_message(str, text_colour=black, scroll_speed=0.02)
  sense.clear

#This prints the data on a sensor hat so the user can view what is happening
  
def printAdvanced(data):
  code = data['status_code']
  message = data['message']
  if code == "1":
    sense.show_message(message, text_colour=white ,back_colour=green, scroll_speed=0.05)
    
  elif code == "2":
    sense.show_message(message, text_colour=amber, back_colour=white, scroll_speed=0.05)
     
  elif code == "3":
    sense.show_message(message, text_colour=red, back_colour=white, scroll_speed=0.05)

  clearSense()  
  
