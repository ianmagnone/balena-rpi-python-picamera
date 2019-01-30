#!/usr/bin/python

import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (2592, 1944)
    # Camera warm-up time
    time.sleep(2)
    for filename in camera.capture_continuous('img{counter:03d}.jpg'):
	    print('Captured %s' % filename)
	    sleep(300) # wait 5 minutes
    # camera.capture('/data/image.jpg')

print 'Picture taken'
time.sleep(10)