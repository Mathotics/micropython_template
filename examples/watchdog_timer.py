
'''
The RP2040 has a watchdog which is a countdown timer that restarts parts of the chip if it reaches zero.

NOTE: If this code works as expected, the delay should never exceed the watchdog timer timeout period.
'''

from machine import WDT # Required for using the watchdog timer
import time # Required for putting the thread to sleep

print("Start")

# enable the WDT with a timeout of 5s (1s is the minimum)
wdt = WDT(timeout=5000)

delay = 0
while True:
    time.sleep(delay) # Put the thread to sleep for the delay period
    print("Delay: {}".format(delay))
    wdt.feed() # Reset the watchdog timer
    delay += 1 # Increase the delay by one second