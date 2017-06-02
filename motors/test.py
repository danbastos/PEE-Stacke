#Authors: Daniel Bastos, Rui Oliveira, Joao Resende

import RPi.GPIO as GPIO
from time import sleep

#Codigo funcional
GPIO.setmode(GPIO.BCM)

MotorAIN1 = 6  #pino 11 na RPi
MotorAIN2 = 13  #pino 12 na RPi
MotorAPWM = 19  #pino 15 na RPi
MotorSTBY = 26  #pino 16 na RPi
    

#Pins configured as output
GPIO.setup(MotorAIN1,GPIO.OUT)
GPIO.setup(MotorAIN2,GPIO.OUT)
GPIO.setup(MotorSTBY,GPIO.OUT)
GPIO.setup(MotorAPWM, GPIO.OUT)
pwm = GPIO.PWM(19, 100)

counts = 0
Encoder_1 = 14
Encoder_2 = 15
GPIO.setup(Encoder_1,GPIO.IN)
GPIO.setup(Encoder_2,GPIO.IN)
Encoder_A_old = GPIO.input(Encoder_1)
Encoder_A = GPIO.input(Encoder_1)
Encoder_B_old = GPIO.input(Encoder_2)
Encoder_B = GPIO.input(Encoder_2)

# Initialize the interrupts - these trigger on the both the rising and falling 
#GPIO.add_event_detect('P8_7', GPIO.BOTH, callback = encodercount)   # Encoder A
#GPIO.add_event_detect('P8_8', GPIO.BOTH, callback = encodercount)   # Encoder B

    # This is the part of the code which runs normally in the background






while True:
    pwm.start(100)
    print "Turning motor on, PWM 100%"
    GPIO.output(MotorSTBY,1)
    GPIO.output(MotorAIN1,1)
    GPIO.output(MotorAIN2,0)
    GPIO.output(MotorAPWM,1)


    if ((Encoder_A,Encoder_B_old) == (1,0)) or ((Encoder_A,Encoder_B_old) == (0,1)):
        # this will be clockwise rotation
        counts += 1
        print 'Encoder count is %s\nAB is %s %s' % (counts, Encoder_A, Encoder_B)

    elif ((Encoder_A,Encoder_B_old) == (1,1)) or ((Encoder_A,Encoder_B_old) == (0,0)):
    # this will be counter-clockwise rotation
        counts -= 1
        print 'Encoder count is %s\nAB is %s %s' % (counts, Encoder_A, Encoder_B)

    else:
    #this will be an error
        error += 1
        print 'Error count is %s' %error

    Encoder_A_old,Encoder_B_old = Encoder_A,Encoder_B
    sleep(0.1)
    print 'Encoder count is %s\nAB is %s %s' % (counts, Encoder_A, Encoder_B)

    #GPIO.output(MotorSTBY,0)
    #GPIO.cleanup()



#pwm.start(50)    

#print "Turning motor on, PWM 50%"
#GPIO.output(MotorSTBY,1)
#GPIO.output(MotorAIN1,1)
#GPIO.output(MotorAIN2,0)
#GPIO.output(MotorAPWM,1)
#sleep(5)


#pwm.start(100)    

print "Turning motor on, PWM 100%"
GPIO.output(MotorSTBY,1)
GPIO.output(MotorAIN1,1)
GPIO.output(MotorAIN2,0)
GPIO.output(MotorAPWM,1)
sleep(5)

print "Stopping motor"

#PWM e standby funcionam

#pwm.stop()
#GPIO.output(MotorAPWM,0)
GPIO.output(MotorSTBY,0)

GPIO.cleanup()

