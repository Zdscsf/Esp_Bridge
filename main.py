import serial
import time

print("Démarrage bridge sur /dev/ttyS0...")

ser = serial.Serial("/dev/ttyS0", 115200, timeout=1)
print("Bridge actif")

while True:
    if ser.in_waiting:
        line = ser.readline().decode().strip()
        print("Reçu:", line)

    ser.write(b"LED_ON\n")
    print("Envoyé LED_ON")
    time.sleep(5)

    ser.write(b"LED_OFF\n")
    print("Envoyé LED_OFF")
    time.sleep(5)
