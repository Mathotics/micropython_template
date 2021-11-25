# Example for using interrupts with the raspberry pi pico

'''
Assuming this works, "IRQ with flags:" should be printed out when Pin(2) is set to low (or high? maybe?)
'''

from machine import Pin # Required for using the pins on the Raspberry Pi Pico

p2 = Pin(2, Pin.IN, Pin.PULL_UP) # Create the pin
p2.irq(lambda pin: print("IRQ with flags:", pin.irq().flags()), Pin.IRQ_FALLING) # 

for i in range(100):
    print("Iteration: {}".format(i))
    time.sleep(0.1) # Put the thread to sleep for 1/10 seconds