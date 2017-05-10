import RPi.GPIO as GPIO
import time

sensor = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)
current = GPIO.input(sensor)
previous = current
def printState(current):
    print 'GPIO pin %s is %s' % (sensor, 'Run, Forest, Run!!!' if current else 'Obstacle')
printState(current)
while True:
    current = GPIO.input(sensor)
    printState(current)
    previous = current
    time.sleep(0.1)
GPIO.cleanup()
