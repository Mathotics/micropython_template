import network
import socket

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

while not sta_if.isconnected():
    print("Trying to connect...")
    sta_if.active(True)
    sta_if.connect('KMART', 'redbull1')

print("Connected")

addr_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)

addr = addr_info[0][-1]
s = socket.socket()
s.connect(addr)


while True:
    data = s.recv(500)
    print(str(data, 'utf8'), end='')
    if data == "\0":
        break