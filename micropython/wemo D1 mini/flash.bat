esptool.py --port COM3 erase_flash
esptool.py --port COM3 --baud 460800 write_flash --flash_size=detect 0 esp8266-512k-20210902-v1.17.bin