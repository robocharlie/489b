# COMPLETED TEMPLATE FOR IN-CLASS CODE DEVELOPMENT
# (without shift(), scroll(), 
#
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


def getIP():
    cmd = "ip addr show wlan0 | grep 'inet\ ' | awk '{print $2}' | cut -d/ -f1"
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    output = output.strip()    # remove whitespace characters
    return output


def delay_us(microsec):
    endTime = time.time() + (float(microsec)/1000000.0)
    while time.time() < endTime:
        pass


def ping():   # ping the clock enable pin (falling edge)
    gpio.output(en, 1)
    delay_us(100)
    gpio.output(en, 0)
    delay_us(1)


def write(value, inputMode=0):
    delay_us(1000)  # 1 ms delay to be safe
    gpio.output(rs, inputMode)    # set input mode (0=instruction, 1=character)
    theShifter.setValue(value)
    ping()


def set_row_col(row, col=0):  # set the cursor row + column position
    ddram = int('10000000', 2)  # base instruction for setting DRAM address
    # set display data RAM (DDRAM) address for row/col
    # (see pg. 196 of datasheet, noting 0x40 = b1000000 = 1 << 6)
    write(ddram | ((row << 6) + col))


def writeMessage(message):  # write a string to the display
    for i in message:
        write(ord(i), 1)


def clearDisplay():
    write(int('00000001', 2))  # clear display


def initialize():  # initialize the display:
    write(int('00111000', 2))  # Function set: 8-bit, 2 lines, 5x8 dots
    write(int('00001111', 2))  # Display ON, Cursor Off, Blinking Off
    write(int('00000110', 2))  # Entry Mode: Increment cursor, display shift Off
    write(int('00000010', 2))  # return home
    write(int('00000001', 2))  # clear display


def shift(steps, display=0):     # shift cursor/display by # steps left/right
    for i in range(abs(steps)):
        if steps > 0:
            write(int('00010111', 2) | (display << 3))  # shift right
        if steps < 0:
            write(int('00010011', 2) | (display << 3))  # shift left


def scroll(steps):  # scroll the screen left a set # of steps, then return
    pass  # this is a lab 3 problem

try:
    initialize()
    #
    # # writeMessage() demo:
    # set_row_col(0)  # go to 1st row
    # writeMessage(getIP())
    #
    # set_row_col(1)  # go to 2nd row
    # writeMessage(time.asctime(time.localtime(time.time())))
    #
    # time.sleep(5)
    #
    # # JSON data demo:
    # clearDisplay()
    # url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    # theJSON = getJSON(url)
    # set_row_col(0)
    # writeMessage(theJSON["metadata"]["title"])
    # set_row_col(1)
    # writeMessage(str(theJSON["metadata"]["count"]) + " events recorded")
    # time.sleep(3)
    # while True:
    #     for i in theJSON["features"]:  # print events greater than 4
    #         if i["properties"]["mag"] >= 4.0:
    #             clearDisplay()
    #             set_row_col(0)
    #             writeMessage(i["properties"]["place"])
    #             set_row_col(1)
    #             writeMessage("Magnitude " + str(i["properties"]["mag"]))
    #             time.sleep(3)
    time.sleep(3)
    write(0b01000001, 1)  # write A to screen
    time.sleep(3)
    write(int('00010111', 2))
    shift(4)
    write(0b01000010, 1)  # write A
    time.sleep(3)
    #write(int('00010011', 2))
    #write(int('00010011', 2))
    shift(-3)
    write(0b01000011, 1)
    time.sleep(3)
    shift(1, 1)
    time.sleep(3)
    clearDisplay()
    gpio.cleanup()

except KeyboardInterrupt:
    clearDisplay()
    gpio.cleanup()