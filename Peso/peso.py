import RPi.GPIO as GPIO
import time
import statistics



class HX711:
    def __init__(self, dout=5, pd_sck=6, gain=128, bitsToRead=24):
        self.PD_SCK = pd_sck
        self.DOUT = dout

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PD_SCK, GPIO.OUT)
        GPIO.setup(self.DOUT, GPIO.IN)

        self.GAIN = 0
        self.REFERENCE_UNIT = 1 #The value returned by the hx711 that curresponds to your refenrence unit AFTER dividing by the SCALE.
                
        self.OFFSET = 1
        self.lastVal = 0
        self.butsToRead = bitsToRead
        self.twosComplementThreshold = 1 << (bitsToRead-1)
        self.twosComplementOffset =  -(1 << (bitsToRead))
        self.set_gain(gain)
        self.read()
        

    def is_ready(self):
        return GPIO.input(self.DOUT) == 0

    def set_gain(self, gain):
        if gain is 128:
            self.GAIN = 1
        elif gain is 64:
            self.GAIN = 3
        elif gain is 32:
            self.GAIN = 2

        GPIO.output(self.PD_SCK, False)
        self.read()

    def waitForReady(self):
        while not self.isReady():
            pass

    def correctTwosComplement(self, unsignedValue):
        if unsignedValue >= self.twosComplementThreshold:
            return unsignedValue + self.twos.ComplementOffset
        else:
            return unsignedValue

    ##falta codigo aqui ainda....
        
    def read_average(self, times=3):
        values = long(0)
        for i in range(times):
            values += self.read_long()
        return values/times

    def get_value(self, times=3):
        return self.read_average(times) - self.OFFSET

    def get_weight(self, times=3):
        value = self.get_value(times)
        value = value / self.REFERENCE_UNIT
        return value
    

    def tare(self, times=15):
        #backup REFERENCE_UNIT value
        reference_unit = self.REFERENCE_UNIT
        self.set_reference_unit(1)
        value = self.read_average(times)
        self.set_offset(value)
        self.set_reference_unit(reference_unit)

    def set_scale(self, scale):
        self.SCALE = scale

    def set_offset(self, offset):
        self.OFFSET = offset

    def power_down(self):
        GPIO.output(self.PD_SCK, False)
        GPIO.output(self.PD_SCK, True)

    def power_up(self):
        GPIO.output(self.PD_SCK, False)

#######Example

hx = HX711(9,11)
hx.set_scale(7050)
hx.tare()

while True:
    try:
        val = hx.get_units(3)
        if val > 100:
            print("OH NO")
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
