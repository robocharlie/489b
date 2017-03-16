import RPi.GPIO as GPIO
import time


class Shifter():
    # initialization
    def __init__(self, data, latch, clock):
        # Port numbering
        GPIO.setmode(GPIO.BCM)

        # Define pins
        self.data_pin = data
        self.latch_pin = latch
        self.clock_pin = clock

        # Setup the pins
        GPIO.setup(self.data_pin, GPIO.OUT)
        GPIO.setup(self.latch_pin, GPIO.OUT, initial=0)
        GPIO.setup(self.clock_pin, GPIO.OUT, initial=0)

    # Function to toggle latch/clock pins
    def toggle(self, pin):
        GPIO.output(pin, 1)
        time.sleep(0)
        GPIO.output(pin, 0)

    # Function to set number
    def set_value(self, byte_val):
        for i in range(8):
            GPIO.output(self.data_pin, byte_val & (1 << (7 - i) > 0) # normal order & value
            #GPIO.output(self.data_pin, byte_val & (1 << i) == 0)
            self.toggle(self.clock_pin)

        self.toggle(self.latch_pin)