from tkinter import *
import json


class Add_btn_click:
    def __init__(self) -> None:
        pass

    def save_btn_click(self, window):
        new_contact = {
            'Имя': name_str.get(),
            'Фамилия': surname_str.get(),
            'Моб.': mob_str.get(),
            'Email': mail_str.get(),
            'Город': city_str.get(),
            'Год рождения': birthyear_str.get()
        }
        path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_7.py/Hometask.Phonebook/phonebook.json'
        with open(path, 'r') as ph_book_r:
            contacts = json.load(ph_book_r)
        
        with open(path, 'w') as ph_book:
            contacts.append(new_contact)
            json.dump(contacts, ph_book, indent=2)
        window.destroy()
        refresh()
        popup_saved()
    
    add_window = Toplevel()
    add_window.title('Добавление нового контакта')
    global name_str
    global surname_str
    global mob_str
    global mail_str
    global city_str
    global birthyear_str

    name_lbl = Label(add_window, text='Имя:')
    name_str = Entry(add_window, width=20, borderwidth=3)
    surname_lbl = Label(add_window, text='Фамилия:')
    surname_str = Entry(add_window, width=20, borderwidth=3)
    mob_lbl = Label(add_window, text='Мобильный:')
    mob_str = Entry(add_window, width=20, borderwidth=3)
    mail_lbl = Label(add_window, text='Email:')
    mail_str = Entry(add_window, width=20, borderwidth=3)
    city_lbl = Label(add_window, text='Город:')
    city_str = Entry(add_window, width=20, borderwidth=3)
    birthyear_lbl = Label(add_window, text='Год рождения:')
    birthyear_str = Entry(add_window, width=20, borderwidth=3)

    name_lbl.grid(row=0, column=0, sticky=W)
    name_str.grid(row=0, column=1)
    surname_lbl.grid(row=1, column=0, sticky=W)
    surname_str.grid(row=1, column=1)
    mob_lbl.grid(row=2, column=0, sticky=W)
    mob_str.grid(row=2, column=1)
    mail_lbl.grid(row=3, column=0, sticky=W)
    mail_str.grid(row=3, column=1)
    city_lbl.grid(row=4, column=0, sticky=W)
    city_str.grid(row=4, column=1)
    birthyear_lbl.grid(row=5, column=0, sticky=W)
    birthyear_str.grid(row=5, column=1)

    save_btn = Button(add_window, text='Добавить', command=lambda: save_btn_click(add_window))
    save_btn.grid(row=6, column=1, sticky=E)


