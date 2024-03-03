import requests
import tkinter as tk


def get_temp(city):

    key = "e483cf1c556c43aba7fcbbf3579c5e7e"
    url = f"https://api.weatherbit.io/v2.0/current"
    units = "M"

    r = requests.get(url, params={"city": city, "include": "minutely,alerts", "units": units, "key": key})
    if r.status_code == 200:
        data = r.json()
        weather_data = data["data"][0]
        city_name = weather_data["city_name"]
        temperature = weather_data["temp"]
        return f"The temperature in {city_name} is {temperature} Celsius"
    else:
        return f"API request status code is: {r.status_code}"


def fetch_weather():
    city = city_entry.get()
    result = get_temp(city)
    result_label.config(text=result)


# main app window
app = tk.Tk()
app.title("Weather app")

city_label = tk.Label(app, text="Entry City:")
city_entry = tk.Entry(app)
get_weather_button = tk.Button(app, text="Show Temperature", command=fetch_weather)
result_label = tk.Label(app, text="", wraplength=300)

city_label.pack()
city_entry.pack()
get_weather_button.pack()
result_label.pack()

app.mainloop()