#Authors: Daniel Bastos, Rui Oliveira, João Rezende

import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
StepPins = [12,13,19,26]
StepperSTBY = 9
GPIO.setup(StepperSTBY,GPIO.OUT)
GPIO.output(StepperSTBY, 1)

# Set all pins as output
for pin in StepPins:
  print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

# Define advanced sequence
# as shown in manufacturers datasheet
#Seq = [[1,0,0,1],
#       [1,0,0,0],
#       [1,1,0,0],
#       [0,1,0,0],
#       [0,1,1,0],
#       [0,0,1,0],
#       [0,0,1,1],
#       [0,0,0,1]]

Seq = [[1,1,0,0],
       [0,1,1,0],
       [0,0,1,1],
       [1,0,0,1]]

       
StepCount = len(Seq)
#StepDir = 1 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise


# Initialise variables
StepATM = 0
StepCounter = 0

def RotateLeft(StepIncrement):
    global StepCounter
    global StepATM
    global StepCount
    TotalSteps = StepATM + StepIncrement
    while(StepATM<TotalSteps):
      #print StepCounter,
      #print Seq[StepCounter]

      for pin in range(0,4):
        xpin=StepPins[pin]# Get GPIO
        if Seq[StepCounter][pin]!=0 and (StepPins[pin] == 12 or StepPins[pin] == 13) :
          #print " Enable GPIO %i" %(xpin)
          GPIO.output(xpin, True)
        else:
          GPIO.output(xpin, False)
      StepATM += 1
      StepCounter += 1
                       
      # If we reach the end of the sequence
      # start again
      if (StepCounter>=StepCount):
        StepCounter = 0
      if (StepCounter<0):
        StepCounter = StepCount+1
      time.sleep(0.01)


def RotateRight(StepDecrement):
    global StepCounter
    global StepATM
    global StepCount
    TotalSteps = StepATM - StepDecrement
    while(StepATM>TotalSteps):
      #print StepCounter,
      #print Seq[StepCounter]

      for pin in range(0,4):
        xpin=StepPins[pin]# Get GPIO
        if Seq[StepCounter][pin]!=0 and (StepPins[pin] == 19 or StepPins[pin] == 26) :
          #print " Enable GPIO %i" %(xpin)
          GPIO.output(xpin, True)
        else:
          GPIO.output(xpin, False)
      StepATM -= 1
      StepCounter += 1
                       
      # If we reach the end of the sequence
      # start again
      if (StepCounter>=StepCount):
        StepCounter = 0
      if (StepCounter<0):
        StepCounter = StepCount-1
      time.sleep(0.01)



#Neste codigo falta associar o numero de steps a distancia percorrida no barao roscado!!!

# Start main loop
while True:
  RotateRight(5000)
  time.sleep(3)
  RotateLeft(40)
  print StepATM
  time.sleep(3)
