import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pwm_pin = 24
GPIO.setup(pwm_pin, GPIO.OUT)

min = 1
max = 13

pwm = GPIO.PWM(pwm_pin, 50)
pwm.start(0)

while(1):
    for duty_cycle in range(min, max):
        pwm.ChangeDutyCycle(duty_cycle)
        print duty_cycle
        time.sleep(.5)
