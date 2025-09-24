# Getting Started with the TEMT6000 Ambient Light Sensor

This guide provides instructions on how to use the TEMT6000 ambient light sensor with an Arduino-compatible board (like the Pulsar ESP32 C6) or a MicroPython-compatible board (like the DualMCU) to detect ambient light levels and display the results via the Serial Monitor.

---

## Hardware Requirements

- **Microcontroller Board:** ESP32 or compatible
- **Sensor:** TEMT6000 Ambient Light Sensor
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

    - Cover the sensor to simulate darkness.
    - Shine a light on the sensor to simulate brightness.
    - Observe changes in the Serial Monitor output.

## Troubleshooting
- **No Output in Serial Monitor:**
    - Ensure the correct COM port is selected.
    - Verify baud rate is set to 115200.
- **Incorrect Readings:**
    - Check wiring connections.
    - Ensure the sensor is receiving power.
- **Sensor Not Responding:**
    - Test with a different GPIO pin.   
- **Board Not Recognized:**
    - Install necessary drivers for your microcontroller board.
## Additional Resources
- [Arduino IDE](https://www.arduino.cc/en/software)
- [Thonny IDE](https://thonny.org/)
- [TEMT6000 Datasheet](https://www.vishay.com/docs/84374/temt6000.pdf)
- [MicroPython Documentation](https://docs.micropython.org/en/latest/)
- [ESP32 Documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
## License
This project is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for details.