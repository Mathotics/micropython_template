# Example using Analog to Digital Converter

from machine import Pin # Required for accessing the GPIO Pins
from machine import ADC # Required for using the Analog to Digital Converter library
import time # Required for putting the thread to sleep

'''
IMPORTANT:
When using the Raspberry Pi Pico for analog to digital conversion, you must only use the pins that have been designated for ADC.

When wiring the Raspberry Pi Pico for analog to digital conversion, you must only use the GND pin that has been designated for ADC. It is labeled on the pinout diagram.
If you are using the Raspberry Pi Pico for analog to digial conversion, do not connect the GND pin that is designated for ADC with the other GND Pins.

The Raspberry Pi Pico ADC pins read a range from 0.0 - 3.3 V; do not use pass this voltage range. Use a voltage divider for higher voltages and extrapolate.

'''

adc = ADC(Pin(26)) # Create the ADC object on one of the ADC pins

adc = ADC(Pin(26))     # create ADC object on ADC pin

for _ in range(100):
    print(adc.read_u16()) # read value, 0-65535 across voltage range 0.0v - 3.3v
    time.sleep(0.1) # Put the thread to sleep for a tenth of a second