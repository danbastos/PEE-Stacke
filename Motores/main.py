#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
from encoder import *
from motor import *
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)


End_Course = 7
GPIO.setup(End_Course,GPIO.IN, pull_up_down=GPIO.PUD_UP)

def my_callback(End_Course):
    return

GPIO.add_event_detect(End_Course, GPIO.FALLING, callback=my_callback)

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
 
def down(delay, steps,last):
    if last == 1:
          while(not GPIO.event_detected(End_Course)):
              setStep(1, 0, 0, 1)
              time.sleep(delay)
              setStep(1, 0, 1, 0)
              time.sleep(delay)
              setStep(0, 1, 1, 0)
              time.sleep(delay)
              setStep(0, 1, 0, 1)
              time.sleep(delay)
          cleanup()
          print "Fim de curso detetado"
          

    else:    
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
def up(delay, steps):  
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
  delay = 5
  Forward(0.1)
  sleep(3)
  up(int(delay) / 1000.0, int(500))
  cleanup()
  sleep(3)
  Backwards(0.5)
  sleep(3)
  Rotate90DegreesLeft()
  sleep(3)
  Forward(0.5)
  sleep(3)
  up(int(delay) / 1000.0, int(1000))
  cleanup()
  sleep(3)
  down(int(delay) / 1000.0, int(900),0)
  cleanup()
  sleep(3)
  Forward(0.5)
  sleep(3)
  Rotate90DegreesRight()
  sleep(3)
  Forward(0.5)
  sleep(3)
  down(int(delay) / 1000.0, int(1000),1)
  sleep(3)
  Backwards(0.3)
  sleep(3)
  
  GPIO.cleanup()
