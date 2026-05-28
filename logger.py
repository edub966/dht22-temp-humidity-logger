import serial
import csv
from datetime import datetime
import time

PORT = "COM4"
BAUD = 9600
OUTPUT_FILE = "sensor_log.csv"

def main():
    print(f"Connecting to {PORT}...")
    ser = serial.Serial(PORT, BAUD, timeout=2)
    time.sleep(2)

    with open(OUTPUT_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["datetime", "timestamp_ms", "temperature_c", "humidity_pct"])

        print(f"Logging to {OUTPUT_FILE} — press Ctrl+C to stop\n")

        ser.readline()

        while True:
            line = ser.readline().decode("utf-8").strip()

            if not line or "READ_FAILED" in line:
                print(f"Bad read, skipping: {line}")
                continue

            parts = line.split(",")
            if len(parts) != 3:
                continue

            timestamp_ms, temp, humidity = parts
            dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            writer.writerow([dt, timestamp_ms, temp, humidity])
            f.flush()  # write to disk immediately, not just buffer

            print(f"{dt}  |  {temp}°C  |  {humidity}%")

if __name__ == "__main__":
    main()
