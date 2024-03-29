import socketio
import coursework


# URL for the main nodejs server ( and port )
serverPort = '80'
serverURL = 'http://192.168.43.58:' + serverPort

# Initialise the socketio client
sio = socketio.Client()



# Event listener for on connect message
@sio.on('connect')
def on_connect():
    print("Connected to server")

# Event listener for initial connection testing message
#@sio.on('test')
#def on_test(msg):
#    print(msg)

# Event listener for display messages e.g. access authorised, carpark full etc.
@sio.on('displayMessage')
def on_displayMessage(displayMessage):
    # @CALUM - Insert code here to display message using variable displayMessage['message'] (Gives message of what's up)
    print("Message to display: " + str(displayMessage))
    coursework.printMessage(displayMessage)

@sio.on('displayAdvanced')
def on_displayAdvanced(data):
    coursework.printAdvanced(data)


# Connection code below
sio.connect(serverURL) # Connects the socket to the given URL
sio.emit('test', {'msg': 'Hello world!'}) # Sends a test message to the server
sio.wait() # Waits for messages
sio.disconnect() # (Not necessary but eventually disconnects should the server not be available)
