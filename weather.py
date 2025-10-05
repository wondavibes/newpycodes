import requests
from bs4 import BeautifulSoup

city = input("Enter the city name: ")

city_format = city.lower().replace(" ", "-")

response = requests.get(f"https://www.weather-forecast.com/locations/{city_format}/forecasts/latest")

soup = BeautifulSoup(response.text, 'html.parser')


try:
    span = soup.find('span', class_='phrase')
    if span:
        weather = span.get_text(strip=True)
        print(f"The weather in {city} is: {weather}") 
except AttributeError:
    print("Could not retrieve weather information. Please check the city name and try again.")  