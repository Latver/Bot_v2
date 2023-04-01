from tkinter import *
import random, re, os

#Путь до файлов
PATH = os.path.dirname(os.path.abspath(__file__))

class random_menu:
    def menu():

        def exit_menu_2():
            random_win.destroy()
            os.system(PATH + r'\Bot_main_menu.py')

        random_win = Tk()
        random_win.geometry(f'300x140')
        random_win['bg'] = 'LightGrey'
        random_win.title('Рандомайзер')
        random_win.protocol('WM_DELETE_WINDOW', exit_menu_2)

        random_win.columnconfigure([0,1,2,3], weight=1, minsize=60)
        random_win.rowconfigure([0,1,2,3,4,5,6], weight=1, minsize=70)

        def random_number_random_win():
            random_win.withdraw()

            def exit_menu():
                random_win_w_r.destroy()
                random_win.deiconify()

            def withdraw_generator_number():
                random_win_w_r.destroy()
                generator_number()

            def withdraw_random_number():
                random_win_w_r.destroy()
                random_number()

            random_win_w_r = Tk()
            random_win_w_r.geometry(f'300x140')
            random_win_w_r.title('Случайное число')
            random_win_w_r.protocol('WM_DELETE_WINDOW', exit_menu)

            random_win_w_r.columnconfigure([0,1,2,3], weight=1, minsize=60)
            random_win_w_r.rowconfigure([0,1,2,3,4,5,6], weight=1, minsize=70)

            button1 = Button(random_win_w_r, text = 'Случайное число \n от 1 до 100', bd=1, font = ('Verdana', 10, 'bold'), fg = 'black', bg = 'white', command = withdraw_random_number).grid(row = 0, column = 0, columnspan = 4, stick = 'wens')
            button2 = Button(random_win_w_r, text = 'Генератор чисел', bd=1, font = ('Verdana', 10, 'bold'), fg = 'black', bg = 'white', command = withdraw_generator_number).grid(row = 1, column = 0, columnspan = 4, stick = 'wens')

        def random_number():

            def exit_menu():
                random_win_r.destroy()
                random_number_random_win()

            random_win_r = Tk()
            random_win_r.geometry(f'300x100')
            random_win_r.title('Вывод')
            random_win_r.protocol('WM_DELETE_WINDOW', exit_menu)
        
            random_win_r.columnconfigure([0,1,2,3], weight=1, minsize=20)
            random_win_r.rowconfigure([0,1,2,3,4,5,6], weight=1, minsize=10)
        
            text_r = Label(random_win_r, font = ('Verdana', 15))
            text_r.grid(row = 3, column = 0, columnspan = 4, rowspan = 1, stick = 'wens')
            text_r.configure(text = f'Ваше число: {random.randint(0, 100)}')
        
        def generator_number():
            N = 'N'
        
            def enter_generate(Return):
                generate()

            def generate():
                b = before.get()
                t = to.get()
                if b > t:
                    text_f.grid(row = 6, column = 2, columnspan = 2, rowspan = 1, stick = 'wens')
                    text_f.configure(text = 'Ошибка!')
                b1 = int(b)
                t1 = int(t)
                N = random.randint(b1, t1)
                text_f.configure(text = f'Ваше число: {N}')

            random_win.withdraw()

            def exit_menu():
                random_win_g.destroy()
                random_number_random_win()

            random_win_g = Tk()
            random_win_g.geometry(f'300x100')
            random_win_g.title('Генератор чисел')
            random_win_g.bind('<Return>', enter_generate)
            random_win_g.protocol('WM_DELETE_WINDOW', exit_menu)
        
            random_win_g.columnconfigure([0,1,2,3,4,5,6], weight=1, minsize=10)
            random_win_g.rowconfigure([0,1,2,3,4,5,6], weight=1, minsize=10)
        
            text_g = Label(random_win_g, font = ('Verdana', 10))
            text_g.grid(row = 0, column = 0, columnspan = 2, rowspan = 1, stick = 'wens')
            text_g.configure(text = f'От')
        
            text2_g = Label(random_win_g, font = ('Verdana', 10))
            text2_g.grid(row = 1, column = 0, columnspan = 2, rowspan = 3, stick = 'wens')
            text2_g.configure(text = f'До')
        
            before = Entry(random_win_g, justify=LEFT, font = ('Verdana', 10))
            before.grid(row = 0, column = 2, columnspan = 1)
        
            to = Entry(random_win_g, justify=LEFT, font = ('Verdana', 10))
            to.grid(row = 1, column = 2, rowspan = 3, columnspan = 1)
        
            text_f = Label(random_win_g, font = ('Verdana', 10, 'bold'))
            text_f.grid(row = 6, column = 1, columnspan = 2, rowspan = 1, stick = 'wens')
            text_f.configure(text = f'Ваше число: {N}')
        
            button_r = Button(random_win_g, text = 'Сгенерировать', bd=1, font = ('Verdana', 10), fg = 'black', bg = 'white', command = generate).grid(row = 4, column = 1, columnspan = 3, stick = 'wens')
        
        def heads_or_tails():
            random_win.withdraw()

            def exit_menu():
                random_win_h.destroy()
                random_win.deiconify()

            random_win_h = Tk()
            random_win_h.geometry(f'300x100')
            random_win_h.title('Орёл или Решка')
            random_win_h.protocol('WM_DELETE_WINDOW', exit_menu)
            
            random_win_h.columnconfigure([0,1,2,3,4,5,6], weight=1, minsize=10)
            random_win_h.rowconfigure([0,1,2,3,4,5,6], weight=1, minsize=10)
        
            text_h = Label(random_win_h, font = ('Verdana', 17, 'bold'))
            text_h.grid(row = 3, column = 3, columnspan = 1, rowspan = 1, stick = 'wens')
            list = ['Орёл', 'Решка', 'Орёл', 'Решка']
            text_h.configure(text = f'{random.choice(list)}')
        
        button1 = Button(random_win, text = 'Случайное число', bd=1, font = ('Verdana', 10, 'bold'), fg = 'black', bg = 'white', command = random_number_random_win).grid(row = 0, column = 0, columnspan = 4, stick = 'wens')
        button3 = Button(random_win, text = 'Орёл или Решка', bd=1, font = ('Verdana', 10, 'bold'), fg = 'black', bg = 'white', command = heads_or_tails).grid(row = 1, column = 0, columnspan = 4, stick = 'wens')
    
        random_win.mainloop()