import time
import sys

print("Bridge actif", flush=True)

while True:
    try:
        # Simulation d'envoi LED_ON / LED_OFF
        print("Envoyé LED_ON", flush=True)
        time.sleep(2)
        print("Envoyé LED_OFF", flush=True)
        time.sleep(2)
    except KeyboardInterrupt:
        print("Arrêt du bridge", flush=True)
        break
