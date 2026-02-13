import serial
import time
import os

# Détecte automatiquement le port série disponible
if os.path.exists("/dev/serial0"):
    port = "/dev/serial0"
elif os.path.exists("/dev/ttyAMA0"):
    port = "/dev/ttyAMA0"
else:
    raise Exception("Aucun port série trouvé (/dev/serial0 ou /dev/ttyAMA0)")

print(f"Démarrage bridge sur {port}...")

ser = serial.Serial("/dev/ttyS0", 115200, timeout=1)
print("Bridge actif")

while True:
    if ser.in_waiting:
        line = ser.readline().decode().strip()
        print("Reçu:", line)

    # Exemple test automatique LED
    ser.write(b"LED_ON\n")
    print("Envoyé LED_ON")
    time.sleep(5)

    ser.write(b"LED_OFF\n")
    print("Envoyé LED_OFF")
    time.sleep(5)

