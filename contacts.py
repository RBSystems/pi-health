#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN)

FLAG = 0

while (True):

    if (GPIO.input(18) == 1):
        print 'Projector Not Stolen'
    elif FLAG < 5:
        FLAG += 1
        print 'Contact Broken!', FLAG
    else:
        session = requests.session()
        session.get('http://dev-elk-shipper0:5546')

    time.sleep(2)

print 'Projector Stolen'


