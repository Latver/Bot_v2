# ##########################################################
# Autor's: LATVER/Delei                                    #
# Браузер: открывает сайты в браузере                      #
############################################################

from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
import os, re
from Manager_Sites import App

PATH = os.path.dirname(os.path.abspath(__file__))

class func_browser:
    def vk():
        def news():
            os.system('explorer https://vk.com/feed')

        def messages():
            os.system('explorer https://vk.com/im')

        def my_page():
            os.system('explorer https://vk.com/id0')

        top = Tk()
        top.title('VK')
        top.geometry('200x200')

        top.columnconfigure([0], weight = 1, minsize = 60)
        top.rowconfigure([0, 1, 2], weight = 1, minsize = 50)

        topbut1 = Button(top, text = 'Новости', font = ('Verdana', 10, 'bold'), fg = 'black', bg = 'white', command = news).grid(column = 0, row = 0, stick = 'wens')
        topbut2 = Button(top, text = 'Сообщения', font = ('Verdana', 10, 'bold'), fg = 'black', bg = 'white', command = messages).grid(column = 0, row = 1, stick = 'wens')
        topbut3 = Button(top, text = 'Моя страница', font = ('Verdana', 10, 'bold'), fg = 'black', bg = 'white', command = my_page).grid(column = 0, row = 2, stick = 'wens')

    def youtube():
        os.system('explorer https://youtube.com')

    def vk_and_youtube():
        os.system('explorer https://youtube.com')
        os.system('explorer https://vk.com/id0')

    def google_translate():
        os.system('explorer https://translate.yandex.ru/')

    def google_disk():
        os.system('explorer https://drive.google.com/drive')

    def gmail():
        os.system('explorer https://gmail.com')

    def exit_menu_com():
        try:
            os.startfile(PATH + r'\Bot_main_menu.py')
            sys.exit()
        except WindowsError:
            error = Tk()
            error.title('Ошибка!')
            error.geometry('310x80')

            error.columnconfigure([0], weight = 1, minsize = 150)
            error.rowconfigure([0], weight = 1, minsize = 0)
            
            error_lbl = Label(error, text = 'Ошибка: Не найден файл "Bot_main_menu.py"', font = ('Verdana', 10, 'bold'), fg = 'red').grid(column = 0, row = 0, stick = 'wens')

    def menu():

        def read_site_com():
            read = open('C:\\Users\\' + os.environ['USERNAME'] + '\\Desktop\\Sites.txt', 'r')

        def save_site_com():
            opens = adress.get()

            write = open('C:\\Users\\' + os.environ['USERNAME'] + '\\Desktop\\Sites.txt', 'a')
            write.write(opens)

            write.close()

        def sites_open():
            def clear_button():
                site_listbox.delete(0, tk.END)


            def add_site():
                site = site_entry.get().strip()
                if site:
                    site_listbox.insert(tk.END, site)
                    site_entry.delete(0, tk.END)

            def delete_site():
                selection = site_listbox.curselection()
                if selection:
                    site_listbox.delete(selection)

            def save_sites():
                filename = filename_entry.get().strip()
                if filename:
                    if not filename.endswith('.txt'):
                        filename += '.txt'
                    with open(filename, 'w') as f:
                        for site in site_listbox.get(0, tk.END):
                            f.write(site + '\n')
                    filename_entry.delete(0, tk.END)
                    messagebox.showinfo("Сохранение", "Список сайтов сохранен")
                else:
                    messagebox.showerror("Ошибка", "Введите имя файла для сохранения")

            def load_sites():
                filename = filedialog.askopenfilename(filetypes=(("Text Files", "*.txt"),))
                if filename:
                    with open(filename, 'r') as f:
                        site_listbox.delete(0, tk.END)
                        for line in f:
                            site = line.strip()
                            if site:
                                site_listbox.insert(tk.END, site)
                    messagebox.showinfo("Загрузка", "Список сайтов загружен")
                else:
                    messagebox.showwarning("Предупреждение", "Не выбран файл для загрузки")

            directory = r'C:\Users\{}\Desktop\sites'.format(os.environ["USERNAME"])  # Абсолютный путь к директории

            window = tk.Tk()
            window.title("Менеджер сайтов")
            window.geometry("400x600")
            window.protocol('WM_DELETE_WIN', func_browser.menu)

            # Создаем основной фрейм
            main_frame = tk.Frame(window)
            main_frame.pack(fill=tk.BOTH, expand=1)

            # Создаем фрейм для ввода нового сайта
            add_frame = tk.LabelFrame(main_frame, text="Добавить сайт", padx=10, pady=10)
            add_frame.pack(padx=10, pady=10)

            site_entry = tk.Entry(add_frame, width=30)
            site_entry.pack(side=tk.LEFT, padx=5)

            add_button = tk.Button(add_frame, text="Добавить", command=add_site)
            add_button.pack(side=tk.LEFT, padx=5)

            # Создаем фрейм для списка сохраненных сайтов
            list_frame = tk.LabelFrame(main_frame, text="Список сайтов", padx=10, pady=10)
            list_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=1)

            site_listbox = tk.Listbox(list_frame, width=40)
            site_listbox.pack(fill=tk.BOTH, expand=1)

            # Создаем фрейм для кнопок управления списком сайтов
            button_frame = tk.Frame(list_frame)
            button_frame.pack(pady=5)

            delete_button = tk.Button(button_frame, text="Удалить", command=delete_site)
            delete_button.pack(side=tk.LEFT)

            clear_button = tk.Button(button_frame, text="Очистить", command=clear_button)
            clear_button.pack(side=tk.LEFT, padx=5)

            # Создаем фрейм для сохранения списка сайтов
            save_frame = tk.LabelFrame(main_frame, text="Сохранить список", padx=10, pady=10)
            save_frame.pack(padx=10, pady=10)

            filename_entry = tk.Entry(save_frame, width=30)
            filename_entry.pack(side=tk.LEFT, padx=5)

            save_button = tk.Button(save_frame, text="Сохранить", command=save_sites)
            save_button.pack(side=tk.LEFT, padx=5)

            # Создаем фрейм для загрузки списка сайтов
            load_frame = tk.LabelFrame(main_frame, text="Загрузить список", padx=10, pady=10)
            load_frame.pack(padx=10, pady=10)

            load_button = tk.Button(load_frame, text="Загрузить", command=load_sites)
            load_button.pack()

            window.mainloop()

        win = Tk() # Окно
        win.geometry(f"250x300")      # Размер окна
        win['bg'] = '#d3d3d3'      # Фон окна
        win.title('Браузер')

        win.columnconfigure([0], weight=3, minsize=0)
        win.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=3, minsize=0)

        button1 = Button(win, text = 'Вконтакте + YouTube', bd=1, font = ('Verdana', 10, 'bold'), fg = 'black', bg = 'white', command = func_browser.vk_and_youtube).grid(row = 0, column = 0, columnspan = 4, stick = 'wens')
        button2 = Button(win, text = 'Вконтакте', bd=1, font = ('Verdana', 10, 'bold'), fg = 'black', bg = 'white', command = func_browser.vk).grid(row = 1, column = 0, columnspan = 4, stick = 'wens')
        button3 = Button(win, text = 'YouTube', bd=1, font = ('Verdana', 10, 'bold'), fg = 'black', bg = 'white', command = func_browser.youtube).grid(row = 2, column = 0, columnspan = 4, stick = 'wens')
        button4 = Button(win, text = 'Переводчик', bd=1, font = ('Verdana', 10, 'bold'), fg = 'black', bg = 'white', command = func_browser.google_translate).grid(row = 3, column = 0, columnspan = 4, stick = 'wens')
        button5 = Button(win, text = 'Google Диск', bd=1, font = ('Verdana', 10, 'bold'), fg = 'black', bg = 'white', command = func_browser.google_disk).grid(row = 4, column = 0, columnspan = 4, stick = 'wens')
        button6 = Button(win, text = 'Gmail', bd=1, font = ('Verdana', 10, 'bold'), fg = 'black', bg = 'white', command = func_browser.gmail).grid(row = 5, column = 0, columnspan = 4, stick = 'wens')
        button8 = Button(win, text = 'Менеджер сайтов', bd=1, font = ('Verdana', 10, 'bold'), fg = 'purple', bg = 'white', command = sites_open).grid(row = 6, column = 0, columnspan = 4, stick = 'wens')

        win.mainloop()