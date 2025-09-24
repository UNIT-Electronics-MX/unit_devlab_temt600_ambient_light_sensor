# Ambient Light Sensor Example

This guide explains how to use a TEMT6000 ambient light sensor with an Arduino-compatible board (such as the Pulsar ESP32 C6) or a MicroPython-compatible board (such as the DualMCU) to detect light and display its status via the Serial Monitor.

---

## Hardware Requirements

- **Microcontroller Board:** ESP32 or compatible
- **Sensor:** TEMT6000 Qwiic Ambient Light Sensor
- **Cabling:** JST connector

## Wiring Instructions

- **VCC**: Connect to **5 V** (match your board’s logic level)
- **GND**: Connect to **GND** (common ground)
- **SIG**: Connect to **GPIO12** (digital input on the microcontroller)

## Software Setup

1. **Install** the Arduino IDE or Thonny IDE.
2. **Create a new project** and paste the code from `light_sensor.ino` (Arduino) or `light_sensor.py` (MicroPython).
3. **Upload** the code to your board.
4. **Open the Serial Monitor** at **115200** baud to view sensor output.

## How to Use

1. **Power up** the board with the uploaded code.
2. **Check the Serial Monitor** for messages:
  - If light is detected:
    ```
    🔆 Light detected (HIGH)
    ```
  - If no light is detected:
    ```
    🌑 No light (LOW)
    ```
3. **Testing:**
  - Shine a flashlight or lamp on the sensor to trigger the "HIGH" message.
  - Cover the sensor to trigger the "LOW" message.

## Troubleshooting

- **Sensor always reads LOW:**
  - Confirm `SIG` is connected to GPIO12.
  - Ensure the sensor is powered (VCC and GND connected).

- **Sensor always reads HIGH:**
  - The sensor may be exposed to constant light; try testing in a darker area.
  - Check for wiring issues such as floating or pulled-up pins.

- **No output in Serial Monitor:**
  - Verify the Serial Monitor is set to **115200** baud.
  - Ensure the code initializes serial communication at the same baud rate.

---

## Technical Notes

- The TEMT6000 outputs an analog voltage proportional to light intensity. Reading this value requires an ADC-capable pin.
- On ESP32, not all pins support ADC. Common ADC pins include GPIO34, GPIO35, GPIO36, and GPIO39. Check your board’s documentation to ensure compatibility.
- On RP2040 (Raspberry Pi Pico), only GPIO26–28 support ADC.
- Functions like `atten()` and `width()` are specific to ESP32; they are ignored on other platforms.

---

### License & Credits

- **Code:** MIT License
- **Sensor:** TEMT6000 Ambient Light Sensor
- **Developed by:** UNIT Electronics

