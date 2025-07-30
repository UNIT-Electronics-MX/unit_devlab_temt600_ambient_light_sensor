# Qwiic Light Sensor Digital Reader

This project demonstrates how to use an ambient light sensor in digital mode with an Arduino-compatible board (Pulsar ESP32 C6) or micropython-compatible board (DualMCU) to detect light presence and print its status via the Serial Monitor.

---

## Hardware Requirements

- **Board:** ESP32 
- **Sensor module:** TEMT6000 Qwiic Ambient Light Sensor
- **Cables:** JST connector

## Wiring

| Sensor Pin | Board Pin    | Notes                                 |
| ---------- | ------------ | ------------------------------------- |
| VCC        | 5 V          | According to your board’s logic level |
| GND        | GND          | Common ground                         |
| SIG        | GPIO12       | Connect to digital input on board     |

## Software Setup

1. **Install Arduino IDE or Thonny IDE**
2. **Open a new sketch** and paste the code from `light_sensor.ino` or `light_sensor.py` (provided).
3. **Upload** the sketch to your board.
4. **Open Serial Monitor** at **115200** baud to view output.

## Usage Instructions

1. **Power on** the board with the uploaded sketch running.
2. **Observe** the Serial Monitor:
   - When the sensor detects sufficient light, you should see:
     ```
     🔆 Light detected (HIGH)
     ```
   - In darkness or low light, you should see:
     ```
     🌑 No light (LOW)
     ```
3. **Test:**
   - Bring a flashlight or lamp close to the sensor’s photodiode.
   - Cover the sensor with your hand or block light to see the alternate message.

## Troubleshooting

- **Always reads LOW:**

  - Verify `SIG` is wired to GPIO12.
  - Ensure the sensor module is powered (VCC/GND).

- **Always reads HIGH:**

  - Sensor may be permanently illuminated by ambient light; test in darker environment.
  - Check for accidental pull-up or floating pin issues.

- **No Serial Output:**

  - Confirm Serial Monitor is at **115200** baud.
  - Ensure `Serial.begin(115200);` matches the monitor setting.

---

### License & Credits

- **Code**: MIT License
- **Sensor**: TEMT6000 Ambient Light Sensor
- **Developed by**: UNIT Electronics

