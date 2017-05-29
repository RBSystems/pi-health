#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import requests
import os
import datetime

def buildAlert():
    host = os.uname()[1]
    data = host.split('-')
    
    payload = {
            'building':data[0],
            'room':data[1],
            'cause':'SECURITY',
            'category':'INFO',
            'hostname':host,
            'timestamp':str(datetime.datetime.now())
            }

    return payload


GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN)

FLAG = 0

print os.uname()[1]

while (True):

    if (GPIO.input(18) == 1):
        print 'Projector Not Stolen'
    elif FLAG < 5:
        FLAG += 1
        print 'Contact Broken!', FLAG
    else:
        FLAG = 0
        address = 'http://dev-elk-shipper0.byu.edu:5546'
        payload = buildAlert()
        requests.post(address, data = payload)
        print 'Alert! Stolen Projector!'

    time.sleep(2)



