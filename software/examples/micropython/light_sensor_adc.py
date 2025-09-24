from machine import Pin, ADC
import time

# Configure GPIO6 as ADC input (ESP32C6)
light_sensor = ADC(Pin(6))

# Depending on your board, you may need to set attenuation for higher voltage range
# For ESP32: attenuation can be 0db (0–1V), 2.5db (0–1.34V), 6db (0–2V), 11db (0–3.6V)
try:
    light_sensor.atten(ADC.ATTN_11DB)   # Full range ~3.6V
except:
    pass  # Some ports (like RP2040) don't need this

# Optionally set resolution (ESP32 defaults to 12 bits → values 0–4095)
try:
    light_sensor.width(ADC.WIDTH_12BIT)
except:
    pass

while True:
    value = light_sensor.read()  # Read raw ADC value
    voltage = value * 3.3 / 4095  # Convert to voltage (assuming 3.3V reference)
    
    print("Raw ADC:", value, "Voltage:", "{:.2f} V".format(voltage))
    time.sleep(0.5)
