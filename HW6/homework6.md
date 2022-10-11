# завдання 1
# урл http://api.open-notify.org/astros.json
# вивести список всіх астронавтів, що перебувають в даний момент на орбіті

import requests
from pprint import pprint
from tabulate import tabulate

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
response_json = response.json()

people = response_json["people"]
pprint(tabulate(people))
print("")

# завдання 2
# апі погоди (всі токени я для вас вже прописав)
# https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric
# де city_name - назва міста на аглійській мові (наприклад, odesa, kyiv, lviv)
# роздрукувати тепрературу та швидкість вітру. з вказівкою міста, яке було вибране

url = "http://api.openweathermap.org/data/2.5/weather?appid=94b5818d19264a3a3eb551824f1ef56e&q=kyiv"
response = requests.get(url)
response_json = response.json()

city_name = response_json["name"]
main = response_json["main"]
wind = response_json["wind"]
temp, feel_temp, temp_min, temp_max = main["temp"], main["feels_like"], main["temp_max"], main["temp_min"]

print("The weather in ", city_name, "-")
print("Wind parameters: ", wind)
print("The temperature now is", int(temp - 273), "C,", "feels like", int(feel_temp - 273), "C")
print("min.temperature is", int(temp_min - 273), "C,", "max_temperature is", int(temp_max - 273), "C")
