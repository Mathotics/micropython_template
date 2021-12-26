import machine
import utime 

pin = machine.Pin(2, machine.Pin.OUT)

x = 0
while x < 10:
    x = x + 1
    pin.off()
    utime.sleep_ms(100)
    pin.on()
    utime.sleep_ms(100)