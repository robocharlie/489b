# WeatherStation when run will collect data from the various sensors and
# output to thingspeak. A seperate html file can view the formatted data.
# Measure wind direction with photoencoder
# Measure wind speed with hall effect, counting ticks and time:
#       peak wind speed
#       average wind speed over a 1 min period
# Measure Temperature
# Measure Humidity
# Measure Pressure
# asynchronous data collection
# pump out every 16 seconds to thingspeak
# email/tweet/text if parameter goes out of set limits

# imports
import RPi.GPIO as GPIO
import time
import Adafruit_BMP.BMP085 as BMP
import Adafruit_DHT
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# set pin config
GPIO.setmode(GPIO.BCM)

# Assign pin numbers
hall = 17
dht_pin = 18
# led = 4
# h_port = 5

# Setup pins
GPIO.setup(hall, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(led, GPIO.OUT)

# SPI setup
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# DHT setup
dht = Adafruit_DHT.DHT11

# BMP
bmp = BMP.BMP085()

# time variables
DHT_delay = 1.5
last_time = time.time()


# Callback triggered whenever the hall effect sensors sees a mag.
def my_callback(channel):
    print '$$$$$$$$$$$$$$$There it goes!$$$$$$$$$$$$'

GPIO.add_event_detect(hall, GPIO.FALLING, callback=my_callback)

try:
    while True:
        if time.time() > last_time + DHT_delay:
            last_time = time.time()
            H, T = Adafruit_DHT.read_retry(dht, dht_pin)
            if H is not None and T is not None:
                print ''
                print 'T={0:0.1f}oC H={1:0.1f}%'.format(T, H)
                print('Temp = {0:0.2f} *C'.format(bmp.read_temperature()))
                print('Pressure = {0:0.2f} Pa'.format(bmp.read_pressure()))
                print('Altitude = {0:0.2f} m'.format(bmp.read_altitude()))
                print('Sealevel Pressure = {0:0.2f} Pa'.format(bmp.read_sealevel_pressure()))
                values = [0]*4
                print ''
                for i in range(4):
                    values[i] = mcp.read_adc(i)
                    print(values[i])
            else:
                print 'Failed dht reading'
        else:
            pass
except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()