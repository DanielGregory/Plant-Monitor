# Smart Plant Monitoring System 🌿

This project is a smart plant monitoring system built with a Raspberry Pi 4. It collects real-time data on **soil moisture**, **temperature**, **humidity**, and **light exposure** to help users take better care of their plants—especially beginners or busy individuals.

## 🌱 Why This Project?

Buying plants is easier than ever, but knowing how to care for them isn’t. Many people struggle with plant care due to a lack of accessible, real-time feedback on their plant’s environment. This project aims to solve that by offering:

- Continuous monitoring
- Simple alerts when conditions are poor
- Support for different plant types and environments

## 🔧 Hardware Used

- **Raspberry Pi 4**
- **DHT22** Temperature and Humidity Sensor (Digital)
- **VEML7700** Light Sensor (I2C)
- **Capacitive Soil Moisture Sensor** (Analog)
- **Robot Hat** add-on board (to enable analog input)
- Jumper wires, breadboard, and other connectors

## 🧠 Software Details

- **Language**: Python
- **Libraries Used**:
  - [`Adafruit_DHT`](https://github.com/adafruit/Adafruit_Python_DHT) – for the DHT22 sensor
  - [`adafruit_veml7700`](https://github.com/adafruit/Adafruit_CircuitPython_VEML7700) – for the light sensor
  - `robot_hat` – for analog input from the soil moisture sensor
  - `busio` and `digitalio` – for hardware I/O
  - `board`, `time`

The logic polls each sensor in a loop and prints the values to the console. Threshold-based alerts notify when a plant is in poor conditions (e.g., low light or dry soil).

> ⚠️ Note: The soil moisture sensor was found to be unreliable. This highlighted an important lesson—while building on a budget is good, each component must reliably perform its role.
