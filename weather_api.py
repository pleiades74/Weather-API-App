
import requests

API_KEY = "YOUR_API_KEY"  # Get free API key from https://openweathermap.org
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        print(f"{city_name}: {temp}°C, {weather}")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    city = input("Enter city: ")
    get_weather(city)
