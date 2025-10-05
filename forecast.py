import requests
from bs4 import BeautifulSoup
city = input("Enter a city name: ")

city_format = city.lower().strip().replace(" ", "-")
url = f"https://www.timeanddate.com/weather/usa/{city_format}"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

try:
    span = soup.find("div", class_="h2")
    if span:
        temperature = span.get_text(strip=True)
        description =span.find_next("p").get_text(strip=True)
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}")
        print(f"Condition: {description}")
    else:
        print("Could not retrieve weather information. Please check the city name and try again.")
except NameError:
    print("Please check the city name and try again")