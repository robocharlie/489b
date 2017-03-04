# dependencies
import RPi.GPIO as GPIO
import time


class LEDdisplay():
    numbers = [
        int('10111111', 2),
        int('00000110', 2),
        int('11011011', 2),
        int('01001111', 2),
        int('11100110', 2),
        int('01101101', 2),
        int('11111101', 2),
        int('00000111', 2),
        int('11111111', 2),
        int('01101111', 2)
    ]

    scroll = [
        int('00000000', 2),
        int('00000001', 2),
        int('00000010', 2),
        int('00000100', 2),
        int('00001000', 2),
        int('00010000', 2),
        int('00100000', 2),
        int('01000000', 2),
        int('10000000', 2)
    ]

    def __init__(self, data, latch, clock):
        # Port numbering
        GPIO.setmode(GPIO.BCM)

        # define pins
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
            # GPIO.output(self.data_pin, byte_val & (1 << (7 - i) > 0) # normal order & value
            GPIO.output(self.data_pin, byte_val & (1 << i) == 0)
            self.toggle(self.clock_pin)

        self.toggle(self.latch_pin)

    # pass an integer form 0 to 9 to display
    def set_number(self, num):
        self.set_value(self.numbers[num])


the_LEDdisplay = LEDdisplay(16, 12, 6)

for val in range(10):
    the_LEDdisplay.set_number(val)
    time.sleep(1)
# set_value(numbers[5])

GPIO.cleanup()
