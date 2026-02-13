import serial
import time

ser = serial.Serial("/dev/ttyS0", 115200, timeout=1)
print("Bridge actif")

while True:
    print("Test log")
    time.sleep(5)
