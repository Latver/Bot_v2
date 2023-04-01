import requests
import os
import sys
import threading
from tkinter import Tk, Button
import tkinter as tk
from tkinter import filedialog, messagebox
from bs4 import BeautifulSoup
import webbrowser
import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont, QColor, QPalette

# Путь до файла
PATH = os.path.dirname(os.path.abspath(__file__))

def Weather_thread():
    menu = Menu()
    Thread = threading.Thread(target=menu.Weather)
    Thread.start()

def News_thread():
    menu = Menu()
    Thread = threading.Thread(target=menu.News)
    Thread.start()

class Menu:

    def Weather(self):
        def get_weather():
            label_weather.config(text="Загрузка погоды...", fg="black")
            root.update()
            city = edit_city.get()
            api_key = "26aecdf5b56cf2b82e37bdac6985cff6"
            geocode_url = f"https://geocode.xyz/{city}?json=1"
            response = requests.get(geocode_url)
            if response.status_code == 200:
                location_data = response.json()
                if "latt" in location_data:
                    lat = location_data["latt"]
                    lon = location_data["longt"]
                    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts&appid={api_key}&lang=ru"
                    response = requests.get(url)
                    if response.status_code == 200:
                        weather_data = response.json()
                        forecast = ""
                        for day in weather_data["daily"]:
                            timestamp = day["dt"]
                            date = datetime.datetime.fromtimestamp(timestamp)
                            day_of_week = date.strftime("%A").replace("Monday", "Понедельник").replace("Tuesday", "Вторник").replace("Wednesday", "Среда").replace("Thursday", "Четверг").replace("Friday", "Пятница").replace("Saturday", "Суббота").replace("Sunday", "Воскресенье")
                            weather = day["weather"][0]["description"]
                            temperature_min = day["temp"]["min"] - 273.15
                            temperature_max = day["temp"]["max"] - 273.15
                            humidity = day["humidity"]
                            wind_speed = day["wind_speed"]
                            forecast += f"{day_of_week}, {date.strftime('%d.%m.%Y')}: {weather}, температура: {temperature_min:.1f}...{temperature_max:.1f} °C, влажность: {humidity} %, скорость ветра: {wind_speed} м/с\n\n"
                        label_weather.config(text=forecast)
                    else:
                        label_weather.config(text="Не удалось получить прогноз погоды\n", fg="black")
                        label_weather.config(text=label_weather.cget("text") + "Проверьте доступ в интернет", fg="red")
                else:
                    label_weather.config(text="Не удалось найти координаты города\n", fg="black")
                    label_weather.config(text=label_weather.cget("text") + "Проверьте правильность написания города", fg="red")
            else:
                label_weather.config(text="Не удалось найти город\n", fg="black")
                label_weather.config(text=label_weather.cget("text") + "Попробуйте снова нажать кнопку или проверьте правильность написания города", fg="red")

        # Создаем главное окно
        root = tk.Tk()

        # Задаем заголовок окна
        root.title("Погода")

        # Задаем размеры окна
        root.geometry('1100x500')

        # Задаем цвет фона окна
        root.config(bg="#DFE4E2")

        # Задаем шрифт
        font = ("Arial", 16)

        # Создаем виджеты
        label_city = tk.Label(root, text="Введите город:", font=font, bg="#DFE4E2")
        label_city.place(x=50, y=50)

        edit_city = tk.Entry(root, font=font, width=20)
        edit_city.place(x=250, y=50)
        edit_city.bind("<Return>", lambda event: get_weather())

        button_weather = tk.Button(root, text="Получить погоду", font=font, width=20, command=get_weather)
        button_weather.place(x=250, y=100)

        label_weather = tk.Label(root, font=("Arial", 14), bg="#DFE4E2")
        label_weather.place(x=0, y=150, width=1100, height=400)

        # Запускаем главный цикл приложения
        root.mainloop()
            
    @staticmethod
    def News():
        # Определить функцию для получения новостей
        def get_news():
            nonlocal news_list

            # Очистить список новостей
            news_list.delete(0, tk.END)

            # Создать окно загрузки
            loading_window = tk.Toplevel(window)
            loading_window.title("Загрузка...")
            loading_label = tk.Label(loading_window, text="Идет загрузка новостей, пожалуйста, подождите...")
            loading_label.pack(pady=10)
            loading_window.update()

            # URL сайта TASS, который нужно спарсить
            url = "https://tass.ru/rss/v2.xml"

            # Запросить XML содержимое сайта
            response = requests.get(url)
            xml_content = response.content

            # Разобрать XML содержимое с помощью BeautifulSoup
            soup = BeautifulSoup(xml_content, "xml")

            # Найти заголовки и ссылки всех статей
            articles = soup.find_all("item")

            # Перебрать статьи и добавить их в список новостей
            for article in articles:
                headline = article.find("title").text
                link = article.find("link").text
                news_list.insert(tk.END, headline)
                news_list.insert(tk.END, "\n")
                # Сохранить ссылку на статью в список ссылок
                news_links.append(link)

            # Закрыть окно загрузки
            loading_window.destroy()

        # Создать главное окно Tkinter
        window = tk.Tk()
        window.title("Агрегатор новостей")

        # Создать метку и кнопку
        label = tk.Label(window, text="Нажмите кнопку, чтобы получить последние новости:")
        label.pack(pady=10)
        button = tk.Button(window, text="Получить новости", command=get_news)
        button.pack()

        # Создать список для отображения новостей
        news_list = tk.Listbox(window, width=100, height=20)
        news_list.pack(pady=10)

        # Создать список ссылок на новости
        news_links = []

        # Создать функцию для открытия ссылки новости в браузере
        def open_link(event):
            url = news_links[news_list.curselection()[0]]
            webbrowser.open(url)

        # Привязать функцию к событию нажатия на список новостей
        news_list.bind("<Double-Button-1>", open_link)

        # Запустить главный цикл обработки событий Tkinter
        window.mainloop()

    def parent_menu():
        # Родительское окно
        global window
        window = Tk()
        window.title('Прочее')
        window.columnconfigure([0], weight=1, minsize=150)
        window.rowconfigure([0], weight=1, minsize=0)

        # Кнопки родительского окна
        button1 = Button(window, font=('Verdana', 10, 'bold'), text='Погода', width=20, height=3, command=Weather_thread)
        button1.grid(column=0, row=0, sticky='wens')
        button2 = Button(window, font=('Verdana', 10, 'bold'), text='Новости', width=20, height=3, command=News_thread)
        button2.grid(column=0, row=1, sticky='wens')

        window.mainloop()