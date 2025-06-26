#Day 13 of the 90 days python challenge

import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # For Celsius, use 'imperial' for Fahrenheit
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises an error for bad status codes
        
        weather_data = response.json()
        
        # Extract and display relevant information
        print(f"\nWeather in {city}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Feels like: {weather_data['main']['feels_like']}°C")
        print(f"Weather conditions: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind speed: {weather_data['wind']['speed']} m/s")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

def main():
    api_key = "your_api_key_here"  # Replace with your actual API key
    city = input("Enter city name: ")
    get_weather(api_key, city)

if __name__ == "__main__":
    main()