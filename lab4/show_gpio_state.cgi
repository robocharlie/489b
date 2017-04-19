#!/usr/bin/python27all

# cgi script to show the state of a single gpio input pin

import RPi.GPIO as GPIO
import cgi
import cgitb
cgitb.enable()
inPort = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(inPort, GPIO.IN)

print "Content-type:text/html\n\n"
print '<html><body><font color="red">'
if GPIO.input(inPort)==0:
    print 'GPIO' + str(inPort) + ' is LOW'
elif GPIO.inpur(inPort)==1:
    print 'GPIO' + str(inPort) + ' is HIGH'
print '</body></html>cd '