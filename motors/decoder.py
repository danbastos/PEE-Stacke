def encodercount(term):
global counts       
global Encoder_A
global Encoder_A_old
global Encoder_B
global Encoder_B_old
global error

Encoder_A,Encoder_B = GPIO.input('P8_7'),GPIO.input('P8_8')

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

# Initialize the interrupts - these trigger on the both the rising and falling 
GPIO.add_event_detect('P8_7', GPIO.BOTH, callback = encodercount)   # Encoder A
GPIO.add_event_detect('P8_8', GPIO.BOTH, callback = encodercount)   # Encoder B

# This is the part of the code which runs normally in the background
while True:
    time.sleep(1)
