import RPi.GPIO as GPIO
from leddisplay import LEDdisplay
import time


# Create led display object
the_LEDdisplay = LEDdisplay(16, 12, 6)

# Spam random combinations
for i in range(100):
    the_LEDdisplay.set_random_pins()
    time.sleep(.01)

the_LEDdisplay.patterns('spiral', False, .2, 1)
the_LEDdisplay.patterns('circle', False, .2, 1)
the_LEDdisplay.patterns('spiral', True, .2, 1)
the_LEDdisplay.patterns('circle', True, .2, 1)

for i in range(len(the_LEDdisplay.numbers)):
    the_LEDdisplay.set_number(i)
    time.sleep(.1*i + .2)

# cleanup
GPIO.cleanup()
