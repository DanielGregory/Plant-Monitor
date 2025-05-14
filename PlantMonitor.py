import time
import board
import busio
import adafruit_dht
import adafruit_veml7700
import digitalio
from robot_hat import ADC

# I2C for VEML7700
i2c = busio.I2C(board.SCL, board.SDA)
veml = adafruit_veml7700.VEML7700(i2c)

# DHT22 on GPIO4 (Digital pin 0)
dhtDevice = adafruit_dht.DHT22(board.D17)

# Soil sensor
adc = ADC("A0")  # Use Robot Hat's ADC interface      
values = [0] * 100  # Store 100 readings for averaging


print("Starting Plant Monitoring System...\n")        

while True:
    try:
        # DHT22 readings
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity

        # Soil sensor
        # Soil sensor - Collect 100 readings
        for i in range(100):
            adc_value = adc.read()  # Read the value from the ADC
            #print(f"ADC reading {i}: {adc_value} (Type: {type(adc_value)})")

            # If adc_value is a list, choose the first element or average it
            if isinstance(adc_value, list):
                values[i] = adc_value[0]  # Take the first value
            else:
                values[i] = adc_value  # Otherwise, take the scalar value

        # Get the maximum value from the list
        max_soil_value = max(values)

        # VEML7700 light sensor
        lux = veml.lux

        print("----- Plant Monitoring System -----")

        print(f"Soil Moisture: {max_soil_value} ")

        if max_soil_value < 100:
            print("  Too Dry")
        elif max_soil_value > 400:
            print("  Too Wet")
        else:
            print("  Good")

        print(f"Light Level: {lux:.2f} lux")
        if lux < 300:
            print("  Too Dark")
        elif lux > 10000:
            print("  Too Bright")
        else:
            print("  Good")

        print(f"Humidity: {humidity:.1f}%")
        print(f"Temperature: {temperature_c:.1f}C")
        print("-----------------------------------\n")

    except RuntimeError as error:
        print(f"DHT22 read error: {error}")
    except Exception as error:
        print(f"Other error: {error}")
        dhtDevice.exit()
        raise error

    time.sleep(5)