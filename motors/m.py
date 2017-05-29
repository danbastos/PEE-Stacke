#Authors: Daniel Bastos, Rui Oliveira, João Rezende

from gpiozero import LED
from time import sleep

a = LED(17)
b = LED(18)

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

