# -- coding: utf-8 --

from tkinter import *
from tkinter import messagebox

import json
import requests

def clicked():
    name = txt.get().lower()  # origin
    url = f'https://api.github.com/users/{name}'
    data = requests.get(url).json()

    keys = ['company', 'created_at', 'email', 'id', 'name', 'url']
    info = {key: data[key] for key in keys}

    with open('data_file.json', 'w') as write_file:
        json.dump(info, write_file, indent=4)

    root.destroy()
    messagebox.showinfo('Главное меню', 'Информация загружена в файл')

root = Tk()
root.title('Главное меню')
root.geometry('300x70+200+200')

lbl = Label(root, text="Введите имя репозитория")
lbl.pack()

txt = Entry(root, width=30)
txt.focus()
txt.pack()

btn = Button(root, text='Получить информацию', command=clicked)
btn.pack()

root.mainloop()

