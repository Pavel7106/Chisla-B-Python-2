"""
ПОМОЩНИК ДЛЯ ПОИСКА ТЕЛЕФОНА / КОМПА
Показывает город и провайдера по IP-адресу
"""
import requests

url = "http://ip-api.com/json/"

response = requests.get(url)
data = response.json()

print("\n" + "="*50)
print("📍 МЕСТОПОЛОЖЕНИЕ ПО IP")
print("="*50)
print(f"🌍 Страна: {data.get('country', 'Неизвестно')}")
print(f"🏙️ Город: {data.get('city', 'Неизвестно')}")
print(f"📡 Провайдер: {data.get('isp', 'Неизвестно')}")
print(f"📱 IP-адрес: {data.get('query', 'Неизвестно')}")
print(f"🗺️ Координаты: {data.get('lat', '?')}, {data.get('lon', '?')}")
print("="*50)
print("⚠️ Точность: примерно до района (не точный адрес)")
