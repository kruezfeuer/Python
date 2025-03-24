import requests
import json
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

# Задание 1

def get_weather_data(city_name):
    api_key = "fc27212dd5eadaf13d9b6f2ca842de17"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных о погоде: {e}")

        return None

def display_weather_info(weather_data):
    if weather_data:
        city_name = weather_data["name"]
        weather = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        pressure = weather_data["main"]["pressure"]
        wind_speed = weather_data["wind"]["speed"]

        print(f"Погода в городе {city_name}:")
        print(f"- Описание: {weather}")
        print(f"- Температура: {temperature}°C")
        print(f"- Влажность: {humidity}%")
        print(f"- Давление: {pressure} гПа")
        print(f"- Скорость ветра: {wind_speed} м/с")
    else:
        print("Не удалось получить информацию о погоде.")

def main():
    city_name = "Saint Petersburg"
    weather_data = get_weather_data(city_name)
    display_weather_info(weather_data)

if __name__ == "__main__":
    main()

print()

# Задание 2

import requests
import json
from datetime import datetime

def get_vacancies(keyword, area_id):
    url = f"https://api.hh.ru/vacancies?text={keyword}&area={area_id}&currency_code=RUR&per_page=20&page=0"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    vacancies = []
    for item in data["items"]:
        salary = item.get('salary')
        if salary:
            salary_from = salary.get('from')
            salary_to = salary.get('to')
            salary_currency = salary.get('currency')
            if salary_from and salary_to:
                salary_str = f"{salary_from} - {salary_to} {salary_currency}"
            elif salary_from:
                salary_str = f"{salary_from} {salary_currency}"
            elif salary_to:
                salary_str = f"{salary_to} {salary_currency}"
            else:
                salary_str = "Н/Д"

    
            published_at = datetime.fromisoformat(item["published_at"]).strftime('%m.%d.%Y')
            vacancy = {
                "Название": item["name"],
                "Работодатель": item["employer"]["name"],
                "Зарплата": salary_str,
                "Регион": item["area"]["name"],
                "Дата публикации": published_at
            }
            vacancies.append(vacancy)
    
    return vacancies

keyword = "python"
area_id = 2  

vacancies = get_vacancies(keyword, area_id)

for vacancy in vacancies:
    for key, value in vacancy.items():
        print(f"{key}: {value}")
    print()

# Дополнительное задание

class Generator:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор картинок с лисичками")

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.next_button = tk.Button(root, text="Следующая картинка с лисичками :)", command=self.load_new_image, bg="orange", fg="white", font=("Verdana", 14, "bold"))
        self.next_button.pack()

        self.load_new_image()

    def load_new_image(self):
        response = requests.get("https://randomfox.ca/floof/")
        data = response.json()
        image_url = data['image']

        image_response = requests.get(image_url)
        image_data = Image.open(BytesIO(image_response.content))

        self.photo = ImageTk.PhotoImage(image_data)

        self.image_label.config(image=self.photo)
        self.image_label.image = self.photo

if __name__ == "__main__":
    root = tk.Tk()
    app = Generator(root)
    root.mainloop()