# gps-firebase
simple example for realtime gps location tracking with python, firebase, (raspberry+ublox gps module)

$ sudo apt-get install gpsd gpsd-clients

$ stty -F /dev/ttyAMA0 9600

$ sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock

$  cgps -s

#### Todos
- Frontend to present coordinates on map (Angular? Polymer?)
- Handle exception (requests.exceptions.HTTPError: 400 Client Error: Bad Request)


Resources that helped me
- http://www.instructables.com/id/Raspberry-Pi-the-Neo-6M-GPS/?ALLSTEPS
- http://stackoverflow.com/questions/6146131/python-gps-module-reading-latest-gps-data
