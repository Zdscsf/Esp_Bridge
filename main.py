import serial
import time
import sys

ser = serial.Serial("/dev/ttyS0", 115200, timeout=1)
print("Bridge actif", flush=True)

time.sleep(2)  # laisse le temps à l'ESP32 de démarrer

while True:
    try:
        if ser.in_waiting:
            line = ser.readline().decode().strip()
            print("Reçu:", line, flush=True)
    except Exception as e:
        print("Erreur lecture:", e, flush=True)

    try:
        ser.write(b"LED_ON\n")
        print("Envoyé LED_ON", flush=True)
        time.sleep(0.5)

        ser.write(b"LED_OFF\n")
        print("Envoyé LED_OFF", flush=True)
        time.sleep(0.5)
    except Exception as e:
        print("Erreur écriture:", e, flush=True)

