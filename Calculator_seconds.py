################################################################################################################################################
# Autor's: LATVER/DeLeei                                                                                                                       #
# Калькулятор секунд: Расчитывает часы/минуты/секунды в секунды, имеет возможность выключения/перезагрузки/сна/выхода из системы ПК по таймеру #
################################################################################################################################################

import tkinter as tk
import re, os

#Путь до файла
PATH = os.path.dirname(os.path.abspath(__file__))

class calc_sec:

    #Функция кнопки
    timer = '0'
    def menu():

        #Выключение/Перезагрузка/Сон/Выход из системы/Отмена неизбежного выключения
        def shutdown():
            timing = result()
            os.system(f'shutdown /s /t {timing} /f /c "Компьютер скоро будет выключен. Сохраните свои документы!"')
        def reboot():
            timing = result()
            os.system(f'shutdown /r /t {timing} /f /c "Компьютер скоро будет перезагружен. Сохраните свои документы!"')
        def sleep_pc():
            timing = result()
            os.system(f'timeout /t {timing} && rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
        def cancel():
            os.system('shutdown /a')
            time_1.configure(text = f'Отмена неизбежного выключения', font = ('Verdana', 10, 'bold'), bg = '#d3d3d3', fg = 'black')

        def enter_result(Return):
            result()

        def result():
            h1 = hours1.get()
            m1 = minutes1.get()
            s1 = seconds1.get()

            if re.search('-', h1):
                time_1.configure(text = f'Ошибка: Отрицательное значение в часах', font = ('Verdana', 10, 'bold'), bg = '#d3d3d3', fg = 'red')
            elif re.search('-', m1):
                time_1.configure(text = f'Ошибка: Отрицательное значение в минутах', font = ('Verdana', 10, 'bold'), bg = '#d3d3d3', fg = 'red')
            elif re.search('-', s1):
                time_1.configure(text = f'Ошибка: Отрицательное значение в секундах', font = ('Verdana', 10, 'bold'), bg = '#d3d3d3', fg = 'red')
            elif h1 == '':
                time_1.configure(text = f'Ошибка: Пустое значение в часах', font = ('Verdana', 10, 'bold'), bg = '#d3d3d3', fg = 'red')
            elif m1 == '':
                time_1.configure(text = f'Ошибка: Пустое значение в минутах', font = ('Verdana', 10, 'bold'), bg = '#d3d3d3', fg = 'red')
            elif s1 == '':
                time_1.configure(text = f'Ошибка: Пустое значение в секундах', font = ('Verdana', 10, 'bold'), bg = '#d3d3d3', fg = 'red')
            else:
                hours_in_seconds1 = int(h1) * 60
                hours_in_seconds2 = hours_in_seconds1 * 60
                minutes_in_seconds = int(m1) * 60
                final = hours_in_seconds2 + minutes_in_seconds + int(s1)
                timer = final
                time_1.configure(text = f'Результат: {timer} секунд', font = ('Verdana', 10, 'bold'), bg = '#d3d3d3', fg = 'black')
                return timer

        #Выход в Bot_v2.0
        def exit_menu():
            nonlocal win
            try:
                os.startfile(PATH + r'\Bot_main_menu.py')
                win.destroy()
            except WindowsError:
                error = Toplevel(win)
                error.title('Ошибка!')
                error.geometry('310x80')

                error.columnconfigure([0], weight = 1, minsize = 150)
                error.rowconfigure([0], weight = 1, minsize = 0)
                
                error_lbl = Label(error, text = 'Ошибка: Не найден файл "Bot_main_menu.py"', font = ('Verdana', 10, 'bold'), fg = 'red').grid(column = 0, row = 0, stick = 'wens')

        win = tk.Tk()
        win['bg'] = 'LightGrey'
        win.title('Калькулятор времени')
        win.bind('<Return>', enter_result)
        win.protocol('WM_DELETE_WINDOW', exit_menu)

        #Строки | Время
        hours1 = tk.Entry(win, width = 5)
        hours1.insert(0, '0')
        hours1.grid(row = 2, column = 0)

        minutes1 = tk.Entry(win, width = 5)
        minutes1.insert(0, '0')
        minutes1.grid(row = 2, column = 1)

        seconds1 = tk.Entry(win, width = 5)
        seconds1.insert(0, '0')
        seconds1.grid(row = 2, column = 2)

        #Текста обозначений
        hours = tk.Label(win, font = ('Verdana', 8, 'bold'))
        hours.grid(row = 0, column = 0, stick = 'wens')
        hours.configure(text = 'Часы', bg = '#d3d3d3')

        minutes = tk.Label(win, font = ('Verdana', 8, 'bold'))
        minutes.grid(row = 0, column = 1, stick = 'wens')
        minutes.configure(text = 'Минуты', bg = '#d3d3d3')

        seconds = tk.Label(win, font = ('Verdana', 8, 'bold'))
        seconds.grid(row = 0, column = 2, stick = 'wens')
        seconds.configure(text = 'Секунды', bg = '#d3d3d3')

        #Кнопки
        button1 = tk.Button(win, font = ('Verdana', 8, 'bold'), text = 'Рассчитать', width = 10, height = 2, command = result, fg = "green", bg = 'white').grid(column = 0, row = 4, columnspan = 4, stick = 'wens')
        button2 = tk.Button(win, font = ('Verdana', 8, 'bold'), text = 'Выключить ПК', width = 20, height = 2, command = shutdown, bg = 'white').grid(column = 0, row = 5, stick = 'wens')
        button3 = tk.Button(win, font = ('Verdana', 8, 'bold'), text = 'Перезагрузить ПК', width = 20, height = 2, command = reboot, bg = 'white').grid(column = 1, row = 5, stick = 'wens')
        button5 = tk.Button(win, font = ('Verdana', 8, 'bold'), text = 'Режим сна ПК', width = 20, height = 2, command = sleep_pc, bg = 'white').grid(column = 2, row = 5, stick = 'wens')
        button6 = tk.Button(win, font = ('Verdana', 8, 'bold'), text = 'Отмена неизбежного выключения', width = 10, height = 2, command = cancel, fg = "blue", bg = 'white').grid(column = 0, row = 6, columnspan = 4, stick = 'wens')
        button7 = tk.Button(win, font = ('Verdana', 8, 'bold'), text = 'Выход в главное меню', width = 10, height = 2, command = exit_menu, bg = 'white', fg = 'purple').grid(column = 0, row = 7, columnspan = 4, stick = 'wens')

        #Результат
        time_1 = tk.Label(win, font = ('Verdana', 8))
        time_1.grid(row = 8, column = 0, columnspan = 4, stick = 'wens')
        time_1.configure(font = ('Verdana', 10, 'bold'), bg = '#d3d3d3', fg = 'black')

        #Размеры по вертикали и горизонтали
        win.columnconfigure([0, 1, 2, 3], weight = 1, minsize = 0)
        win.rowconfigure([0, 1, 2, 3, 4, 5], weight = 1, minsize = 0)

        win.mainloop()