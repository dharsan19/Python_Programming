import requests

# API to get no of peoples in Space
response = requests.get(url = "http://api.open-notify.org/astros.json")
response.raise_for_status()

data = response.json()
print(data)