import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
MotorControl_Right = 15  #AIN1 - motor direitos
MotorControl2_Right = 18  #AIN2 - motor direitos
MotorsPWM_Right = 14  #PWM de controlo da direita
MotorControl_Left = 27  #AIN1 - motores esquerdos
MotorControl2_Left = 22  #AIN2 - motores esquedos
MotorsPWM_Left = 17  #PWM de controlo da esquerda 
MotorsSTBY = 24  #Standby (Decide se todos os motores estao ligados ou desligados)
    

GPIO.setup(MotorsSTBY,GPIO.OUT)

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

def my_callback(Encoder_Right_Front):
    return

GPIO.add_event_detect(Encoder_Right_Front, GPIO.RISING, callback=my_callback)

def Move(distance):
    count = 0
    countfinal = 1768.3466*distance
    GPIO.output(MotorsSTBY,1)
    GPIO.output(MotorControl_Right,1)
    GPIO.output(MotorControl2_Right,0)
    GPIO.output(MotorsPWM_Right,1)
    pwm_Motors_Right.start(100)
    GPIO.output(MotorControl_Left,1)
    GPIO.output(MotorControl2_Left,0)
    GPIO.output(MotorsPWM_Left,1)
    pwm_Motors_Left.start(100)
    print "Turning motor on, PWM 100%"
    GPIO.input(Encoder_Right_Front)
    while(count <= countfinal):
        if GPIO.event_detected(Encoder_Right_Front):
            count = count + 1
            print 'Count is: ', count
    print 'Moved: ', distance
    #desligar todos os motores
    GPIO.output(MotorsSTBY,0)
    GPIO.output(MotorControl_Right,0)
    GPIO.output(MotorControl2_Right,0)
    GPIO.output(MotorsPWM_Right,0)
    GPIO.output(MotorControl_Left,0)
    GPIO.output(MotorControl2_Left,0)
    GPIO.output(MotorsPWM_Left,0)
    sleep(5)


def Rotate180Degrees():
    GPIO.output(MotorControl_Right,0)
    GPIO.output(MotorControl2_Right,1)
    GPIO.output(MotorControl_Left,1)
    GPIO.output(MotorControl2_Left,0)
    GPIO.output(MotorsPWM_Left,1)
    GPIO.output(MotorsPWM_Right,1)
    pwm_Motors_Right.start(100)
    pwm_Motors_Left.start(100)
    GPIO.output(MotorsSTBY,1)
    sleep(2*1.6)  #este valor deve ser ajustado depois com toda a carga
    #pode ser determinado com os encoders de forma prática qual o valor para virar o desejado

    #desligar todos os motores
    GPIO.output(MotorsSTBY,0)
    GPIO.output(MotorControl_Right,0)
    GPIO.output(MotorControl2_Right,0)
    GPIO.output(MotorsPWM_Right,0)
    GPIO.output(MotorControl_Left,0)
    GPIO.output(MotorControl2_Left,0)
    GPIO.output(MotorsPWM_Left,0)


def Rotate90DegreesLeft():
    GPIO.output(MotorControl_Right,1)
    GPIO.output(MotorControl2_Right,0)
    GPIO.output(MotorControl_Left,0)
    GPIO.output(MotorControl2_Left,1)
    GPIO.output(MotorsPWM_Left,1)
    GPIO.output(MotorsPWM_Right,1)
    pwm_Motors_Right.start(100)
    pwm_Motors_Left.start(100)
    GPIO.output(MotorsSTBY,1)
    sleep(1.6)  #este valor deve ser ajustado depois com toda a carga
    #pode ser determinado com os encoders de forma prática qual o valor para virar o desejado

    #desligar todos os motores
    GPIO.output(MotorsSTBY,0)
    GPIO.output(MotorControl_Right,0)
    GPIO.output(MotorControl2_Right,0)
    GPIO.output(MotorsPWM_Right,0)
    GPIO.output(MotorControl_Left,0)
    GPIO.output(MotorControl2_Left,0)
    GPIO.output(MotorsPWM_Left,0)

def Rotate90DegreesRight():
    GPIO.output(MotorControl_Right,0)
    GPIO.output(MotorControl2_Right,1)
    GPIO.output(MotorControl_Left,1)
    GPIO.output(MotorControl2_Left,0)
    GPIO.output(MotorsPWM_Left,1)
    GPIO.output(MotorsPWM_Right,1)
    pwm_Motors_Right.start(100)
    pwm_Motors_Left.start(100)
    GPIO.output(MotorsSTBY,1)
    sleep(1.6)  #este valor deve ser ajustado depois com toda a carga
    #pode ser determinado com os encoders de forma prática qual o valor para virar o desejado

    #desligar todos os motores
    GPIO.output(MotorsSTBY,0)
    GPIO.output(MotorControl_Right,0)
    GPIO.output(MotorControl2_Right,0)
    GPIO.output(MotorsPWM_Right,0)
    GPIO.output(MotorControl_Left,0)
    GPIO.output(MotorControl2_Left,0)
    GPIO.output(MotorsPWM_Left,0)


while True:

    #Move(0.5)
    Rotate90DegreesRight()
    print "Rodou 90 graus, supostamente"
    sleep(3)
    #stop motors
    GPIO.cleanup()
