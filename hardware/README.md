# Hardware
<div align="center">
    <a href="./unit_sch_V_0_0_1_ue0098_TEMT6000.pdf"><img src="resources/Schematics_icon.jpg?raw=false" width="450px" alt="Schematics"/><br/> Schematics</a>
</div>

---


## ⚙️ Technical Specifications
<div align="center">

| Pin | Symbol | Type     | Description                                                                 |
| :---: | :----- | :------- | :-------------------------------------------------------------------------- |
| 1     | GND    | Power    | Ground reference (connect to MCU GND)                                       |
| 2     | VCC    | Power    | +3.3 V to +5 V supply voltage                                               |
| 3     | D0     | Analog   | voltage ∝ ambient light; connect to an ADC input of your MCU |
</div>

> **Note:** Do not exceed 5 V on VCC. SIO swings between 0 V (dark) and VCC (bright).

## 🔌 Pinout

Include a diagram like `docs/pinout.png` or describe functionally:
<div align="center">
    <img src="docs/pinout.png" alt="Pinout Diagram" width="500px"/>

<br/>

| Pin Label | Function        | Notes                             |
|-----------|-----------------|-----------------------------------|
| VCC       | Power Supply    | 3.3V or 5V, depending on design    |
| GND       | Ground          | Common ground reference            |
| D0        | Data Signal     | Digital input/output signal        |
</div>

## 📏 Dimensions

<div align="center">
<a href="./resources/unit_dimension_V_0_0_1_ue0098_TEMT6000.png"><img src="./resources/unit_dimension_V_0_0_1_ue0098_TEMT6000.png" width="500px"><br/> Dimensions</a>
</div>

## 📃 Topology

<div align="center">
<a href="./resources/unit_topology_V_0_0_1_ue0098_TEMT6000.png"><img src="./resources/unit_topology_V_0_0_1_ue0098_TEMT6000.png" width="300px"><br/> Topology</a>

| Ref. | Description                              |
|------|------------------------------------------|
| S1   | TEMT6000 Ambient Light Sensor            |
| J1   | JST 1 mm pitch Connector for Power Supply and Signal |

</div>

## Reference 

- [Datasheet](https://www.vishay.com/docs/84374/temt6000.pdf)