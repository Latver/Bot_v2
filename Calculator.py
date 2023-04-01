###################################################################################################################################
# Autor: Delei                                                                                                                    #
# Калькулятор: выполняет операции над числами и алгебраическими формулами                                                         #
# TODO: Сделать чтобы при нажатии на клавишу "enter" выводился результат расчетов, также при написании цифры должен убиратся ноль #
###################################################################################################################################

import tkinter as tk
import math, keyboard, os

def add_digit(digit):      # Функция добавления цифры в строку
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0,tk.END)
    calc.insert(0,value+digit)

def add_operation(operation):      # Функция добавления вычислительного знака
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        textcalc = tk.Label(calculate())
        textcalc.grid
    calc.delete(0,tk.END)
    calc.insert(0,value+operation)

def calculate():      # Функция вычисления
    value = calc.get()
    π = 3.14159265359
    if keyboard.is_pressed('enter'):
        if value[-1] in '+-/*':
            value = value+value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,eval(value))

def clear():      # Функция очистки строки
    calc.delete(0,tk.END)
    calc.insert(0, 0)

def pi():      # Функция числа Пи
    calc.insert('π')

def sin():      # Функция синуса
    calc.insert(tk.END, '= ' + str(math.sin(int(calc.get()))))

def cos():      # Функция косинуса
    calc.insert(tk.END, '= ' + str(math.cos(int(calc.get()))))

def tan():      # Функция тангенса
    calc.insert(tk.END, '= ' + str(math.tan(int(calc.get()))))
    

def make_digit_button(digit):      # Кнопки с цифрами
    return tk.Button(text = digit, bd=1, font = ('Arial', 13), fg = 'black', bg = 'white', command=lambda : add_digit(digit))

def make_operation_button(operation):      # Кнопка '+', '-', '/', '*'
    return tk.Button(text = operation, bd=1, font = ('Arial', 15), fg = 'black', bg = 'LightGrey', command=lambda : add_operation(operation))

def make_calc_button(operation):      # Кнопка '='
    return tk.Button(text = operation, bd=1, font = ('Arial', 15), fg = 'black', bg = 'LightGrey', command=calculate)

def make_clear_button(operation):      # Кнопка очистки
    return tk.Button(text = operation, bd=1, font = ('Arial', 13), fg = 'black', bg = 'white', command=clear)

def make_together_button(operation):      # Скобки
    return tk.Button(text = operation, bd=1, font = ('Arial', 15), fg = 'black', bg = 'white', command=lambda : add_digit(operation))

def make_pi_button(digit):      # Число Пи
    return tk.Button(text = digit, bd=1, font = ('Arial', 13), fg = 'black', bg = 'LightGrey', command=lambda : add_digit(digit))

def make_point_button(digit):      # Запятая
    return tk.Button(text = digit, bd=1, font = ('Arial', 15), fg = 'black', bg = 'white', command=lambda : add_digit(digit))

def make_percent_button(digit):      # Проценты
    return tk.Button(text = digit, bd=1, font = ('Arial', 14), fg = 'black', bg = 'LightGrey', command=lambda : add_digit(digit))

def make_sin_button(operation):      # Синус
    return tk.Button(text = operation, bd=1, font = ('Arial', 13), fg = 'black', bg = 'LightGrey', command=sin)

def make_cos_button(operation):      # Косинус
    return tk.Button(text = operation, bd=1, font = ('Arial', 13), fg = 'black', bg = 'LightGrey', command=cos)

def make_tan_button(operation):      # Тангенс
    return tk.Button(text = operation, bd=1, font = ('Arial', 13), fg = 'black', bg = 'LightGrey', command=tan)


win = tk.Tk() # Окно
win.geometry(f"299x299+100+200")      # Размер окна
win['bg'] = '#696969'      # Задний фон
win.title('Калькулятор')      # Заголовок окна

win.columnconfigure([0,1,2,3,4], weight=1, minsize=60)      # Растяжение окна по горизонтали
win.rowconfigure([0,1,2,3,4,5], weight=1, minsize=50)      # Растяжение окна по вертикали

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15))      # Строка
calc.insert(0, '0')      # Ноль
calc.grid(row = 0, column = 0, columnspan = 5, stick = 'wens')      # Размер строки

make_digit_button('1').grid(row = 4, column = 1, stick = 'wens')      # Кнопки цифр
make_digit_button('2').grid(row = 4, column = 2, stick = 'wens')
make_digit_button('3').grid(row = 4, column = 3, stick = 'wens')
make_digit_button('4').grid(row = 3, column = 1, stick = 'wens')
make_digit_button('5').grid(row = 3, column = 2, stick = 'wens')
make_digit_button('6').grid(row = 3, column = 3, stick = 'wens')
make_digit_button('7').grid(row = 2, column = 1, stick = 'wens')
make_digit_button('8').grid(row = 2, column = 2, stick = 'wens')
make_digit_button('9').grid(row = 2, column = 3, stick = 'wens')
make_digit_button('0').grid(row = 5, column = 1, columnspan = 2, stick = 'wens')

make_operation_button('+').grid(row = 4, column = 4, stick = 'wens')      # Кнопки вычислений
make_operation_button('-').grid(row = 3, column = 4, stick = 'wens')
make_operation_button('/').grid(row = 1, column = 4, stick = 'wens')
make_operation_button('*').grid(row = 2, column = 4, stick = 'wens')

make_calc_button('=').grid(row = 5, column = 4, stick = 'wens')      # Кнопка знака равно
make_clear_button('C').grid(row = 1, column = 1, stick = 'wens')      # Кнопка очистки строки

make_together_button('(').grid(row = 1, column = 2, stick = 'wens')      # Кнопка открытой скобки
make_together_button(')').grid(row = 1, column = 3, stick = 'wens')      # Кнопка закрытой скобки

make_pi_button('π').grid(row = 1, column = 0, stick = 'wens')      # Кнопка числа Пи

make_point_button('.').grid(row = 5, column = 3, stick = 'wens')      # Кнопка запятой

make_percent_button('%').grid(row = 2, column = 0, stick = 'wens')      # Кнопка процента

make_sin_button('sin').grid(row = 3, column = 0, stick = 'wens')      # Кнопка синуса
make_cos_button('cos').grid(row = 4, column = 0, stick = 'wens')      # Кнопка косинуса
make_tan_button('tan').grid(row = 5, column = 0, stick = 'wens')      # Кнопка тангенса

win.grid_columnconfigure(0,minsize = 60) #Размеры по горизонтали
win.grid_columnconfigure(1,minsize = 60)
win.grid_columnconfigure(2,minsize = 60)
win.grid_columnconfigure(3,minsize = 60)
win.grid_columnconfigure(4,minsize = 60)

win.grid_rowconfigure(0,minsize = 50) #Размеры по вертикали
win.grid_rowconfigure(1,minsize = 50)
win.grid_rowconfigure(2,minsize = 50)
win.grid_rowconfigure(3,minsize = 50)
win.grid_rowconfigure(4,minsize = 50)
win.grid_rowconfigure(5,minsize = 50)

win.mainloop()      # Показ окна