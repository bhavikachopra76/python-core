import requests

api_key = "your_api_key_here"
city = "Mohali"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city},&APPID={api_key}&units=metric"
response = requests.get(url)
data = response.json()

for i , j in data['main'].items():
    print(i, ":", j)