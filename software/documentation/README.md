---
title: "TEMT600 Ambient Light Sensor"
version: "1.0"
modified: "2025-04-30"
output: "temt600_ambient_light_sensor"
subtitle: "Compact module built around the TEMT600 phototransistor."
---

<!--
# README_TEMPLATE.md
This file serves as an input to generate a datasheet-style technical PDF.
Fill in each section without deleting or modifying the existing headings.
-->

# TEMT600 Ambient Light Sensor

![product](./images/top.png) <!-- FILL HERE: replace image if needed -->

## Introduction

<!-- FILL HERE -->
The **TEMT600 Ambient Light Sensor Development Board** is a compact module built around the Vishay TEMT600 phototransistor. It provides a linear analog voltage proportional to ambient light intensity, making it ideal for display back-light control, energy-saving systems, photographic exposure adjustment, and environmental monitoring.

## Functional Description
 
- **Linear Analog Output:** V<sub>OUT</sub> varies linearly with illuminance  
- **High Sensitivity:** Detects from near-dark (≪1 lx) up to bright sunlight (>10 k lx)    


## Electrical Characteristics & Signal Overview

<!-- FILL HERE -->
- **Wide Supply Range:** 3.3 V – 5 V
- **Low Quiescent Current:** ≈ 0.5 mA typical 

## Applications

<!-- FILL HERE -->
- Automatic display brightness adjustment  
- Photographic light metering  
- Smart home & IoT light sensing  
- Plant/garden lighting control  
- Wearable/light-level logging  
- Data-logging & environmental sensing

## Features

<!-- FILL HERE -->
- **Compact Footprint:** 20 × 12 mm PCB with 3 mm mounting hole  
- **Standard JST-PH Connector:** 3-pin plug-and-play  
- **RoHS-Compliant & Lead-Free**

## Pin & Connector Layout

| Group     | Available Pins | Suggested Use                          |
|-----------|----------------|----------------------------------------|
| GPIO      | <!-- FILL -->  | <!-- FILL -->                          |
| UART      | <!-- FILL -->  | <!-- FILL -->                          |
| TouchPad  | <!-- FILL -->  | <!-- FILL -->                          |
| Analog    | <!-- FILL -->  | <!-- FILL -->                          |
| SPI       | <!-- FILL -->  | <!-- FILL -->                          |

## Settings

### Interface Overview

| Interface  | Signals / Pins         | Typical Use                              |
|------------|------------------------|------------------------------------------|
| UART       | <!-- FILL -->          | <!-- FILL -->                             |
| I2C        | <!-- FILL -->          | <!-- FILL -->                             |
| SPI        | <!-- FILL -->          | <!-- FILL -->                             |
| USB        | <!-- FILL -->          | <!-- FILL -->                             |

### Supports

| Symbol | I/O         | Description                        |
|--------|-------------|------------------------------------|
| VCC    | Input       | <!-- FILL -->                      |
| GND    | GND         | <!-- FILL -->                      |
| IO     | Bidirectional | <!-- FILL -->                   |

## Block Diagram

![Function Diagram](images/pinout.png) <!-- FILL HERE: replace image if needed -->

## Dimensions

![Dimensions](../../hardware/resources/unit_dimension_V_0_0_1_ue0098_TEMT6000.png) <!-- FILL HERE: replace image if needed -->

## Usage

<!-- FILL HERE -->
Mention supported development platforms and toolchains 

- (e.g., Arduino IDE, ESP-IDF, PlatformIO, etc.)

## Downloads

<!-- FILL HERE -->
- [Schematic PDF](docs/schematic.pdf)
- [Board Dimensions DXF](docs/dimensions.dxf)
- [Pinout Diagram PNG](docs/pinout.png)

## Purchase

<!-- FILL HERE -->
- [Buy from vendor](https://example.com)
- [Product page](https://example.com/product/template-board)
