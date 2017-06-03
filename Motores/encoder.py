#Authors: Daniel Bastos, Rui Oliveira, Joao Resende

import RPi.GPIO as GPIO
from time import sleep
from motor import *


GPIO.setmode(GPIO.BCM)
IRsensor = 4
MotorControl_Right = 15  #AIN1 - motor direitos
MotorControl2_Right = 18  #AIN2 - motor direitos
MotorsPWM_Right = 14  #PWM de controlo da direita
MotorControl_Left = 27  #AIN1 - motores esquerdos
MotorControl2_Left = 22  #AIN2 - motores esquedos
MotorsPWM_Left = 17  #PWM de controlo da esquerda 
MotorsSTBY = 24  #Standby (Decide se todos os motores estao ligados ou desligados)
    
pwmRightDefault=99
pwmLeftDefault=100

GPIO.setup(MotorsSTBY,GPIO.OUT)
GPIO.setup(IRsensor, GPIO.IN)

#Pins configured as output to control right motors
GPIO.setup(MotorControl_Right,GPIO.OUT)
GPIO.setup(MotorControl2_Right,GPIO.OUT)
GPIO.setup(MotorsPWM_Right, GPIO.OUT)
pwm_Motors_Right = GPIO.PWM(MotorsPWM_Right, 100)

#Pins configured as output to control left motors
GPIO.setup(MotorControl_Left,GPIO.OUT)
GPIO.setup(MotorControl2_Left,GPIO.OUT)
GPIO.setup(MotorsPWM_Left, GPIO.OUT)
pwm_Motors_Left = GPIO.PWM(MotorsPWM_Left, 100)

#Pin 10 configured to detect rising edge
Encoder_Right_Front = 10
GPIO.setup(Encoder_Right_Front,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Encoder 2
Encoder_Left_Front = 11
GPIO.setup(Encoder_Left_Front,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def my_callback(Encoder_Right_Front):
    return

GPIO.add_event_detect(Encoder_Right_Front, GPIO.RISING, callback=my_callback)

def left_callback(Encoder_Left_Front):
    return

GPIO.add_event_detect(Encoder_Left_Front, GPIO.RISING, callback=left_callback)


def Tilt(Error):
    #Error [-3,3]
    global pwmRight
    global pwmLeft
    pwmErrorScaling=1   #scale 

    if Error < 0 and Error>=-3:
        pwmRight+=Error*pwmErrorScaling      #if the robot tilts to the left the pwm of the right motors are less

    elif Error>0 and Error<=3:
        pwmLeft-=Error*pwmErrorScaling
    else:
        #caso o erro seja igual a 0, o pwm nos motores passa a ser o default
        pwmRight=pwmRightDefault 
        pwmLeft=pwmLeftDefault
        return pwmRight,pwmLeft

    return pwmRight,pwmLeft

def Move(delay,Error):
    #Move for a time given by delay
    Tilt(Error)
    RightMotors(1,pwmRight)
    LeftMotors(1,pwmLeft)
    GPIO.output(MotorsSTBY,1)
    sleep(delay)
    TurnOffMotors()


def Forward(distance):
    count = 0
    countfinal = 430*distance
    RightMotors(1,99)
    LeftMotors(1,100)
    GPIO.output(MotorsSTBY,1)
    print "Turning motor on, PWM 100%"
    GPIO.input(Encoder_Right_Front)
    GPIO.input(Encoder_Left_Front)
    while(count <= countfinal):
        while(not GPIO.event_detected(Encoder_Right_Front)):
            sleep(0.000001)
        while(not GPIO.event_detected(Encoder_Left_Front)):
            sleep(0.000001)
            
        count = count + 1
    print 'Moved: ', distance
    #desligar todos os motores
    TurnOffMotors()


def Backwards(distance):
    count = 0
    countfinal = 430*distance
    IRcurrent = GPIO.input(IRsensor)
    #print 'GPIO pin: ', IRcurrent
    IRprevious = IRcurrent
    RightMotors(0,99)
    LeftMotors(0,100)
    GPIO.output(MotorsSTBY,1)
    print "Turning motor on, PWM 100%"
    GPIO.input(Encoder_Right_Front)
    GPIO.input(Encoder_Left_Front)
    while(count <= countfinal):
        while(not GPIO.event_detected(Encoder_Right_Front)):
            sleep(0.000001)
        while(not GPIO.event_detected(Encoder_Left_Front)):
            sleep(0.000001)
           
        count = count + 1
        IRcurrent = GPIO.input(IRsensor)
        if IRcurrent:
            GPIO.output(MotorsSTBY,1)
            IRprevious = IRcurrent
        else:
            GPIO.output(MotorsSTBY,0)
            while(not IRcurrent):
                IRcurrent = GPIO.input(IRsensor)
                sleep(0.000001)
            GPIO.output(MotorsSTBY,1)
            
    #desligar todos os motores
    TurnOffMotors()

def Rotate180DegreesRight():
    count = 0
    countfinal = 769
    RightMotors(0,80)
    LeftMotors(1,80)
    GPIO.output(MotorsSTBY,1)
    GPIO.input(Encoder_Left_Front)
    while(count <= countfinal):
        while(not GPIO.event_detected(Encoder_Left_Front)):
            sleep(0.000001)
        count = count + 1

    #desligar todos os motores
    TurnOffMotors()

def Rotate180DegreesLeft():
    count = 0
    countfinal = 400
    RightMotors(1,80)
    LeftMotors(0,80)
    GPIO.output(MotorsSTBY,1)
    GPIO.input(Encoder_Right_Front)
    while(count <= countfinal):
        while(not GPIO.event_detected(Encoder_Right_Front)):
            sleep(0.000001)
        count = count + 1
            
    #desligar todos os motores
    TurnOffMotors()


def Rotate90DegreesLeft():
    count = 0
    countfinal = 190
    RightMotors(1,80)
    LeftMotors(0,80)
    GPIO.output(MotorsSTBY,1)
    GPIO.input(Encoder_Right_Front)
    while(count <= countfinal):
        while(not GPIO.event_detected(Encoder_Right_Front)):
            sleep(0.000001)
        count = count + 1
            
    #desligar todos os motores
    TurnOffMotors()

def Rotate90DegreesRight():
    count = 0
    countfinal = 225
    RightMotors(0,80)
    LeftMotors(1,80)
    GPIO.output(MotorsSTBY,1)
    GPIO.input(Encoder_Left_Front)
    while(count <= countfinal):
        while(not GPIO.event_detected(Encoder_Left_Front)):
            sleep(0.000001)
        count = count + 1

    #desligar todos os motores
    TurnOffMotors()


def Rotate(degrees, direction):
    count = 0
    #countfinal = 3.241*degrees
    countfinal = 1.55*degrees
    if direction == 0:  #rotacao para a direita
        GPIO.output(MotorControl_Right,1)
        GPIO.output(MotorControl2_Right,0)
        GPIO.output(MotorControl_Left,0)
        GPIO.output(MotorControl2_Left,1)
        GPIO.output(MotorsPWM_Left,1)
        GPIO.output(MotorsPWM_Right,1)
        pwm_Motors_Right.start(75)
        pwm_Motors_Left.start(75)
        GPIO.output(MotorsSTBY,1)
        GPIO.input(Encoder_Left_Front)
        while(count <= countfinal):
            while(not GPIO.event_detected(Encoder_Left_Front)):
                sleep(0.000001)
            count = count + 1
            #print 'Count is: ', count
    elif direction == 1:    #rotacao para a esquerda
        GPIO.output(MotorControl_Right,0)
        GPIO.output(MotorControl2_Right,1)
        GPIO.output(MotorControl_Left,1)
        GPIO.output(MotorControl2_Left,0)
        GPIO.output(MotorsPWM_Left,1)
        GPIO.output(MotorsPWM_Right,1)
        pwm_Motors_Right.start(75)
        pwm_Motors_Left.start(75)
        GPIO.output(MotorsSTBY,1)
        GPIO.input(Encoder_Right_Front)
        while(count <= countfinal):
            while(not GPIO.event_detected(Encoder_Right_Front)):
                sleep(0.000001)
            count = count + 1
                #print 'Count is: ', count
    else:
        return
    #desligar todos os motores
    print 'Count is: ', count
    GPIO.output(MotorsSTBY,0)
    GPIO.output(MotorControl_Right,0)
    GPIO.output(MotorControl2_Right,0)
    GPIO.output(MotorsPWM_Right,0)
    GPIO.output(MotorControl_Left,0)
    GPIO.output(MotorControl2_Left,0)
    GPIO.output(MotorsPWM_Left,0)
    

#while True:

    #Forward(0.5)	#distance to move given in meters
    #sleep(1)
    #Rotate90DegreesRight()
    #sleep(2)
    #Forward(0.3)
    #sleep(1)
    #Rotate90DegreesLeft()
    #sleep(1)
    #BackWards(0.5)
    #sleep(1)
    #Rotate180DegreesRight()
    #sleep(1)
    #Rotate180DegreesLeft()
    #sleep(1)
    #Forward(1)
    #sleep(2)
    #Rotate(90, 0)
    #rodar para a esquerda, segundo argumento 0
    #rodar para a direita, segundo argumento 1
    #print "Rodou 90 graus, supostamente"
    #BackWards(0.3)
    #sleep(1)
    #stop motors
    #GPIO.cleanup()
