# Example using PWM to dim and brighten an LED

import time # Required for putting the thread to sleep
from machine import Pin # Required for accessing the GPIO Pins
from machine import PWM # Required for using the PWM

# Create the PWM Object
pwm = PWM(Pin(25)) # Pin 25 is the led on the board

# Set the PWM frequency
pwm.freq(1000)

# Fade the LED in and out a few times
duty = 0 # The Duty cycle
direction = 1 # The direction that the LED is going (dim or brighten)

for _ in range(8 * 256):
    duty += direction # Assign the duty cycle
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.01) # Put the thread to sleep temporarily