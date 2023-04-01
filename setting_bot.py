#####################################################
# Autor: LATVER                                     #
# Настройки бота: позволяет изменять настройки бота #
# TODO: Придумать еще функции                       #
#####################################################

from tkinter import *
import os, sys, time

PATH = os.path.dirname(os.path.abspath(__file__))
class setting_bot_win:
    global PATH
    def main():

        def new_win():

            def auto_launch():

                def exit_menu_4():
                    successfull_win.destroy()
                    window.deiconify()

                #Дополнительное окно
                nwin.withdraw()
                window.withdraw()
                os.system(r'copy /y "' + PATH + r'\Bot_v2.0.py" "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\"')
                successfull_win = Tk()
                successfull_win.title('Бот добавлен в автозагрузку!')
                successfull_win.geometry('400x100')
                successfull_win.columnconfigure([0], weight = 1, minsize = 150)
                successfull_win.rowconfigure([0], weight = 1, minsize = 0)
                successfull_win.protocol("WM_DELETE_WINDOW", exit_menu_4)

                #Текст
                label = Label(successfull_win, font = ('Verdana', 10, 'bold'), text = 'Бот успешно добавлен в автозагрузку!').grid(column = 0, row = 0)

            def not_launch():

                def exit_menu_3():
                    error_win.destroy()
                    window.deiconify()

                #Дополнительное окно
                nwin.withdraw()
                window.withdraw()
                os.system(r'del /F "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\Bot_v2.0.py"')
                error_win = Tk()
                error_win.title('Бот убран из автозагрузки!')
                error_win.geometry('400x100')
                error_win.columnconfigure([0], weight = 1, minsize = 150)
                error_win.rowconfigure([0], weight = 1, minsize = 0)
                error_win.protocol("WM_DELETE_WINDOW", exit_menu_3)

                #Текст
                label = Label(error_win, font = ('Verdana', 10, 'bold'), text = 'Бот успешно убран из автозагрузки!').grid(column = 0, row = 0)

            def exit_menu_2():
                nwin.destroy()
                window.deiconify()
                
            #Дополнительное окно
            window.withdraw()
            nwin = Tk()
            nwin.title('Автозагрузка')
            nwin.columnconfigure([0], weight = 1, minsize = 150)
            nwin.rowconfigure([0, 1], weight = 1, minsize = 0)
            nwin.protocol('WM_DELETE_WINDOW', exit_menu_2)

            #Кнопки
            but = Button(nwin, font = ('Verdana', 10, 'bold'), text = 'Добавить бота в автозагрузку', width = 55, height = 4, command = auto_launch).grid(column = 0, row = 0, stick = 'wens')  
            but2 = Button(nwin, font = ('Verdana', 10, 'bold'), text = 'Убрать бота из автозагрузки', width = 55, height = 4, command = not_launch).grid(column = 0, row = 1, stick = 'wens')

            nwin.mainloop()

        def exit_menu():
            window.destroy()
            os.system(PATH + r'\Bot_main_menu.py')

        #Родительское окно
        window = Tk()
        window.title('Настройки бота')
        window.columnconfigure([0], weight = 1, minsize = 150)
        window.rowconfigure([0], weight = 1, minsize = 0)
        window.protocol('WM_DELETE_WINDOW', exit_menu)

        #Кнопки
        button1 = Button(window, font = ('Verdana', 10, 'bold'), text = 'Автозагрузка', width = 35, height = 3, command = new_win).grid(column = 0, row = 0, stick = 'wens')

        window.mainloop()