from tkinter import *
import os, threading, subprocess

def thread_cmds():
    threading.Thread(target = cmds).start()
def thread_autoloading():
    threading.Thread(target = autoloading).start()
def thread_regedit():
    threading.Thread(target = regedit).start()
def thread_services():
    threading.Thread(target = services).start()
def thread_appdata():
    threading.Thread(target = appdata).start()
def thread_device_manager():
    threading.Thread(target = device_manager).start()
def thread_finish_process():
    threading.Thread(target = finish_process).start()

def cmds():
    os.system('explorer C:\\Windows\\System32\\cmd.exe')

def autoloading():
    os.system('explorer C:\\Users\\%USERNAME%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')

def regedit():
    os.system('%windir%\\regedit.exe')

def services():
    os.system('%windir%\system32\services.msc')

def appdata():
    os.system('explorer C:\\Users\\' + os.environ['USERNAME'] + '\\AppData')

def device_manager():
    os.system('explorer C:\Windows\System32\devmgmt.msc')

def finish_process():

    def kill_finish_process():
        nonlocal entry_finish_process

        value = entry_finish_process.get()

        os.system('Taskkill /IM ' + value + ' /F /T')

    def enter_finish_process(Return):
        kill_finish_process()

    

    finish_process_win = Tk()
    finish_process_win.title('Завершить процесс')
    finish_process_win.geometry('184x70')
    finish_process_win.bind('<Return>', enter_finish_process)

    taskkill = subprocess.getoutput('TASKLIST /FI "USERNAME ne NT AUTHORITY\\SYSTEM" /FI "STATUS eq running"')

    finish_process_win.columnconfigure([0], weight = 1, minsize = 150)
    finish_process_win.rowconfigure([0, 1, 2], weight = 1, minsize = 0)

    label_finish_process = Label(finish_process_win, font = ('Verdana', 10, 'bold'), text = 'Напишите номер PID', fg = 'red')
    label_finish_process.grid(column = 0, row = 0, stick = 'wens')

    label_finish_process.configure(text = taskkill)

    entry_finish_process = Entry(finish_process_win, font = ('Verdana', 10, 'bold'))
    entry_finish_process.grid(column = 0, row = 1, stick = 'wens')

    button_finish_process = Button(finish_process_win, font = ('Verdana', 10, 'bold'), text = 'Завершить процесс', command = kill_finish_process).grid(column = 0, row = 2, stick = 'wens')

    finish_process_win.mainloop()

class menu_system:
    def menu():
        #Родительское окно
        window = Tk()
        window.title('Система')
        window.geometry('300x600')
        window.columnconfigure([0], weight = 1, minsize = 150)
        window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], weight = 1, minsize = 0)

        #Кнопки родительского окна
        button1 = Button(window, font = ('Verdana', 10, 'bold'), text = 'Командная строка', command = thread_cmds, width = 15, height = 3).grid(column = 0, row = 0, stick = 'wens')
        button2 = Button(window, font = ('Verdana', 10, 'bold'), text = 'Папка автозагрузки', command = thread_autoloading, width = 15, height = 3).grid(column = 0, row = 1, stick = 'wens')
        button3 = Button(window, font = ('Verdana', 10, 'bold'), text = 'Реестр', command = thread_regedit, width = 15, height = 3).grid(column = 0, row = 2, stick = 'wens')
        button4 = Button(window, font = ('Verdana', 10, 'bold'), text = 'Папка appdata', command = thread_appdata, width = 15, height = 3).grid(column = 0, row = 3, stick = 'wens')
        button5 = Button(window, font = ('Verdana', 10, 'bold'), text = 'Диспетчер устройств', command = thread_regedit, width = 15, height = 3).grid(column = 0, row = 4, stick = 'wens')
        button6 = Button(window, font = ('Verdana', 10, 'bold'), text = 'Завершить процесс приложения', command = thread_finish_process, width = 15, height = 3).grid(column = 0, row = 5, stick = 'wens')
        button7 = Button(window, font = ('Verdana', 10, 'bold'), text = 'Реестр', command = thread_regedit, width = 15, height = 3).grid(column = 0, row = 6, stick = 'wens')
        button8 = Button(window, font = ('Verdana', 10, 'bold'), text = 'Реестр', command = thread_regedit, width = 15, height = 3).grid(column = 0, row = 7, stick = 'wens')
        button9 = Button(window, font = ('Verdana', 10, 'bold'), text = 'Реестр', command = thread_regedit, width = 15, height = 3).grid(column = 0, row = 8, stick = 'wens')
        button10 = Button(window, font = ('Verdana', 10, 'bold'), text = 'Реестр', command = thread_regedit, width = 15, height = 3).grid(column = 0, row = 9, stick = 'wens')

        window.mainloop()

menu_system.menu()