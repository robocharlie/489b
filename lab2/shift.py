# dependencies
import RPi.GPIO as GPIO
import time

# Port numbering
GPIO.setmode(GPIO.bcm)

# define pins
data_pin = 16
latch_pin = 12
clock_pin = 6

GPIO.setup(data_pin, GPIO.OUT)
GPIO.setup(latch_pin, GPIO.OUT, initial=0)
GPIO.setup(clock_pin, GPIO.OUT, initial=0)

four = int('00110011', 2)

mask = 1

for i in range(8):
    # if we want the led off, set gpio high
    if four & mask == 0:
        GPIO.OUTPUT(data_pin, 1)
    # else we want it on, set gpio low
    else:
        GPIO.OUTPUT(data_pin, 0)
    mask <<= 1

    GPIO.OUTPUT(clock_pin, 1)
    time.sleep(0)

    GPIO.OUTPUT(clock_pin, 0)
