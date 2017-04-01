# empty file to start things
import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()

print 'Temp = {0:0.1f} *C'.format(sensor.read_temperature())
print 'Pressure = {0:0.1f} Pa'.format(sensor.read_pressure())
print 'Altitude = {0:0.1f} m'.format(sensor.read_altitude())