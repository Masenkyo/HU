import requests
key = "aef970e5de15ffde15625b1971172283"
city = "Utrecht"

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric")
data = response.json()

print(data)
for key, value in data.items():
    print(f"key({key}): value({value})")