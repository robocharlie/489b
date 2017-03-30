# Code to test our custom thingspeak.py module

from random import randrange
from time import sleep
from thingspeak import sendData

api_key = "RV3H5FDV17IZNFY7"
count = 0

try:
  while True:
    data = [randrange(100,1000), randrange(100,1000), randrange(100,1000)]
    sendData(data, api_key)
    count += 1
    sleep(16)

except KeyboardInterrupt:
  print("\nExiting, " + str(count) + " data events sent")
