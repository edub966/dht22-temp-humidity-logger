# DHT22 Temperature & Humidity Logger

An Arduino-based sensor system that reads temperature and humidity in real time,
logs the data to a CSV file via serial communication, and visualizes it with Python.

## How it works

1. A DHT22 sensor wired to an Arduino Nano reads temperature and humidity every 2 seconds
2. Readings are streamed over USB serial as CSV-formatted lines
3. A Python logger captures the serial stream and writes it to `sensor_log.csv`
4. A Python plotter reads the CSV and generates a time-series chart with matplotlib

## Hardware

- Arduino Nano
- DHT22 temperature & humidity sensor (3-pin module)
- USB cable

## Wiring

| DHT22 Pin | Arduino Nano Pin |
|-----------|-----------------|
| VCC       | 5V              |
| DATA      | D2              |
| GND       | GND             |

## Setup

1. Install the Adafruit DHT sensor library in Arduino IDE (Tools → Manage Libraries → search "DHT sensor library")
2. Upload `arduino/dht22_logger.ino` to your Nano
3. Install Python dependencies: pip install pyserial matplotlib pandas
4. Run the logger (update `PORT` in `logger.py` if not on COM4):
5. When done collecting, run the plotter: plotter.py
## Output
The logger prints live readings to the console and saves them to `sensor_log.csv`.
The plotter generates a two-panel time-series chart of temperature and humidity.

## Skills

Arduino · C++ · Python · pyserial · pandas · matplotlib · Serial communication · ETL
