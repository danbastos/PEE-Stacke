#!/usr/bin/env python2.7

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(7,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
    GPIO.wait_for_edge(7,GPIO.FALLING)
    print "\n End of course detected"
except KeyboardInterrupt:
    GPIO.cleanup()
