#Authors: Daniel Bastos, Rui Oliveira, João Rezende

from gpiozero import OutputDevice
from time import sleep

a = OutputDevice(15)
b = OutputDevice(18)

for i in range(5):
    #motor on
    a.on()
    b.off()
    print("Forward")
    sleep(5)
    #other direction
    a.off()
    b.on()
    print("Backwards")
    sleep(5)

b.off()
