# Shift register class

import RPi.GPIO as GPIO
import time

class Shifter():

  def __init__(self, data, latch, clock):
    self.dataPin, self.latchPin, self.clockPin = data, latch, clock
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.dataPin, GPIO.OUT)  # set pins as outputs
    GPIO.setup(self.latchPin, GPIO.OUT, initial=0)
    GPIO.setup(self.clockPin, GPIO.OUT, initial=0)

  def ping(self, thePin):  # ping the clock or latch pin
    GPIO.output(thePin,1)
    time.sleep(0)
    GPIO.output(thePin,0)

  def setValue(self, byteVal):  # display a given byte pattern
    for i in range(8):    # 8 bits in register
      bit = int((byteVal & (1<<(7-i))) > 0)   # load MSB first, match high/low with byte
      # bit = int((byteVal & (1<<i)) == 0)        # load LSB first, invert high/low with byte
      GPIO.output(self.dataPin, bit)
      self.ping(self.clockPin)
    self.ping(self.latchPin)