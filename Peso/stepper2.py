#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
from hx711 import HX711
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO signals to use
# Physical pins 11,15,16,18
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
 
enable_pin = 9
coil_A_1_pin = 13
coil_A_2_pin = 12
coil_B_1_pin = 19
coil_B_2_pin = 26
 
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
 
GPIO.output(enable_pin, 1)

#choose pins on rpi(BCM5 and BCM6)
hx = HX711(dout=2, pd_sck=3)

hx.setReferenceUnit(21)

hx.reset()
hx.tare()

def forward(delay, steps):  
  for i in range(0, steps):
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        setStep(1, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 1)
        time.sleep(delay)
        
##        setStep(1, 0, 1, 0)
##        time.sleep(delay)
##        setStep(0, 1, 1, 0)
##        time.sleep(delay)
##        setStep(0, 1, 0, 1)
##        time.sleep(delay)
##        setStep(1, 0, 0, 1)
##        time.sleep(delay)
####
##      setStep(0, 1, 0, 1)
##      time.sleep(delay)
##      setStep(1, 0, 0, 1)
##      time.sleep(delay)
##      setStep(1, 0, 0, 1)
##      time.sleep(delay)
##      setStep(1, 0, 1, 0)
##      time.sleep(delay)
def backwards(delay, steps):  
  for i in range(0, steps):
    setStep(0, 1, 0, 1)
    #setStep(1, 0, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    #setStep(1, 0, 0, 1)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    #setStep(0, 1, 0, 1)
    time.sleep(delay)
    #setStep(0, 1, 1, 0)
    setStep(1, 0, 1, 0)
    time.sleep(delay)

def cleanup():
    #setSt
    #setStep(0, 1, 0, 1)
    setStep(0, 0, 0, 0)
    
  
def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)
 
while True:
  delay = raw_input("Delay between steps (milliseconds)?")
  steps = raw_input("How many steps forward? ")
  forward(int(delay) / 1000.0, int(steps))
  cleanup()
  steps = raw_input("How many steps backwards? ")
  backwards(int(delay) / 1000.0, int(steps))
  cleanup()
  
