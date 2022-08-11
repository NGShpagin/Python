from tkinter import *
from tkinter import ttk
import json
from tkinter import messagebox
import common_func


class AddWindow:
    def __init__(self):
        self.add_window = Toplevel()
        self.add_window.title('Добавление нового контакта')
        
        # New Contact fields
        self.name_lbl = Label(self.add_window, text='Имя:')
        self.name_lbl.grid(row=0, column=0, sticky=W)
        self.name_str = Entry(self.add_window, width=20, borderwidth=3)
        self.name_str.grid(row=0, column=1)
        self.surname_lbl = Label(self.add_window, text='Фамилия:')
        self.surname_lbl.grid(row=1, column=0, sticky=W)
        self.surname_str = Entry(self.add_window, width=20, borderwidth=3)
        self.surname_str.grid(row=1, column=1)
        self.mob_lbl = Label(self.add_window, text='Мобильный:')
        self.mob_lbl.grid(row=2, column=0, sticky=W)
        self.mob_str = Entry(self.add_window, width=20, borderwidth=3)
        self.mob_str.grid(row=2, column=1)
        self.mail_lbl = Label(self.add_window, text='Email:')
        self.mail_lbl.grid(row=3, column=0, sticky=W)
        self.mail_str = Entry(self.add_window, width=20, borderwidth=3)
        self.mail_str.grid(row=3, column=1)
        self.city_lbl = Label(self.add_window, text='Город:')
        self.city_lbl.grid(row=4, column=0, sticky=W)
        self.city_str = Entry(self.add_window, width=20, borderwidth=3)
        self.city_str.grid(row=4, column=1)
        self.birthyear_lbl = Label(self.add_window, text='Год рождения:')
        self.birthyear_lbl.grid(row=5, column=0, sticky=W)
        self.birthyear_str = Entry(self.add_window, width=20, borderwidth=3)
        self.birthyear_str.grid(row=5, column=1)

        # Add Button
        self.save_btn = Button(self.add_window, text='Добавить', command=lambda: self.save_btn_click(self.add_window))
        self.save_btn.grid(row=6, column=1, sticky=E)

    def save_btn_click(self, window):
        new_contact = {
            'Имя': self.name_str.get(),
            'Фамилия': self.surname_str.get(),
            'Моб.': self.mob_str.get(),
            'Email': self.mail_str.get(),
            'Город': self.city_str.get(),
            'Год рождения': self.birthyear_str.get()
        }
        if (self.name_str.get() or self.surname_str.get()) == '':
            self.popup_null_saved()
            self.repeat()
        else:
            path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_7/Hometask.Tkinter/phonebook.json'
            with open(path, 'r') as ph_book_r:
                contacts = json.load(ph_book_r)
            
            with open(path, 'w') as ph_book:
                contacts.append(new_contact)
                json.dump(contacts, ph_book, indent=4, ensure_ascii=False)
            window.destroy()
            common_func.refresh()
            self.popup_saved()

    def popup_null_saved(self):
        messagebox.showwarning(title='Ошибка', message='Не заполнено имя или фамилия пользователя')

    def popup_saved(self):
        messagebox.showinfo(title='Контакт добавлен!', message='Контакт добавлен!')
            