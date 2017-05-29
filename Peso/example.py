#Authors: Daniel Bastos, Rui Oliveira, João Rezende

import sys
import time

import RPi.GPIO as GPIO
from hx711 import HX711

#choose pins on rpi(BCM5 and BCM6)
hx = HX711(dout=2, pd_sck=3)

hx.setReferenceUnit(21)

hx.reset()
hx.tare()

while True:
    try:
        val = hx.getWeight()
        print("{0: 4.4f}".format(val))

    except(KeyboardInterrupt, SystemExit):
        GPIO.cleanup()
        sys.exit()
