from cProfile import label
from timeit import repeat
from tkinter import *
from tkinter import messagebox
from turtle import left, update, width
import pandas as pd
import json
import pprint

from requests import delete

phonebook = Tk()
phonebook.title('Phonebook')


def popup_saved():
    messagebox.showinfo(title='Контакт добавлен!', message='Контакт добавлен!')

def popup_deleted():
    messagebox.showinfo(title='Удаление', message='Контакт  удален!')

def popup_null_saved():
    messagebox.showwarning(title='Ошибка', message='Не заполнено имя или фамилия пользователя')

def sure_deleted():
    response = messagebox.askyesno('Вы уверены, что хотите удалить контакт?')
    if response == True:
       popup_deleted


# Clicks

def add_btn_click():
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


def save_btn_click(window):
    new_contact = {
        'Имя': name_str.get(),
        'Фамилия': surname_str.get(),
        'Моб.': mob_str.get(),
        'Email': mail_str.get(),
        'Город': city_str.get(),
        'Год рождения': birthyear_str.get()
    }
    if (name_str.get() or surname_str.get()) == '':
        popup_null_saved()
        repeat()
    else:
        path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_7.py/Hometask.Phonebook/phonebook.json'
        with open(path, 'r') as ph_book_r:
            contacts = json.load(ph_book_r)
        
        with open(path, 'w') as ph_book:
            contacts.append(new_contact)
            json.dump(contacts, ph_book, indent=4)
        window.destroy()
        refresh()
        popup_saved()
    
    
def delete_btn_click():
    return 

def search_btn_click():
    search_window = Toplevel()
    search_window.title('Поиск контакта')
    global search_list
    global search_field_entry
    global search_frame_lbl
    search_list = StringVar()
    parameters = [
        "Фамилия",
        "Имя",
        "Город",
        "Год рождения"
    ]
    search_list.set(parameters[0])
    search_drop = OptionMenu(search_window, search_list, *parameters)
    search_lbl = Label(search_window, text='Параметр поиска')
    search_lbl.grid(row=0, column=0, sticky=W)
    search_drop.grid(row=0, column=1)
    search_field_lbl = Label(search_window, text='Поле поиска')
    search_field_entry = Entry(search_window, width=15, borderwidth=3)
    search_field_lbl.grid(row=1, column=0, sticky=W)
    search_field_entry.grid(row=1, column=1)
    search_frame = LabelFrame(search_window, width=350, height=200)
    search_frame.grid(row=2, column=0, columnspan=3, sticky=N)
    search_frame_lbl = Label(search_frame, text='Результаты поиска', justify=LEFT, width=35)
    search_frame_lbl.grid(row=0, column=0)
    user_search_btn = Button(search_window, text='Поиск', width=5, command=lambda: user_search_btn_click())
    user_search_btn.grid(row=1, column=2)

def user_search_btn_click():
    path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_7.py/Hometask.Phonebook/phonebook.json'
    search_object = search_field_entry.get()
    search_choice = search_list.get()
    contacts_df = pd.read_json(path)
    contacts = contacts_df.head()
    search_frame_lbl.config(text=contacts, width=NO)
    

def refresh():
    path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_7.py/Hometask.Phonebook/phonebook.json'
    contacts_df = pd.read_json(path)
    global contacts
    contacts = contacts_df.head()
    if len(contacts):
        text_frame_lbl.config(text=(contacts['Фамилия'] + ' ' + contacts['Имя']), justify=LEFT)
        if len(contacts) > 1:
            open_btn.config(state='disabled')
    else:
        text_frame_lbl.config(text='Контакты отсутствуют')



frame = LabelFrame(phonebook, padx=5, pady=5)
frame.grid(row=0, column=1, sticky=N)


text_frame = LabelFrame(phonebook, width=200, height=200)
text_frame.grid(row=0, column=0, sticky=N)
text_frame_lbl = Label(text_frame, text='', justify=LEFT, padx=10, pady=5)
text_frame_lbl.grid(row=0, column=0)
scroll = Scrollbar(text_frame)
scroll.grid(row=0, column=1, sticky=E)


# Buttons
search_btn = Button(frame, text='Поиск', command=search_btn_click, width=8)
search_btn.grid(row=0, column=0, sticky=E)
add_btn = Button(frame, text='Добавить', command=add_btn_click, width=8)
add_btn.grid(row=1, column=0, sticky=E)
delete_btn = Button(frame, text='Удалить', width=8)
delete_btn.grid(row=2, column=0, sticky=E)
open_btn = Button(frame, text='Открыть', width=8)
open_btn.grid(row=3, column=0, sticky=E)
change_btn = Button(frame, text='Изменить', width=8)
change_btn.grid(row=4, column=0, sticky=E)

refresh()
phonebook.mainloop() 