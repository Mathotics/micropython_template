'''
    blink.py

    blinks the LED on a raspberry pi pico 5 times
'''

from machine import Pin # Required for connecting to the Pins on the microcontroller
import time # Required for putting the thread to sleep

p = Pin(25, Pin.OUT) # Connect to the LED on the rasppi

def blink(max):
    i = 0 # 
    while (max > i):
        p.value(1) # Turn on the LED
        time.sleep(0.5) # Pause for 0.5 seconds
        p.value(0) # Turn off the LED
        time.sleep(0.5) # Pause for 0.5 seconds
        i +=1

blink(5) # Blink the LED 5 times