####################################################################################################
# Autor: LATVER                                                                                    #
# Питание ПК: служит чтобы принудительно завершать работу, также может завершать работу по таймеру #
# TODO: Сделать функции сон и выход из системы по таймеру                                          #
####################################################################################################

from tkinter import *
import os, time, threading
from Calculator_seconds import calc_sec

PATH = os.path.dirname(os.path.abspath(__file__))

#Меню
class menu_power_pc:
    def menu_pc():

        #Калькулятор секунд
        def Calc_sec():
            nonlocal window
            window.withdraw()
            calc_sec.menu()

        #Шаблоны
        def Power_off1():
            os.system('shutdown /s /t 1 /f')

        def Power_off2():
            os.system('shutdown /s /t 1800 /f')

        def Power_off3():
            os.system('shutdown /s /t 3600 /f')

        def Power_off4():
            os.system('shutdown /s /t 5400 /f')

        def Power_off5():
            os.system('shutdown /s /t 7200 /f')

        def Reboot1():
            os.system('shutdown /r /t 1 /f')

        def Reboot2():
            os.system('shutdown /r /t 1800 /f')

        def Reboot3():
            os.system('shutdown /r /t 3600 /f')

        def Reboot4():
            os.system('shutdown /r /t 5400 /f')

        def Reboot5():
            os.system('shutdown /r /t 7200 /f')

        def stop():
            os.system('shutdown /a')

        #Выключение ПК
        def Power_off():

            def exit_menu_4():
                win.destroy()
                window.deiconify()

            def templates():

                def exit_menu_5():
                    temp_win.destroy()
                    win.deiconify()

                win.withdraw()
                temp_win = Tk()
                temp_win.title('Шаблоны')
                temp_win.columnconfigure([0], weight = 1, minsize = 150)
                temp_win.rowconfigure([0, 1, 2, 3], weight = 1, minsize = 0)
                temp_win.protocol('WM_DELETE_WINDOW', exit_menu_5)

                button7 = Button(temp_win, font = ('Verdana', 10, 'bold'), text = 'Выключить ПК через 30 минут', width = 55, height = 3, command = Power_off2).grid(column = 0, row = 0, stick = 'wens')
                button8 = Button(temp_win, font = ('Verdana', 10, 'bold'), text = 'Выключить ПК через 1 час', width = 55, height = 3, command = Power_off3).grid(column = 0, row = 1, stick = 'wens')
                button9 = Button(temp_win, font = ('Verdana', 10, 'bold'), text = 'Выключить ПК через 1.5 часа', width = 55, height = 3, command = Power_off4).grid(column = 0, row = 2, stick = 'wens')
                button10 = Button(temp_win, font = ('Verdana', 10, 'bold'), text = 'Выключить ПК через 2 часа', width = 55, height = 3, command = Power_off5).grid(column = 0, row = 3, stick = 'wens')

                temp_win.mainloop()

            window.withdraw()
            win = Tk()
            win.title('Выключение ПК')
            win.columnconfigure([0], weight = 1, minsize = 150)
            win.rowconfigure([0, 1, 2, 3], weight = 1, minsize = 0)
            win.protocol('WM_DELETE_WINDOW', exit_menu_4)

            button6 = Button(win, font = ('Verdana', 10, 'bold'), text = 'Выключить ПК', width = 35, height = 3, command = Reboot1).grid(column = 0, row = 0, stick = 'wens')
            button14 = Button(win, font = ('Verdana', 10, 'bold'), text = 'Шаблоны', width = 35, height = 3, command = templates).grid(column = 0, row = 1, stick = 'wens')
            button11 = Button(win, font = ('Verdana', 10, 'bold'), text = 'Отмена неизбежного выключения', width = 35, height = 3, command = stop, fg = 'red').grid(column = 0, row = 2, stick = 'wens')

            win.mainloop()

        #Перезагрузка ПК
        def Reboot():

            def exit_menu_2():
                win.destroy()
                window.deiconify()

            def templates2():

                def exit_menu_3():
                    temp_win.destroy()
                    win.deiconify()

                win.withdraw()
                temp_win = Tk()
                temp_win.title('Шаблоны')
                temp_win.columnconfigure([0], weight = 1, minsize = 150)
                temp_win.rowconfigure([0, 1, 2, 3], weight = 1, minsize = 0)
                temp_win.protocol('WM_DELETE_WINDOW', exit_menu_3)

                button7 = Button(temp_win, font = ('Verdana', 10, 'bold'), text = 'Перезагрузить ПК через 30 минут', width = 55, height = 3, command = Reboot2).grid(column = 0, row = 0, stick = 'wens')
                button8 = Button(temp_win, font = ('Verdana', 10, 'bold'), text = 'Перезагрузить ПК через 1 час', width = 55, height = 3, command = Reboot3).grid(column = 0, row = 1, stick = 'wens')
                button9 = Button(temp_win, font = ('Verdana', 10, 'bold'), text = 'Перезагрузить ПК через 1.5 часа', width = 55, height = 3, command = Reboot4).grid(column = 0, row = 2, stick = 'wens')
                button10 = Button(temp_win, font = ('Verdana', 10, 'bold'), text = 'Перезагрузить ПК через 2 часа', width = 55, height = 3, command = Reboot5).grid(column = 0, row = 3, stick = 'wens')

                temp_win.mainloop()

            window.withdraw()
            win = Tk()
            win.title('Перезагрузка ПК')
            win.columnconfigure([0], weight = 1, minsize = 150)
            win.rowconfigure([0, 1, 2, 3], weight = 1, minsize = 0)
            win.protocol('WM_DELETE_WINDOW', exit_menu_2)

            button6 = Button(win, font = ('Verdana', 10, 'bold'), text = 'Перезагрузить ПК', width = 35, height = 3, command = Reboot1).grid(column = 0, row = 0, stick = 'wens')
            button14 = Button(win, font = ('Verdana', 10, 'bold'), text = 'Шаблоны', width = 35, height = 3, command = templates2).grid(column = 0, row = 1, stick = 'wens')
            button11 = Button(win, font = ('Verdana', 10, 'bold'), text = 'Отмена неизбежной перезагрузки', width = 35, height = 3, command = stop, fg = 'red').grid(column = 0, row = 2, stick = 'wens')

            win.mainloop()

        #Режим сна ПК
        def Sleep():
            pass

        #Выход из учетной записи
        def Exit():
            pass

        def exit_menu():
            window.destroy()
            os.startfile(PATH + r'\Bot_main_menu.py')

        window = Tk()
        window.title('Питание ПК')
        window.columnconfigure([0], weight = 1, minsize = 150)
        window.rowconfigure([0, 1, 2, 3, 4], weight = 1, minsize = 0)
        window.protocol('WM_DELETE_WINDOW', exit_menu)

        button1 = Button(window, font = ('Verdana', 10, 'bold'), text = 'Выключить ПК', width = 25, height = 3, command = Power_off).grid(column = 0, row = 0, stick = 'wens')
        button2 = Button(window, font = ('Verdana', 10, 'bold'), text = 'Перезагрузить ПК', width = 25, height = 3, command = Reboot).grid(column = 0, row = 1, stick = 'wens')
        button3 = Button(window, font = ('Verdana', 10, 'bold'), text = 'Спящий режим ПК', width = 25, height = 3, command = Sleep).grid(column = 0, row = 2, stick = 'wens')
        button4 = Button(window, font = ('Verdana', 10, 'bold'), text = 'Выход из системы ПК', width = 25, height = 3, command = Exit).grid(column = 0, row = 3, stick = 'wens')
        button5 = Button(window, font = ('Verdana', 10, 'bold'), text = 'Задать время', width = 25, height = 3, command = Calc_sec).grid(column = 0, row = 4, stick = 'wens')

        window.mainloop()