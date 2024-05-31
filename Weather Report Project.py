import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup
import re
import webbrowser
from datetime import datetime, timedelta, timezone

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_wikipedia_info(city):
    url = f'https://en.wikipedia.org/wiki/{city.replace(" ", "_")}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = soup.find_all("p")

    summary_text = ""
    for p in paragraphs[:3]:
        cleaned_text = re.sub(r"\[\d+\]", "", p.get_text())
        cleaned_text = re.sub(r"\([^()]*\)", "", cleaned_text)
        summary_text += cleaned_text + " "

    return summary_text.strip(), url

def open_link(url):
    webbrowser.open_new(url)

def fetch_weather(api_key, root):
    city = city_entry.get()
    weather_data = get_weather(api_key, city)
    if weather_data and "weather" in weather_data:
        city_info = weather_data.get("name", "")
        country = weather_data.get("sys", {}).get("country", "")
        temperature = weather_data.get("main", {}).get("temp", "")
        humidity = weather_data.get("main", {}).get("humidity", "")
        description = weather_data["weather"][0]["description"]

        utc_offset = weather_data.get("timezone", 0)
        local_time = datetime.now(timezone.utc) + timedelta(seconds=utc_offset)

        weather_info_window = tk.Toplevel(root)
        weather_info_window.title("Weather Information")

        time_label = ttk.Label(
            weather_info_window,
            text=f"Local Time: {local_time.strftime('%A, %d %B %Y %I:%M %p')}\n"
                 f"Time Zone: UTC{'+' if utc_offset >= 0 else '-'}{abs(utc_offset) // 3600}",
            font=("Arial", 10),
            wraplength=400,
        )
        time_label.pack(padx=10, pady=10)

        weather_label = ttk.Label(
            weather_info_window,
            text=f"Place: {city_info}, {country}\n"
                 f"Temperature: {temperature}°C\n"
                 f"Humidity: {humidity}%\n"
                 f"Description: {description}\n\n",
            font=("Arial", 10),
            wraplength=400,
        )
        weather_label.pack(padx=10, pady=5)

        openweathermap_link = f"https://openweathermap.org/find?q={city}"
        openweathermap_label = ttk.Label(
            weather_info_window, text="View detailed weather report", cursor="hand2", foreground="red"
        )
        openweathermap_label.pack(pady=5)
        openweathermap_label.bind("<Button-1>", lambda event: webbrowser.open_new(openweathermap_link))

        wikipedia_summary, wikipedia_link = get_wikipedia_info(city)

        wiki_label = ttk.Label(
            weather_info_window,
            text="About the place:\n" + wikipedia_summary + "\n\n"
                 "Source: Wikipedia\n\n",
            font=("Arial", 10),
            wraplength=400,
        )
        wiki_label.pack(padx=10, pady=5)

        link_label = ttk.Label(
            weather_info_window, text="Read more on Wikipedia", cursor="hand2", foreground="blue"
        )
        link_label.pack(pady=5)
        link_label.bind("<Button-1>", lambda event: open_link(wikipedia_link))
    else:
        messagebox.showerror("Error", "Failed to fetch weather data")

def main():
    global root, city_entry, api_key
    api_key = "9e9df35fe5cc859dc01e7d20909ae92f"

    root = tk.Tk()
    root.title("Weather")
    root.geometry("300x150")
    root.resizable(False, False)

    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 10))
    style.configure("TEntry", font=("Helvetica", 10))
    style.configure("TButton", font=("Helvetica", 10))

    frame = ttk.Frame(root, padding=(10, 10, 10, 10))
    frame.grid(row=0, column=0, sticky="nsew")

    city_label = ttk.Label(frame, text="Enter a place: ")
    city_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    city_entry = ttk.Entry(frame, width=20)
    city_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    fetch_button = ttk.Button(frame, text="Fetch Weather", command=lambda: fetch_weather(api_key, root))
    fetch_button.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
