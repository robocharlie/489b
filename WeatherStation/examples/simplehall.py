import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

hall = 17

GPIO.setup(hall, GPIO.IN, pull_up_down=GPIO.PUD.up)


def my_callback(channel):
    print 'detected'

GPIO.add_event_detect(hall, GPIO.FALLING, callback=my_callback)

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
