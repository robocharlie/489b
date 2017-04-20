import RPi.GPIO as GPIO
import threading
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


class LedLoop(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def led_toggle(self, num, blink):
        GPIO.output(led[num], 1)
        time.sleep(blink)
        GPIO.output(led[num], 0)

    def run(self, direction):
        count = 0
        while True:
            if direction == 'right':
                try:
                    self.led_toggle(count, .2)
                    count += 1
                except IndexError:
                    count = 0
            else:
                try:
                    self.led_toggle(count, .15)
                    count -= 1
                except IndexError:
                    count = len(led) - 1

pattern1 = LedLoop()
pattern1.daemon = True
pattern1.run('right')

pattern2 = LedLoop()
pattern2.daemon = True
pattern2.run('left')

try:
    while True:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
