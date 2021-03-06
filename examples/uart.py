# Example using UART communication protocol

'''
IMPORTANT:  To run this code, you need to wire GP4 to GP9 and GP8 to GP5
The USB (or some debugging message) must also be attached
'''
from machine import Pin # Required for connecting to the Pins
from machine import UART # Required for using UART
import time

uart0 = UART(1, baudrate=9600, tx= Pin(4), rx=Pin(5))
uart1 = UART(1, baudrate=9600, tx= Pin(8), rx=Pin(9))

uart0.write('Hello World')  # Write 12 bytes

time.sleep(0.01) # From testing, some time needs to pass before the UART Message registers to the recieve Pin

print(uart1.read(12)) # Read the first 12 bytes and print the message

uart1.write('Bye') # Send 'Bye' 

time.sleep(0.01) # From testing, some time needs to pass before the UART message registers to the recieve Pin

print(uart0.read(4)) # Read the first 4 bytes and print the message