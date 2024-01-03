import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

def display_weather(weather_data):
    if weather_data:
        result_str = (
            f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:\n"
            f"Temperature: {weather_data['main']['temp']}°C\n"
            f"Description: {weather_data['weather'][0]['description']}\n"
            f"Humidity: {weather_data['main']['humidity']}%\n"
            f"Wind Speed: {weather_data['wind']['speed']} m/s"
        )
        return result_str
    else:
        return "Failed to fetch weather data."

def get_weather_and_display(api_key, city, result_label):
    weather_data = get_weather(api_key, city)
    result_label.config(text=display_weather(weather_data))

def main():
    api_key = '87551c89a236c69b2e607e44f187551f'

    def on_submit():
        city = city_entry.get()
        get_weather_and_display(api_key, city, result_label)

    # GUI setup
    app = tk.Tk()
    app.title("Somya Weather App")

    tk.Label(app, text="Enter city name:").pack(pady=10)

    city_entry = tk.Entry(app, width=30)
    city_entry.pack(pady=10)

    submit_button = tk.Button(app, text="Get Weather", command=on_submit)
    submit_button.pack(pady=10)

    result_label = tk.Label(app, text="")
    result_label.pack(pady=10)

    app.mainloop()

if __name__ == "__main__":
    main()
