#include <Arduino.h>

const int SENSOR_PIN = 12;  // GPIO12 connected to the module’s digital output

void setup() {
  // Initialize Serial at 115200 baud
  Serial.begin(115200);
  while (!Serial) { }  // Wait for Serial (on some boards)

  // Configure GPIO12 as digital input with internal pull-down
  pinMode(SENSOR_PIN, INPUT_PULLDOWN);

  Serial.println("Reading Qwiic module in digital mode (GPIO12)...");
}

void loop() {
  int state = digitalRead(SENSOR_PIN);  // Read 0 (LOW) or 1 (HIGH)

  if (state == HIGH) {
    Serial.println("🔆 Light detected (HIGH)");
  } else {
    Serial.println("🌑 No light (LOW)");
  }

  delay(500);  // 0.5 second pause
}
