from machine import Pin
import time

# --- DIGITAL INPUT CONFIGURATION ---
# Use GPIO12 as a digital input with internal pull-down
sensor_digital = Pin(12, Pin.IN, Pin.PULL_DOWN)

print("Reading Qwiic module in digital mode (GPIO12)...")

while True:
    state = sensor_digital.value()  # 0 = LOW, 1 = HIGH
    if state:
        print("🔆 Light detected (HIGH)")
    else:
        print("🌑 No light (LOW)")
    time.sleep(0.5)

