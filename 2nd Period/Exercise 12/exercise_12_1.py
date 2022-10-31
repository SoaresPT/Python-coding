# 12.1
import requests

url = "https://api.chucknorris.io/jokes/random"
data = requests.get(url)
data_json = data.json()
print(data_json['value'])