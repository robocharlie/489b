import RPi.GPIO as GPIO
from leddisplay import LEDdisplay
import time


# Create led display object
the_LEDdisplay = LEDdisplay(16, 12, 6)

# Spam random combinations
for val in range(100):
    the_LEDdisplay.set_random_pins()
    print(val)
    time.sleep(.01)

the_LEDdisplay.patterns('spiral', False, .2, 5)
the_LEDdisplay.patterns('circle', False, .2, 3)
the_LEDdisplay.patterns('spiral', True, .2, 5)
the_LEDdisplay.patterns('circle', True, .2, 3)

# cleanup
GPIO.cleanup()
