import RPi.GPIO as GPIO

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

def RightMotors(direction,pwm):
    if direction == 1:    # motores da direita a andar para a frente
        GPIO.output(MotorControl_Right,1)
        GPIO.output(MotorControl2_Right,0)

    elif direction == 0:  #motores da direita a andar para tras
        GPIO.output(MotorControl_Right,0)
        GPIO.output(MotorControl2_Right,1)
    else:
        return
    GPIO.output(MotorsPWM_Right,1)    
    pwm_Motors_Right.start(pwm)
    return

def LeftMotors(direction,pwm):
    if direction == 1:    # motores da direita a andar para a frente
        GPIO.output(MotorControl_Left,1)
        GPIO.output(MotorControl2_Left,0)
        
    elif direction == 0:  #motores da direita a andar para tras
        GPIO.output(MotorControl_Left,0)
        GPIO.output(MotorControl2_Left,1)
    else:
        return
    GPIO.output(MotorsPWM_Left,1)    
    pwm_Motors_Left.start(pwm)
    return

def TurnOffMotors():
    GPIO.output(MotorsSTBY,0)
    GPIO.output(MotorControl_Right,0)
    GPIO.output(MotorControl2_Right,0)
    GPIO.output(MotorsPWM_Right,0)
    GPIO.output(MotorControl_Left,0)
    GPIO.output(MotorControl2_Left,0)
    GPIO.output(MotorsPWM_Left,0)
    return

