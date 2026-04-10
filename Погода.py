import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

print(f"Статус-код: {response.status_code}")

print("Заголовки ответа:")
for key, value in response.headers.items():
    print(f"{key}: {value}")

print("\nДанные ответа в формате JSON:")
data = response.json()
print(data)

print("\nТекущие координаты МКС:")
print(f"Широта: {data['iss_position']['latitude']}")
print(f"Долгота: {data['iss_position']['longitude']}")
