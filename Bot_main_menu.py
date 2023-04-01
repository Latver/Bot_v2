#########################################
# Author: LATVER                        #
# Bot_v2.0: главное окно хелппера       #
# TODO: Доделать функцию горячих клавиш #
#########################################

#Библотеки
from tkinter import *
from tkinter import ttk, Tk, Entry, END
import os, time, keyboard, requests
from AutoClicker import status_on
from browser import func_browser
from Calculator_seconds import calc_sec
from power_PC import menu_power_pc
from setting_bot import setting_bot_win
from Random import random_menu
from other import Menu

#Путь до файлов
PATH = os.path.dirname(os.path.abspath(__file__))

#Версия бота
current_version = "2.0"

#Проверка и получение обновлений
def get_latest_version():
    url = "https://example.com/latest_version.txt" # URL, где расположен файл с последней версией
    response = requests.get(url)
    latest_version = response.text.strip()
    return latest_version


def delete_symbols():
    enter.delete(0, END)

#Функция питания ПК
def power_PC():
    try:
        window.withdraw()
        menu_power_pc.menu_pc()
    except WindowsError:
        window.withdraw()
        error = Toplevel(window)
        error.title('Ошибка!')
        error.geometry('310x80')
        error.columnconfigure([0], weight = 1, minsize = 150)
        error.rowconfigure([0], weight = 1, minsize = 0)
        error_lbl = Label(error, text = 'Ошибка: Не найден файл "power_PC.py"', font = ('Verdana', 10, 'bold'), fg = 'red').grid(column = 0, row = 0, stick = 'wens')
        window.deiconify()

#Функция браузера
def browser():
    try:
        window.withdraw()
        func_browser.menu()
    except WindowsError:
        window.withdraw()
        error = Toplevel(window)
        error.title('Ошибка!')
        error.geometry('310x80')
        error.columnconfigure([0], weight = 1, minsize = 150)
        error.rowconfigure([0], weight = 1, minsize = 0)
        error_lbl = Label(error, text = 'Ошибка: Не найден файл "browser.py"', font = ('Verdana', 10, 'bold'), fg = 'red').grid(column = 0, row = 0, stick = 'wens')

#Функция системы Windows
def system():
    try:
        window.withdraw()
        os.startfile(PATH + r'\system.py')
    except WindowsError:
        window.withdraw()
        error = Toplevel(window)
        error.title('Ошибка!')
        error.geometry('310x80')
        error.columnconfigure([0], weight = 1, minsize = 150)
        error.rowconfigure([0], weight = 1, minsize = 0)
        error_lbl = Label(error, text = 'Ошибка: Не найден файл "system.py"', font = ('Verdana', 10, 'bold'), fg = 'red').grid(column = 0, row = 0, stick = 'wens')

#Функция автокликера
def AutoClicker():
    try:
        window.withdraw()
        status_on.window_menu()
    except WindowsError:
        window.withdraw()
        error = Toplevel(window)
        error.title('Ошибка!')
        error.geometry('310x80')
        error.columnconfigure([0], weight = 1, minsize = 150)
        error.rowconfigure([0], weight = 1, minsize = 0)
        error_lbl = Label(error, text = 'Ошибка: Не найден файл "AutoClicker.py"', font = ('Verdana', 10, 'bold'), fg = 'red').grid(column = 0, row = 0, stick = 'wens')

#Функция починки ПК
def Fixing_PC():
    try:
        window.withdraw()
        os.startfile(PATH + r'\Fixing_PC.py')
    except WindowsError:
        window.withdraw()
        error = Toplevel(window)
        error.title('Ошибка!')
        error.geometry('310x80')
        error.columnconfigure([0], weight = 1, minsize = 150)
        error.rowconfigure([0], weight = 1, minsize = 0)
        error_lbl = Label(error, text = 'Ошибка: Не найден файл "Fixing_PC.py"', font = ('Verdana', 10, 'bold'), fg = 'red').grid(column = 0, row = 0, stick = 'wens')

#Функция рандомайзера
def Random():
    try:
        window.withdraw()
        random_menu.menu()
    except WindowsError:
        window.withdraw()
        error = Toplevel(window)
        error.title('Ошибка!')
        error.geometry('310x80')
        error.columnconfigure([0], weight = 1, minsize = 150)
        error.rowconfigure([0], weight = 1, minsize = 0)
        error_lbl = Label(error, text = 'Ошибка: Не найден файл "Random.py"', font = ('Verdana', 10, 'bold'), fg = 'red').grid(column = 0, row = 0, stick = 'wens')

#Функция настроек бота
def setting_bot():
    try:
        window.withdraw()
        setting_bot_win.main()
    except WindowsError:
        window.withdraw()
        error = Toplevel(window)
        error.title('Ошибка!')
        error.geometry('310x80')
        error.columnconfigure([0], weight = 1, minsize = 150)
        error.rowconfigure([0], weight = 1, minsize = 0)
        error_lbl = Label(error, text = 'Ошибка: Не найден файл "setting_bot.py"', font = ('Verdana', 10, 'bold'), fg = 'red').grid(column = 0, row = 0, stick = 'wens')

#Функция всего прочего
def other():
    try:
        window.withdraw()
        Menu.parent_menu()
    except WindowsError:
        window.withdraw()
        error = Toplevel(window)
        error.title('Ошибка!')
        error.geometry('310x80')
        error.columnconfigure([0], weight = 1, minsize = 150)
        error.rowconfigure([0], weight = 1, minsize = 0)
        error_lbl = Label(error, text = 'Ошибка: Не найден файл "other.py"', font = ('Verdana', 10, 'bold'), fg = 'red').grid(column = 0, row = 0, stick = 'wens')

#Главное окно поверх всех окон
def lift():
    window.attributes("-topmost", True)
#Главное окно не поверх всех окон
def not_lift():
    window.attributes("-topmost", False)

#При нажатии клавиши enter переходит в функцию files
def press_enter(Return):
    files()

#Функция горячих клавиш
def files():
    global enter

    #Берем значение из строки
    value = enter.get()

    #Горячие клавиши на выключение ПК
    if value == '11':
        try:
            window.withdraw()
            class_shutdown.Power_off()
        except WindowsError:
            window.withdraw()
            error = Toplevel(window)
            error.title('Ошибка!')
            error.geometry('310x80')
            error.columnconfigure([0], weight = 1, minsize = 150)
            error.rowconfigure([0], weight = 1, minsize = 0)
            error_lbl = Label(error, text = 'Ошибка: Не найден файл "Power_PC.py"', font = ('Verdana', 10, 'bold'), fg = 'red').grid(column = 0, row = 0, stick = 'wens')
    elif value == '111':
        window.withdraw()
        os.system('shutdown /s /t 1 /f')
    elif value == '112':
        try:
            window.withdraw()
            class_shutdown.templates()
        except WindowsError:
            window.withdraw()
            error = Toplevel(window)
            error.title('Ошибка!')
            error.geometry('310x80')
            error.columnconfigure([0], weight = 1, minsize = 150)
            error.rowconfigure([0], weight = 1, minsize = 0)
            error_lbl = Label(error, text = 'Ошибка: Не найден файл "Power_PC.py"', font = ('Verdana', 10, 'bold'), fg = 'red').grid(column = 0, row = 0, stick = 'wens')        
    elif value == '113':
        window.withdraw()
        os.system('shutdown -a')
    elif value == '114':
        try:
            window.withdraw()
            calc_sec.menu()
        except WindowsError:
            window.withdraw()
            error = Toplevel(window)
            error.title('Ошибка!')
            error.geometry('310x80')
            error.columnconfigure([0], weight = 1, minsize = 150)
            error.rowconfigure([0], weight = 1, minsize = 0)
            error_lbl = Label(error, text = 'Ошибка: Не найден файл "Power_PC.py"', font = ('Verdana', 10, 'bold'), fg = 'red').grid(column = 0, row = 0, stick = 'wens')  
    elif value == '1121':
        os.system('shutdown /s /t 1800 /f')
    elif value == '1122':
        os.system('shutdown /s /t 3600 /f')
    elif value == '1123':
        os.system('shutdown /s /t 5400 /f')
    elif value == '1124':
        os.system('shutdown /s /t 7200 /f')

    #Горячие клавиши на перезагрузку ПК
    elif value == '12':
        try:
            window.withdraw()
            class_reboot.Reboot()
        except WindowsError:
            window.withdraw()
            error = Toplevel(window)
            error.title('Ошибка!')
            error.geometry('310x80')
            error.columnconfigure([0], weight = 1, minsize = 150)
            error.rowconfigure([0], weight = 1, minsize = 0)
            error_lbl = Label(error, text = 'Ошибка: Не найден файл "Power_PC.py"', font = ('Verdana', 10, 'bold'), fg = 'red').grid(column = 0, row = 0, stick = 'wens')
    elif value == '121':
        window.withdraw()
        os.system('shutdown /r /t 1 /f')
    elif value == '122':
        try:
            window.withdraw()
            class_shutdown.templates()
        except WindowsError:
            window.withdraw()
            error = Toplevel(window)
            error.title('Ошибка!')
            error.geometry('310x80')
            error.columnconfigure([0], weight = 1, minsize = 150)
            error.rowconfigure([0], weight = 1, minsize = 0)
            error_lbl = Label(error, text = 'Ошибка: Не найден файл "Power_PC.py"', font = ('Verdana', 10, 'bold'), fg = 'red').grid(column = 0, row = 0, stick = 'wens')        
    elif value == '123':
        os.system('shutdown -a')
    elif value == '124':
        try:
            window.withdraw()
            calc_sec.menu()
        except WindowsError:
            window.withdraw()
            error = Toplevel(window)
            error.title('Ошибка!')
            error.geometry('310x80')
            error.columnconfigure([0], weight = 1, minsize = 150)
            error.rowconfigure([0], weight = 1, minsize = 0)
            error_lbl = Label(error, text = 'Ошибка: Не найден файл "Power_PC.py"', font = ('Verdana', 10, 'bold'), fg = 'red').grid(column = 0, row = 0, stick = 'wens')  
    elif value == '1221':
        os.system('shutdown /r /t 1800 /f')
    elif value == '1222':
        os.system('shutdown /r /t 3600 /f')
    elif value == '1223':
        os.system('shutdown /r /t 5400 /f')
    elif value == '1224':
        os.system('shutdown /r /t 7200 /f')

    #Горячие клавиши на спящий режим
    elif value == '13':
        pass
    elif value == '134':
        try:
            window.withdraw()
            calc_sec.menu()
        except WindowsError:
            window.withdraw()
            error = Toplevel(window)
            error.title('Ошибка!')
            error.geometry('310x80')
            error.columnconfigure([0], weight = 1, minsize = 150)
            error.rowconfigure([0], weight = 1, minsize = 0)
            error_lbl = Label(error, text = 'Ошибка: Не найден файл "Power_PC.py"', font = ('Verdana', 10, 'bold'), fg = 'red').grid(column = 0, row = 0, stick = 'wens')

    #Горячие клавиши на выход из учетной записи
    elif value == '14':
        pass
    elif value == '144':
        try:
            window.withdraw()
            calc_sec.menu()
        except WindowsError:
            window.withdraw()
            error = Toplevel(window)
            error.title('Ошибка!')
            error.geometry('310x80')
            error.columnconfigure([0], weight = 1, minsize = 150)
            error.rowconfigure([0], weight = 1, minsize = 0)
            error_lbl = Label(error, text = 'Ошибка: Не найден файл "Power_PC.py"', font = ('Verdana', 10, 'bold'), fg = 'red').grid(column = 0, row = 0, stick = 'wens')

    elif value == '21':
        func_browser.vk_and_youtube()
    elif value == '22':
        func_browser.vk()
    elif value == '23':
        func_browser.youtube()
    elif value == '24':
        func_browser.google_translate()
    elif value == '25':
        func_browser.google_disk()
    elif value == '26':
        func_browser.gmail()   

    #Проверка ввода в поле
    elif not value:
        enter.delete(0, END)
        enter.insert(0, "Не введено число")
        enter.config(fg='red', font=('Arial', 12, 'bold'))
        enter.bind("<FocusOut>", delete_symbols())
    else:
        enter.delete(0, END)
        enter.insert(0, "Введено неверное число")
        enter.config(fg='red', font=('Arial', 11, 'bold'))
        enter.bind("<FocusOut>", delete_symbols())

#Создаем родительское окно
window = Tk()
window.title('Bot v2.0')
window.geometry('200x600')
window.columnconfigure([0], weight=1, minsize=150)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], weight=1, minsize=0)

#Устанавливаем стиль оформления
style = ttk.Style()
style.theme_use("vista")

#Создаем кнопки
button1 = ttk.Button(window, text='Питание ПК', width=15, command=power_PC)
button1.grid(column=0, row=0, sticky='wens')
button2 = ttk.Button(window, text='Браузер', width=15, command=browser)
button2.grid(column=0, row=1, sticky='wens')
button3 = ttk.Button(window, text='Система', width=15, command=system)
button3.grid(column=0, row=2, sticky='wens')
button4 = ttk.Button(window, text='Автокликер', width=15, command=AutoClicker)
button4.grid(column=0, row=3, sticky='wens')
button5 = ttk.Button(window, text='Починка ПК', width=15, command=Fixing_PC)
button5.grid(column=0, row=4, sticky='wens')
button6 = ttk.Button(window, text='Рандомайзер', width=15, command=Random)
button6.grid(column=0, row=5, sticky='wens')
button7 = ttk.Button(window, text='Настройки бота', width=15, command=setting_bot)
button7.grid(column=0, row=6, sticky='wens')
button8 = ttk.Button(window, text='Прочее', width=15, command=other)
button8.grid(column=0, row=7, sticky='wens')
button9 = ttk.Button(window, text='Поверх окон', width=15, command=lift)
button9.grid(column=0, row=8, sticky='wens')
button10 = ttk.Button(window, text='Не поверх окон', width=15, command=not_lift)
button10.grid(column=0, row=9, sticky='wens')
button11 = ttk.Button(window, text='Перейти', width=10, command=files)
button11.grid(column=0, row=11, sticky='wens')

#Нажатие клавиши "enter" переходит по введенной горячей клавише в функцию press_enter
window.bind('<Return>', press_enter)

#Поле ввода для ввода горячих клавиш с placeholder
class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="Пишите здесь...", color='grey', *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)
        self._add_placeholder()

    def _clear_placeholder(self, event):
        if self['fg'] == self.placeholder_color:
            self.delete(0, END)
            self['fg'] = self.default_fg_color

    def _add_placeholder(self, event=None):
        if not self.get():
            self.insert(0, self.placeholder)
            self['fg'] = self.placeholder_color

enter = EntryWithPlaceholder(window, font=('Arial', 14, 'bold'), placeholder="Пишите здесь...", width=30)
enter.grid(column=0, row=10)
enter.focus()
window.mainloop()