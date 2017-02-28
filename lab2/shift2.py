# dependencies
import RPi.GPIO as GPIO
import time

# Port numbering
GPIO.setmode(GPIO.BCM)

# define pins
data_pin = 16
latch_pin = 12
clock_pin = 6

GPIO.setup(data_pin, GPIO.OUT)
GPIO.setup(latch_pin, GPIO.OUT, initial=0)
GPIO.setup(clock_pin, GPIO.OUT, initial=0)

numbers = [
    int('01111110', 2),
    int('00110000', 2),
    int('01101101', 2),
    int('01111001', 2),
    int('00110011', 2),
    int('01011011', 2),
    int('01011111', 2),
    int('01110000', 2),
    int('01111111', 2),
    int('01111011', 2)
]


# Function to toggle latch/clock pins
def toggle(pin):
    GPIO.output(pin, 1)
    time.sleep(0)
    GPIO.output(pin, 0)


# Function to set number
def set_value(byte_val):
    for i in range(8):
        GPIO.output(data_pin, byte_val & (1 << i) == 0)
        toggle(clock_pin)
        
    toggle(latch_pin)

for val in numbers:
    set_value(val)
    time.sleep(1)
#set_value(numbers[5])

GPIO.cleanup()