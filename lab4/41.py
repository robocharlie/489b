import RPi.GPIO as GPIO
import time

button = 4
led = [6, 8, 10, 12, 14]
b_ltr = True
counter = 0
led_direction = 0  # 0 is left to right, 1 is right to left

GPIO.setmode(GPIO.BCM)

GPIO.setup(button, GPIO.IN)
for i in led:
    GPIO.setup(led[i-1], GPIO.OUT)


def my_callback(channel):
    b_ltr = not b_ltr


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


