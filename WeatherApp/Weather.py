import requests

api_key = '30d4741c779ba94c470ca1f63045390a'

user_input = input("Enter the name of the city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '44':
    print("Couldn't find the city you're looking for")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {user_input} is : {weather}")
    print(f"The temperature in {user_input} is: {round((temp - 32) * 5/9)}°C / {temp}°F")
