#!/usr/bin/python

import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (2592, 1944)
    # Camera warm-up time
    time.sleep(2)
    camera.capture('/data/image.jpg')

print 'Picture taken'
time.sleep(10)