# gps-firebase
simple example for realtime gps location tracking with python, firebase, (raspberry+ublox gps module)

$ stty -F /dev/ttyAMA0 9600

$ sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock

$  cgps -s
