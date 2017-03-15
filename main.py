#! /usr/bin/python
# License: GPL 2.0

import os
from gps import *
from time import *
import time
import threading
from firebase.firebase import FirebaseApplication, FirebaseAuthentication


gpsd = None #seting the global variable

os.system('clear') #clear the terminal (optional)

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true

  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread

  SECRET = ''
  DSN = ''
  EMAIL = ''
  authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
  firebase = FirebaseApplication(DSN, authentication)

  try:
    gpsp.start() # start it up
    while True:

      os.system('clear')

      result = firebase.patch('/gps',
	{

		'latitude': gpsd.fix.latitude,
		'longitude': gpsd.fix.longitude,
		'time utc': gpsd.utc,

	})
      time.sleep(5) #set to whatever

  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."
