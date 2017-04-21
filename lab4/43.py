import RPi.GPIO as GPIO
import multiprocessing
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


class Pulser(multiprocessing.Process):
    def __init__(self, pin):
        multiprocessing.Process.__init__(self)
        self.pin = pin

    def run(self):
        min_power = 1
        max_power = 100
        fade_led = GPIO.PWM(self.pin, min_power)
        fade_led.start(0)
        for duty_cycle in range(min_power, max_power + 1):
            fade_led.ChangeDutyCycle(duty_cycle)
            time.sleep(.5/202)
        for duty_cycle in range(min_power, max_power + 1):
            fade_led.ChangeDutyCycle(max_power - duty_cycle)
            time.sleep(.5/202)


def forward():
    LEDS = [Pulser(led[0]), Pulser(led[1]), Pulser(led[2]), Pulser(led[3]), Pulser(led[4])]
    for i in LEDS:
        i.start()
        time.sleep(.1)
    #for i in LEDS:
        #i.join()


def backward():
    LEDS = [Pulser(led[4]), Pulser(led[3]), Pulser(led[2]), Pulser(led[1]), Pulser(led[0])]
    for i in LEDS:
        i.start()
        time.sleep(.1)
    #for i in LEDS:
        #i.join()


while True:
    forward()
    #backward()
