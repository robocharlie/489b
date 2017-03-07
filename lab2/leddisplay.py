import time
from shifter import Shifter
from random import randint


class LEDdisplay():
    # initialization
    def __init__(self, data, latch, clock):
        self.shifter = Shifter(data, latch, clock)

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

    # pass an integer from 0 to 9 to display
    def set_number(self, num):
        self.shifter.set_value(self.numbers[num])

    # Pass a pin number, and set the given LED
    def set_single_pin(self, pin):
        self.shifter.set_value(int('10000000', 2) >> pin)

    # Turn on a random combination of LEDs
    def set_random_pins(self):
        self.shifter.set_value(randint(0, 255))

    # Spiral pattern
    def patterns(self, pattern, invert, speed, repeats):
        # Pattern for the LEDs
        patterns = {'spiral': [7, 6, 1, 3, 4, 5, 1, 2],
                    'circle': [7, 6, 5, 4, 3, 2]}
        for x in range(repeats):
            if invert:
                for i in range(len(patterns[pattern])):
                    self.set_single_pin(patterns[pattern][len(patterns[pattern]) - i])
                    time.sleep(speed)
            else:
                for i in range(len(patterns[pattern])):
                    self.set_single_pin(pattern[i])
                    time.sleep(speed)
