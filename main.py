#! /usr/bin/python
# License: MIT

import os
from gps import *
from time import *
import time
import threading
from firebase.firebase import FirebaseApplication, FirebaseAuthentication


gpsd = None

os.system('clear')

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd
    gpsd = gps(mode=WATCH_ENABLE)
    self.current_value = None
    self.running = True

  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next()

if __name__ == '__main__':
  gpsp = GpsPoller()

  SECRET = ''
  DSN = ''
  EMAIL = ''
  authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
  firebase = FirebaseApplication(DSN, authentication)

  try:
    gpsp.start()
    while True:

      os.system('clear')
      result = firebase.patch('/gps',
        {
            'latitude': gpsd.fix.latitude,
            'longitude': gpsd.fix.longitude,
            'time utc': gpsd.utc,
        })
      time.sleep(5)

  except (KeyboardInterrupt, SystemExit):
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join()
  print "Program finished."
