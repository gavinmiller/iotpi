# Raspberry Pi Carpark authentication Python scripts
Raspberry Pi python scripts for the carpark authentication server. These deal with capturing an image every 'x' amount of seconds and scanning for a number plate, then allowing or denying entry based on whether or not the license plate is registered in the database, and if there are free spaces left.

Every script is to be downloaded on the functional gateway pi except the parking_pi.py script, which is for the parking space pi, and the socketclient.py and coursework.py script, which are meant for the sense-hat/display pi.

To run the program, ensure all pi's are running as well as the server, all are connected on the same network or can at least reach each other, and that all server IP's and ports are changed appropriately according to the port displayed on the servers console after first running and the ip of the server.

There are configs to be changed in config.py, parking_pi.py (lines 88, 89, 92, 93, 94), and socketclient.py.
