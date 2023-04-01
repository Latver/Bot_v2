# -*- coding: utf-8 -*-

########################################################################################
# Autor: LATVER                                                                        #
# AutoClicker: автоматически нажимает левую клавишу мыши неограниченное количество раз #
########################################################################################

# Библиотеки
from tkinter import *
import pyautogui, keyboard, threading, os, sys, time

# Путь до файла
PATH = os.path.dirname(os.path.abspath(__file__))

# Справка о баге
def bug():
    bug_win = Tk()
    bug_win.title("Подсказка")
    bug_win.geometry("580x70")
    bug_win.columnconfigure([0], weight = 1, minsize = 150)
    bug_win.rowconfigure([0], weight = 1, minsize = 0)

    label_bug = Label(
        bug_win,
        font=("Verdana", 10, "bold"),
        text="Если вы хотите больше кликов чем 3 в секунду,\nто нажмите на кнопку автокликера несколько раз и клик суммируется.\nЕсли вы выберете для каждого клика свою клавишу, то при нажатии на нее,\nбудет происходит тот клик, на который вы назначили клавишу.",
        fg="black",
    ).grid(column=0, row=0)

# Справка об автокликере
def reference():
    ref_win = Tk()
    ref_win.title("Справка")
    ref_win.geometry("498x113")
    ref_win.columnconfigure([0], weight = 1, minsize = 150)
    ref_win.rowconfigure([0], weight = 1, minsize = 0)

    label_ref = Label(
        ref_win,
        font=("Verdana", 10, "bold"),
        text="Если удерживать клавишу контролирующего клика,\nто клик будет происходить по вашему нажатию на клавишу.\nЕсли нажать клавишу 1, то автокликер будет постоянно кликать.\nЕсли нажать клавишу 2, то авктокликер перестанет кликать.\nЕсли нажать клавишу 3, то автокликер завершит работу",
        fg="black",
    ).grid(column=0, row=0)

    ref_button = Button(
        ref_win,
        text="Подсказка",
        font=("Verdana", 10, "bold"),
        width=15,
        height=1,
        command=bug,
        bg="#d3d3d3",
        fg="red",
    ).grid(column=0, row=1, stick="wens")

# Автокликер
class status_on:

    # Один клик в секунду
    def one_click_win():
        global win
        global button1
        global status

        # Поток для одного клика
        def thread1():
            threading.Thread(target=all_clicks_one).start()

        counter = 0

        def clicks_one():
            nonlocal counter
            nonlocal enter_one_win
            value = enter_one_win.get()
            counter += 1
            label_one_win.configure(font = ('Verdana', 8, 'bold'), text = 'Вы назначили контролирующую клавишу "' + str(value) + '"\nВы нажали на кнопку запуск ' + str(counter) + ' раз\nВаш текущий клик: ' + str(counter) + ' раз в секунду')

        # Функция выполнения одного клика
        def one_click():

            # Отключение поля ввода
            enter_one_win.configure(state=DISABLED)

            value = enter_one_win.get()
            # Проверка клавиш
            if value == "1":
                one_win.destroy()

                key_error = Tk()
                key_error.title("Ошибка!")
                key_error.geometry("490x58")

                key_error.columnconfigure([0, 1], minsize=0)
                key_error.rowconfigure([0], minsize=0)

                key_label = Label(
                    key_error,
                    font=("Verdana", 16, "bold"),
                    text='Невозможно использовать клавишу "1"',
                    fg="red",
                    bg="white",
                ).grid(column=0, row=0)

                key_error_button = Button(key_error, font = ('Verdana', 10, 'bold'), text = 'Как пользоваться?', fg = 'red', bg = '#d3d3d3', command = reference).grid(column = 0, row = 1, stick = 'wens')
                key_error.mainloop()

            elif value == "2":
                one_win.destroy()

                key_error = Tk()
                key_error.title("Ошибка!")
                key_error.geometry("490x58")

                key_error.columnconfigure([0, 1], minsize=0)
                key_error.rowconfigure([0], minsize=0)

                key_label = Label(
                    key_error,
                    font=("Verdana", 16, "bold"),
                    text='Невозможно использовать клавишу "1"',
                    fg="red",
                    bg="white",
                ).grid(column=0, row=0)

                key_error_button = Button(key_error, font = ('Verdana', 10, 'bold'), text = 'Как пользоваться?', fg = 'red', bg = '#d3d3d3', command = reference).grid(column = 0, row = 1, stick = 'wens')
                key_error.mainloop()

            elif value == "3":
                one_win.destroy()

                key_error = Tk()
                key_error.title("Ошибка!")
                key_error.geometry("490x58")

                key_error.columnconfigure([0, 1], minsize=0)
                key_error.rowconfigure([0], minsize=0)

                key_label = Label(
                    key_error,
                    font=("Verdana", 16, "bold"),
                    text='Невозможно использовать клавишу "1"',
                    fg="red",
                    bg="white",
                ).grid(column=0, row=0)

                key_error_button = Button(key_error, font = ('Verdana', 10, 'bold'), text = 'Как пользоваться?', fg = 'red', bg = '#d3d3d3', command = reference).grid(column = 0, row = 1, stick = 'wens')
                key_error.mainloop()

            else:
                try:

                    # Цикл работы автокликера
                    while True:

                        # Автокликер запущен, клавиша нажата
                        if keyboard.is_pressed(value):

                            # Функция одного клика в секунду при контролирующей клавише
                            pyautogui.click()

                        # Автокликер запущен
                        elif keyboard.is_pressed("1"):

                            # Цикл работы автокликера при нажатии клавиши "1"
                            while True:
                                # Функция одного клика в секунду
                                pyautogui.click()

                                # Автокликер не запущен
                                if keyboard.is_pressed("2"):

                                    # Выход из цикла в предыдущий
                                    break

                                # Выход из кода в главное меню
                                elif keyboard.is_pressed("3"):

                                    # Родительское окно поверх всех
                                    win.attributes("-topmost", True)

                                    # Уничтожение окна с контролирующим кликом
                                    one_win.destroy()

                                    # Родительское окно не поверх всех
                                    win.attributes("-topmost", False)

                                    button4.configure(state = NORMAL)

                                    # Выход из цикла
                                    return

                        # Выход из кода в главное меню
                        elif keyboard.is_pressed("3"):

                            # Уничтожение окна с контролирующим кликом
                            one_win.destroy()

                            # Выход из цикла
                            return
                except ValueError:
                    one_win.destroy()

                    error = Tk()
                    error.title("Не введен символ!")
                    error.geometry("400x80")

                    error.columnconfigure([0], weight=1, minsize=150)
                    error.rowconfigure([0], weight=1, minsize=0)

                    error_lbl = Label(
                        error,
                        text="Ошибка: Введите пожалуйста любой символ",
                        font=("Verdana", 10, "bold"),
                        fg="red",
                    ).grid(column=0, row=0, stick="wens")
                    error.mainloop()

        def all_clicks_one():
            clicks_one()
            one_click()

        # Окно одного клика в секунду

        one_win = Tk()
        one_win.title("Один клик")
        one_win.geometry("370x150")

        one_win.rowconfigure([0, 1, 2], weight=15, minsize=0)
        one_win.columnconfigure([0], weight=15, minsize=0)

        label_one_win = Label(
            one_win,
            text="Назначьте клавишу контролирующего клика",
            font=("Verdana", 9, "bold"),
        )
        label_one_win.grid(column=0, row=0)
        
        enter_one_win = Entry(
            one_win, font=("Verdana", 10, "bold"), bg="#d3d3d3", fg="black"
        )
        enter_one_win.grid(column=0, row=1)

        one_win_button = Button(
            one_win,
            text="Запуск",
            font=("Verdana", 10, "bold"),
            width=15,
            height=1,
            command=thread1,
            bg="white",
            fg="black",
        )
        one_win_button.grid(column=0, row=2, stick="wens")
        two_win_button = Button(
            one_win,
            text="Справка",
            font=("Verdana", 10, "bold"),
            width=15,
            height=1,
            command=reference,
            bg="white",
            fg="black",
        ).grid(column=0, row=3, stick="wens")
        one_win.mainloop()

    # Двойной клик
    def two_click_win():
        global win

        # Поток двойного клика в секунду
        def thread2():
            threading.Thread(target=all_clicks_two).start()

        counter = 0
        dbs = 0

        def clicks_two():
            nonlocal counter
            nonlocal dbs
            nonlocal enter_two_win
            value = enter_two_win.get()
            dbs += 2
            counter += 1
            label_two_win.configure(font = ('Verdana', 8, 'bold'), text = 'Вы назначили контролирующую клавишу "' + str(value) + '"\nВы нажали на кнопку запуск ' + str(counter) + ' раз\nВаш текущий клик: ' + str(dbs) + ' раз в секунду')

        # Функция выполнения двойного клика в секунду
        def two_click():
            nonlocal two_win
            nonlocal enter_two_win
            nonlocal one_win_button

            threading.Thread().start()

            enter_two_win.configure(state=DISABLED)

            try:
                value = enter_two_win.get()

                if value == "1":
                    two_win.destroy()

                    key_error = Tk()
                    key_error.title("Ошибка!")
                    key_error.geometry("490x58")

                    key_error.columnconfigure([0, 1], minsize=0)
                    key_error.rowconfigure([0], minsize=0)

                    key_label = Label(
                        key_error,
                        font=("Verdana", 16, "bold"),
                        text='Невозможно использовать клавишу "1"',
                        fg="red",
                        bg="white",
                    ).grid(column=0, row=0)

                    key_error_button = Button(key_error, font = ('Verdana', 10, 'bold'), text = 'Как пользоваться?', fg = 'red', bg = '#d3d3d3', command = reference).grid(column = 0, row = 1, stick = 'wens')
                    key_error.mainloop()

                elif value == "2":
                    two_win.destroy()

                    key_error = Tk()
                    key_error.title("Ошибка!")
                    key_error.geometry("490x58")

                    key_error.columnconfigure([0, 1], minsize=0)
                    key_error.rowconfigure([0], minsize=0)

                    key_label = Label(
                        key_error,
                        font=("Verdana", 16, "bold"),
                        text='Невозможно использовать клавишу "1"',
                        fg="red",
                        bg="white",
                    ).grid(column=0, row=0)

                    key_error_button = Button(key_error, font = ('Verdana', 10, 'bold'), text = 'Как пользоваться?', fg = 'red', bg = '#d3d3d3', command = reference).grid(column = 0, row = 1, stick = 'wens')
                    key_error.mainloop()

                elif value == "3":
                    two_win.destroy()

                    key_error = Tk()
                    key_error.title("Ошибка!")
                    key_error.geometry("490x58")

                    key_error.columnconfigure([0, 1], minsize=0)
                    key_error.rowconfigure([0], minsize=0)

                    key_label = Label(
                        key_error,
                        font=("Verdana", 16, "bold"),
                        text='Невозможно использовать клавишу "1"',
                        fg="red",
                        bg="white",
                    ).grid(column=0, row=0)

                    key_error_button = Button(key_error, font = ('Verdana', 10, 'bold'), text = 'Как пользоваться?', fg = 'red', bg = '#d3d3d3', command = reference).grid(column = 0, row = 1, stick = 'wens')
                    key_error.mainloop()

                else:
                    
                    while True:
                        if keyboard.is_pressed(value):
                            threading.Thread().start()
                            # Автокликер запущен, клавиша нажата
                            pyautogui.doubleClick()
                        # Автокликер запущен
                        elif keyboard.is_pressed("1"):
                            threading.Thread().start()
                            while True:
                                pyautogui.doubleClick()
                                # Автокликер не запущен
                                if keyboard.is_pressed("2"):
                                    break
                                # Выход из кода в главное меню
                                elif keyboard.is_pressed("3"):
                                    two_win.destroy()
                                    return
                        # Выход из кода в главное меню
                        elif keyboard.is_pressed("3"):
                            two_win.destroy()
                            return
            except ValueError:
                two_win.destroy()

                error = Tk()
                error.title("Не введен символ!")
                error.geometry("400x80")

                error.columnconfigure([0], weight=1, minsize=150)
                error.rowconfigure([0], weight=1, minsize=0)

                error_lbl = Label(
                    error,
                    text="Ошибка: Введите пожалуйста один любой символ",
                    font=("Verdana", 10, "bold"),
                    fg="red",
                ).grid(column=0, row=0)
                error.mainloop()

        def all_clicks_two():
            clicks_two()
            two_click()

        # Окно двойного клика

        two_win = Tk()
        two_win.title("Два клика")
        two_win.geometry("370x150")

        two_win.rowconfigure([0, 1, 2], weight=15, minsize=0)
        two_win.columnconfigure([0], weight=15, minsize=0)

        label_two_win = Label(
            two_win,
            text="Назначьте клавишу контролирующего клика",
            font=("Verdana", 9, "bold"),
        )
        label_two_win.grid(column=0, row=0)
        enter_two_win = Entry(
            two_win, font=("Verdana", 10, "bold"), bg="#d3d3d3", fg="black"
        )
        enter_two_win.grid(column=0, row=1)

        one_win_button = Button(
            two_win,
            text="Запуск",
            font=("Verdana", 10, "bold"),
            width=15,
            height=1,
            command=thread2,
            bg="white",
            fg="black",
        )
        one_win_button.grid(column=0, row=2, stick="wens")
        two_win_button = Button(
            two_win,
            text="Справка",
            font=("Verdana", 10, "bold"),
            width=15,
            height=1,
            command=reference,
            bg="white",
            fg="black",
        ).grid(column=0, row=3, stick="wens")
        two_win.mainloop()
        key_error.mainloop()

    # Тройной клик
    def three_click_win():
        global win

        # Поток для тройного клика
        def thread3():
            threading.Thread(target=all_clicks_three).start()

        counter = 0
        dbs = 0

        def clicks_three():
            nonlocal counter
            nonlocal dbs
            nonlocal enter_three_win
            value = enter_three_win.get()
            dbs += 3
            counter += 1
            label_three_win.configure(font = ('Verdana', 8, 'bold'), text = 'Вы назначили контролирующую клавишу "' + str(value) + '"\nВы нажали на кнопку запуск ' + str(counter) + ' раз\nВаш текущий клик: ' + str(dbs) + ' раз в секунду')


        # Функция выполнения тройного клика в секунду
        def three_click():
            global win
            nonlocal three_win
            nonlocal enter_three_win
            nonlocal one_win_button

            enter_three_win.configure(state=DISABLED)

            try:
                value = enter_three_win.get()

                if value == "1":
                    three_win.destroy()

                    key_error = Tk()
                    key_error.title("Ошибка!")
                    key_error.geometry("490x58")

                    key_error.columnconfigure([0, 1], minsize=0)
                    key_error.rowconfigure([0], minsize=0)

                    key_label = Label(
                        key_error,
                        font=("Verdana", 16, "bold"),
                        text='Невозможно использовать клавишу "1"',
                        fg="red",
                        bg="white",
                    ).grid(column=0, row=0)

                    key_error_button = Button(key_error, font = ('Verdana', 10, 'bold'), text = 'Как пользоваться?', fg = 'red', bg = '#d3d3d3', command = reference).grid(column = 0, row = 1, stick = 'wens')
                    key_error.mainloop()

                elif value == "2":
                    three_win.destroy()

                    key_error = Tk()
                    key_error.title("Ошибка!")
                    key_error.geometry("490x58")

                    key_error.columnconfigure([0, 1], minsize=0)
                    key_error.rowconfigure([0], minsize=0)

                    key_label = Label(
                        key_error,
                        font=("Verdana", 16, "bold"),
                        text='Невозможно использовать клавишу "1"',
                        fg="red",
                        bg="white",
                    ).grid(column=0, row=0)

                    key_error_button = Button(key_error, font = ('Verdana', 10, 'bold'), text = 'Как пользоваться?', fg = 'red', bg = '#d3d3d3', command = reference).grid(column = 0, row = 1, stick = 'wens')
                    key_error.mainloop()

                elif value == "3":
                    three_win.destroy()

                    key_error = Tk()
                    key_error.title("Ошибка!")
                    key_error.geometry("490x58")

                    key_error.columnconfigure([0, 1], minsize=0)
                    key_error.rowconfigure([0], minsize=0)

                    key_label = Label(
                        key_error,
                        font=("Verdana", 16, "bold"),
                        text='Невозможно использовать клавишу "1"',
                        fg="red",
                        bg="white",
                    ).grid(column=0, row=0)

                    key_error_button = Button(key_error, font = ('Verdana', 10, 'bold'), text = 'Как пользоваться?', fg = 'red', bg = '#d3d3d3', command = reference).grid(column = 0, row = 1, stick = 'wens')
                    key_error.mainloop()

                else:

                    while True:
                        if keyboard.is_pressed(value):
                            threading.Thread().start()
                            # Автокликер запущен, клавиша нажата
                            pyautogui.tripleClick()
                        # Автокликер запущен
                        elif keyboard.is_pressed("1"):
                            threading.Thread().start()
                            while True:
                                pyautogui.tripleClick()
                                # Автокликер не запущен
                                if keyboard.is_pressed("2"):
                                    break
                                # Выход из кода в главное меню
                                elif keyboard.is_pressed("3"):
                                    three_win.destroy()
                                    return
                        # Выход из кода в главное меню
                        elif keyboard.is_pressed("3"):
                            three_win.destroy()
                            return
            except ValueError:
                three_win.destroy()

                error = Tk()
                error.title("Не введен символ!")
                error.geometry("400x80")

                error.columnconfigure([0], weight=1, minsize=150)
                error.rowconfigure([0], weight=1, minsize=0)

                error_lbl = Label(
                    error,
                    text="Ошибка: Введите пожалуйста один любой символ",
                    font=("Verdana", 10, "bold"),
                    fg="red",
                ).grid(column=0, row=0, stick="wens")
                error.mainloop()

        def all_clicks_three():
            clicks_three()
            three_click()

        # Окно тройного клика в секунду

        three_win = Tk()
        three_win.title("Три кликa")
        three_win.geometry("370x150")

        three_win.rowconfigure([0, 1, 2], weight=15, minsize=0)
        three_win.columnconfigure([0], weight=15, minsize=0)

        label_three_win = Label(
            three_win,
            text="Назначьте клавишу контролирующего клика",
            font=("Verdana", 9, "bold"),
        )
        label_three_win.grid(column=0, row=0)

        enter_three_win = Entry(
            three_win, font=("Verdana", 10, "bold"), bg="#d3d3d3", fg="black"
        )
        enter_three_win.grid(column=0, row=1)

        one_win_button = Button(
            three_win,
            text="Запуск",
            font=("Verdana", 10, "bold"),
            width=15,
            height=1,
            command=thread3,
            bg="white",
            fg="black",
        )
        one_win_button.grid(column=0, row=2, stick="wens")
        two_win_button = Button(
            three_win,
            text="Справка",
            font=("Verdana", 10, "bold"),
            width=15,
            height=1,
            command=reference,
            bg="white",
            fg="black",
        ).grid(column=0, row=3, stick="wens")
        three_win.mainloop()


    # Автокликер
    def status():
        status_win = Tk()
        status_win.title("Автокликер")
        status_win.geometry("350x200")

        status_win.columnconfigure([0], weight=15, minsize=0)
        status_win.rowconfigure([0, 1, 2], weight=15, minsize=0)

        button1 = Button(
            status_win,
            text="1 клик в секунду",
            font=("Verdana", 10, "bold"),
            width=15,
            height=1,
            command=status_on.one_click_win,
            bg="white",
            fg="black",
        ).grid(column=0, row=0, stick="wens")
        button2 = Button(
            status_win,
            text="2 клика в секунду",
            font=("Verdana", 10, "bold"),
            width=15,
            height=1,
            command=status_on.two_click_win,
            bg="white",
            fg="black",
        ).grid(column=0, row=1, stick="wens")
        button3 = Button(
            status_win,
            text="3 клика в секунду",
            font=("Verdana", 10, "bold"),
            width=15,
            height=1,
            command=status_on.three_click_win,
            bg="white",
            fg="black",
        ).grid(column=0, row=2, stick="wens")
        status_win.mainloop()

    def window_menu():

        # Выход в главное меню
        def exit_menu():
            try:
                nonlocal win
                win.destroy()
                os.startfile(PATH + r'\Bot_main_menu.py')
            except WindowsError:
                error = Tk()
                error.title("Ошибка!")
                error.geometry("310x80")

                error.columnconfigure([0], weight=1, minsize=150)
                error.rowconfigure([0], weight=1, minsize=0)

                error_lbl = Label(
                    error,
                    text='Ошибка: Не найден файл "Bot_v2.0.py"',
                    font=("Verdana", 10, "bold"),
                    fg="red",
                ).grid(column=0, row=0, stick="wens")
                error.mainloop()

        # Родительское окно
        win = Tk()
        win.title("Автокликер")
        win.geometry("300x250")
        win.protocol('WM_DELETE_WINDOW', exit_menu)

        win.rowconfigure([0, 1, 2], weight=15, minsize=0)
        win.columnconfigure([0], weight=15, minsize=0)

        button1 = Button(
            win,
            text="Запуск автокликера",
            font=("Verdana", 10, "bold"),
            width=15,
            height=1,
            command=status_on.status,
            bg="white",
            fg="black",
        )
        button1.grid(column=0, row=0, stick="wens")

        button2 = Button(
            win,
            text="Как использовать?",
            font=("Verdana", 10, "bold"),
            width=15,
            height=1,
            command=reference,
            bg="white",
            fg="red",
        ).grid(column=0, row=1, stick="wens")

        button4 = Button(
            win,
            text="Выход в главное меню",
            font=("Verdana", 10, "bold"),
            width=15,
            height=1,
            command=exit_menu,
            bg="white",
            fg="green",
        )
        button4.grid(column=0, row=2, stick="wens")

        win.mainloop()