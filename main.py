import serial
import time
import sys

ser = serial.Serial("/dev/ttyS0", 115200, timeout=1)
print("Bridge actif", flush=True)

while True:
    if ser.in_waiting:
        line = ser.readline().decode().strip()
        print("Reçu:", line, flush=True)

    ser.write(b"LED_ON\n")
    print("Envoyé LED_ON", flush=True)
    time.sleep(5)

    ser.write(b"LED_OFF\n")
    print("Envoyé LED_OFF", flush=True)
    time.sleep(5)
