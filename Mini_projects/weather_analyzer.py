import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# File Path Setup

CSV_FILE = "data/weather.csv"
os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)
# Load Data

def load_weather_data():
    if not os.path.exists(CSV_FILE):
        print("weather.csv not found! Please create it inside the data/ folder.")
        return None
    try:
        df = pd.read_csv(CSV_FILE, parse_dates=["Date"])
        return df
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None


# Analysis Functions

def analyze_weather(df):
    print("\n--- Weather Analysis ---")
    max_temp = df["Temperature"].max()
    min_temp = df["Temperature"].min()
    avg_temp = df["Temperature"].mean()

    print(f" Max Temperature: {max_temp:.2f} °C")
    print(f" Min Temperature: {min_temp:.2f} °C")
    print(f" Avg Temperature: {avg_temp:.2f} °C")

    max_humidity = df["Humidity"].max()
    min_humidity = df["Humidity"].min()
    avg_humidity = df["Humidity"].mean()

    print(f" Max Humidity: {max_humidity:.2f}%")
    print(f" Min Humidity: {min_humidity:.2f}%")
    print(f" Avg Humidity: {avg_humidity:.2f}%")
    print("------------------------\n")


# Plotting Functions

def plot_temperature(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df["Date"], df["Temperature"], marker="o", linestyle="-", label="Temperature (°C)")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Daily Temperature Trend")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_humidity(df):
    plt.figure(figsize=(10, 5))
    plt.bar(df["Date"].dt.strftime("%Y-%m-%d"), df["Humidity"], color="skyblue", label="Humidity (%)")
    plt.xlabel("Date")
    plt.ylabel("Humidity (%)")
    plt.title("Daily Humidity Levels")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
# Main Function

def main():
    df = load_weather_data()
    if df is None:
        return

    analyze_weather(df)

    print(" Generating plots...")
    plot_temperature(df)
    plot_humidity(df)

if __name__ == "__main__":
    main()
