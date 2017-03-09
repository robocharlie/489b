# TEMPLATE FOR IN-CLASS CODE DEVELOPMENT

# LCD display with shift register (8-bit operation)
#   - Connect Qa->Qh from shift register to data0->data7 of LCD
#   - uses shifter.py for Shifter() class 

import RPi.GPIO as gpio
import time
from subprocess import *  # need for getIP() function
from shifter import Shifter
from getjson import getJSON

gpio.setmode(gpio.BCM)  # use GPIO pin numbering for extension board

# Pin configuration:
rs = 26  # register select (LCD pin 4)
en = 13  # clock enable (LCD pin 6)
for pin in (rs, en):
    gpio.setup(pin, gpio.OUT, initial=0)

dataPin, latchPin, clockPin = 16, 12, 6
theShifter = Shifter(dataPin, latchPin, clockPin)   # create shift register object

def getIP():  # get the Pi's IP number using a Unix command
    cmd = "ip addr show wlan0 | grep 'inet\ ' | awk '{print $2}' | cut -d/ -f1"
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    output = output.strip()    # remove whitespace characters
    return output


def delay_us(microsec):   # higher resolution delay function
    pass


def ping():   # ping the clock enable pin (falling edge)
    pass


def write(value, inputMode = 0):  # write input voltages to register
    pass


def shift(steps, display = 0):     # shift cursor/display by # steps left/right
    pass


def set_row_col(row, col=0):  # set the cursor row + column position
    pass


def writeMessage(message):  # write a string to the display
    pass


def scroll(steps):  # scroll the screen left a set # of steps, then return
    pass


def clearDisplay():
    pass


def initialize():  # initialize the display:
    pass
