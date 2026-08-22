# Script to create a polished visual HTML page with SVG diagram and Arduino code for ESP32-S3 LED circuit html_content = """

Wiring a 5mm LED + current-limiting resistor to GPIO 4 on the ESP32-S3 N16R8 / N8R16 board

Follow the schematic below to connect the external LED safely to **GPIO 4** and **GND**:

|From (Source)|To (Destination)|Component / Polarity|Notes|
|--|--|--|--|
|ESP32-S3 GPIO 4|Resistor (Lead 1)|Control Signal (3.3V Logic)|Pin 4 on left header|
|Resistor (Lead 2)|LED Anode (+)|220Ω to 330Ω Resistor|Connects to the longer leg of the LED|
|LED Cathode (-)|ESP32-S3 GND|Return Path|Connects from the shorter leg / flat edge to GND|

```
GPIO 33–37
```
are reserved internally for the high-speed Octal memory bus, and pins
```
GPIO 0, 45, 46
```
are strapping pins that affect boot mode.
Copy and paste this sketch into the Arduino IDE:

```
// =========================================================================
// ESP32-S3 External LED Blink Example
// Controls a single external LED connected to GPIO 4
// =========================================================================

// Define the safe GPIO pin connected to the external LED
const int LED_PIN = 4;

void setup() {
 // Configure GPIO 4 as a digital output
 pinMode(LED_PIN, OUTPUT);

 // Optional: Initialize Serial monitor for debugging
 Serial.begin(115200);
 Serial.println("ESP32-S3 External LED Test Started!");

void loop() {
 // 1. Turn the external LED ON (3.3V output)
 digitalWrite(LED_PIN, HIGH);
 Serial.println("LED is ON");
 delay(1000); // Wait for 1 second (1000 milliseconds)

 // 2. Turn the external LED OFF (0V output)
 digitalWrite(LED_PIN, LOW);
 Serial.println("LED is OFF");
 delay(1000); // Wait for 1 second

```

```
ESP32S3 Dev Module
```

```
Enabled
```

```
16MB (128Mb)
```
or
```
8MB
```

```
OPI PSRAM
```
(for N16R8/N8R16)
```
115200
```