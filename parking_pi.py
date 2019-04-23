import RPi.GPIO as GPIO
import time
import requests


def start_sensor():
    # Initialises distance sensor

    GPIO.setmode(GPIO.BOARD)

    PIN_TRIGGER = 7
    PIN_ECHO = 11

    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)
    # setting correct GPIO pins as input and output pins

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    time.sleep(2)


def stop_sensor():
    # Stops sensor

    GPIO.cleanup()


def get_distance():
    # Takes measurement using distance sensor and returns distance in cm

    PIN_TRIGGER = 7
    PIN_ECHO = 11

    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    # triggers sensor for 1 nano second, sends out ultrasound for that time

    while GPIO.input(PIN_ECHO)==0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time # calculates time taken for ultrasound to return
    distance = round(pulse_duration * 17150, 2) # calculates distance by using constant of ultrasonic speed
    return distance


def get_occupancy(distanceInCM):
    # Returns whether parking space is occupied based on distance measurement
    # of sensor which is placed on the ground of a parking space

    if distanceInCM > 80:
        return False
    else:
        return True


def check_parking_space_for_update():
    # Checks the occupancy of the parking space
    # Checks it again after 30 seconds to confirm and avoid changing values in database
    # when a car only drives over or similar
    # Makes changes to global value variable only if the value returned by the sensor is different
    # Returns whether changes to the variable have been made

    global parking_space_value
    initial_value = parking_space_value

    sensor_value = get_occupancy(get_distance())
    time.sleep(30)
    if initial_value != sensor_value and sensor_value == get_occupancy(get_distance()): # i.e. when the occupancy has stayed the same
        parking_space_value = sensor_value
        return True # i.e. changes have been made
    
    return False # i.e. no changes have been made


def send_parking_space_update(id, status):
    # Sends GET request to database containing the id and occupancy status of the parking space
    request = requests.get(serverURL + "parkingspace?id=" + id + "&status=" + status)
    if request.status_code == 404:
        print("Request not successful")
        return False
    return True


serverIP = "192.168.43.58"
serverPort = "80"
serverURL = "http://" + serverIP + ":" + serverPort + "/"
parking_space_value = "False"  # i.e. parking space is empty
parking_space_id = "ab6"
parking_space_floor = "1"
parking_space_direction = "left"


# set up parking space on database
requests.get(serverURL + "initparkingspace?id=" + parking_space_id + "&floor=" + parking_space_floor + "&direction=" + parking_space_direction)

# Initialising sensor
start_sensor()

try:
    while True:
        # Continuously check for changes in parking space status (every 60 seconds)
        # and send update to database when status changes
        if check_parking_space_for_update():
            print("Status is: " + str(parking_space_value))
            send_parking_space_update(parking_space_id, str(parking_space_value))
        time.sleep(60)
except KeyboardInterrupt:
    stop_sensor()
