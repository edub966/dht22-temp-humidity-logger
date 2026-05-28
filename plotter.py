import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

FILE = "sensor_log.csv"

df = pd.read_csv(FILE)
df["datetime"] = pd.to_datetime(df["datetime"])

# drop any rows where readings failed
df = df[df["temperature_c"] != " READ_FAILED"]
df["temperature_c"] = df["temperature_c"].astype(float)
df["humidity_pct"] = df["humidity_pct"].astype(float)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6), sharex=True)
fig.suptitle("DHT22 Temperature & Humidity Log", fontsize=14, fontweight="bold")

# temperature plot
ax1.plot(df["datetime"], df["temperature_c"], color="#E24B4A", linewidth=1.5)
ax1.fill_between(df["datetime"], df["temperature_c"], alpha=0.1, color="#E24B4A")
ax1.set_ylabel("Temperature (°C)")
ax1.grid(True, alpha=0.3)
ax1.set_ylim(df["temperature_c"].min() - 1, df["temperature_c"].max() + 1)

# humidity plot
ax2.plot(df["datetime"], df["humidity_pct"], color="#378ADD", linewidth=1.5)
ax2.fill_between(df["datetime"], df["humidity_pct"], alpha=0.1, color="#378ADD")
ax2.set_ylabel("Humidity (%)")
ax2.set_xlabel("Time")
ax2.grid(True, alpha=0.3)
ax2.set_ylim(df["humidity_pct"].min() - 2, df["humidity_pct"].max() + 2)

# format x-axis as readable timestamps
ax2.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("sensor_plot.png", dpi=150, bbox_inches="tight")
plt.show()

print(f"\nStats:")
print(f"  Readings:       {len(df)}")
print(f"  Temp range:     {df['temperature_c'].min():.1f}°C – {df['temperature_c'].max():.1f}°C")
print(f"  Humidity range: {df['humidity_pct'].min():.1f}% – {df['humidity_pct'].max():.1f}%")
print(f"\nPlot saved to sensor_plot.png")