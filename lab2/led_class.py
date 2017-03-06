# dependencies
import RPi.GPIO as GPIO
import time
from random import randint

class LEDdisplay():

    # Patterns for 0-9
    numbers = [
        int('00111111', 2),
        int('00000110', 2),
        int('01011011', 2),
        int('01001111', 2),
        int('01100110', 2),
        int('01101101', 2),
        int('01111101', 2),
        int('00000111', 2),
        int('01111111', 2),
        int('01101111', 2)
    ]

    # Patterns to show nothing, A-G, and then decimal
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
            # GPIO.output(self.data_pin, byte_val & (1 << (7 - i) > 0) # normal order & value
            GPIO.output(self.data_pin, byte_val & (1 << i) == 0)
            self.toggle(self.clock_pin)

        self.toggle(self.latch_pin)

    # pass an integer form 0 to 9 to display
    def set_number(self, num):
        self.set_value(self.scroll[num])

    # Pass a pin number, and set the given LED
    def set_single_pin(self, pin):
        self.set_value(int('10000000', 2) >> pin)

    def set_random_pins(self):
        self.set_value(randint(0, 255))

# Create led display object
the_LEDdisplay = LEDdisplay(16, 12, 6)

# Spam random combinations
for val in range(300):
    the_LEDdisplay.set_random_pins()
    print(val)
    time.sleep(.01)

# spiral pattern
pattern = [1, 2, 64, 16, 8, 4, 64, 32]
for x in range(5):
    for val in pattern:
        the_LEDdisplay.set_value(pattern[val])
        time.sleep(.1)



GPIO.cleanup()
