import RPi.GPIO as GPIO
import time

button = 25
led = [4, 17, 18, 23, 24]
b_ltr = True
counter = 0
led_direction = 0  # 0 is left to right, 1 is right to left

GPIO.setmode(GPIO.BCM)

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


def my_callback(channel):
    b_ltr = not b_ltr
    print "swap"


def led_toggle(num):
    GPIO.output(led[num], 1)
    time.sleep(.5)
    GPIO.output(led[num], 0)


GPIO.add_event_detect(button, GPIO.FALLING, callback=my_callback)

try:
    while True:
        if b_ltr:
            try:
                led_toggle(counter)
                counter += 1
            except IndexError:
                counter = 0
        else:
            try:
                led_toggle(counter)
                counter -= 1
            except IndexError:
                counter = len(led) - 1
except KeyboardInterrupt:
    GPIO.cleanup()


