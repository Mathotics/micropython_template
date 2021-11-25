import time # Required for putting the thread to sleep
import _thread # Required for starting another thread
import machine # Required for accessing the pins of the raspberry pi pico

def blink(n, delay):
    led = machine.Pin(25, machine.Pin.OUT)
    for i in range(n):
        led.high()
        time.sleep(delay)
        led.low()
        time.sleep(delay)
    print('done')

def send_messages(n, message, delay):
    for i in range(n):
        print(message)
        time.sleep(delay)

# If this works as expected, we should see blinking and the "Hello World" message appear at the same time
_thread.start_new_thread(blink, (10, 0.5))
_thread.start_new_thread(send_messages, (10, "Hello World", 0.5))
