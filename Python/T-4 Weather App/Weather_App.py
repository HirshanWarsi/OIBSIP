import requests

api_key = "14200ae164f7f610fca113ef344c16bb"

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}"
    response = requests.get(url)
    return response.json()

def display_weather(weather_data, city):
    if weather_data.get('cod') == '404':
        print("No City Found")
    else:
        weather = weather_data['weather'][0]['main']
        temp_f = round(weather_data['main']['temp'])
        temp_c = round((temp_f - 32) * 5.0/9.0)
        humidity = weather_data['main']['humidity']

        print(f"The weather in {city} is: {weather}")
        print(f"The temperature in {city} is: {temp_f}°F / {temp_c}°C")
        print(f"The humidity in {city} is: {humidity}%")

def main():
    user_input = input("Enter city: ")
    weather_data = get_weather(user_input, api_key)
    display_weather(weather_data, user_input)

if __name__ == "__main__":
    main()

