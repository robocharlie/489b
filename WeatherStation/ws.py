# empty file to start things

# # bmp example
# import Adafruit_BMP.BMP085 as BMP085
#
# sensor = BMP085.BMP085()
#
# print 'Temp = {0:0.1f} *C'.format(sensor.read_temperature())
# print 'Pressure = {0:0.1f} Pa'.format(sensor.read_pressure())
# print 'Altitude = {0:0.1f} m'.format(sensor.read_altitude())
#
#
# #dht example slow refresh, only 1 hz
# import Adafruit_DHT
# import time
#
# sensor2 = Adafruit_DHT.DHT11
# dataport = 4 # whatever gpio port it is on
# print 'T = {0:0.1f}oC H = {1:0.1f}%'.format(T, H)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

hall = 17

GPIO.setup(hall, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def my_callback():
    print 'There it goes!'

GPIO.add_event_detect(hall, GPIO.RISING, callback=my_callback)

try:
    while True:
        pass
except:
    print("Exiting...")
    GPIO.cleanup()
