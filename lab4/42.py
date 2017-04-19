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


def led_toggle(num, blink):
    GPIO.output(led[num], 1)
    time.sleep(blink)
    GPIO.output(led[num], 0)

try:
    pass
except KeyboardInterrupt:
    GPIO.cleanup()
