import RPi.GPIO as GPIO
import multiprocessing
import time

GPIO.setmode(GPIO.BCM)
pwm_pin = 24
GPIO.setup(pwm_pin, GPIO.OUT)

led_pin = 19
GPIO.setup(led_pin, GPIO.OUT)


class motorLoop(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)

    def run(self):
        min = 1
        max = 13
        pwm = GPIO.PWM(pwm_pin, 50)
        pwm.start(0)
        while True:
            for duty_cycle in range(min, max):
                pwm.ChangeDutyCycle(duty_cycle)
                print duty_cycle
                time.sleep(.5)


motor1 = motorLoop()
motor1.daemon = True
motor1.start()

while True:
    GPIO.output(led_pin, 1)
    print "ON"
    time.sleep(.8)
    GPIO.output(led_pin, 0)
    print "OFF"
    time.sleep(.8)

motor1.join()
