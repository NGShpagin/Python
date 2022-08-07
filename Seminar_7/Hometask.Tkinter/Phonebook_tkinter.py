from timeit import repeat
from tkinter import *
from tkinter import messagebox
import json
from tkinter import ttk

phonebook = Tk()
phonebook.title('Phonebook')


def popup_saved():
    messagebox.showinfo(title='Контакт добавлен!', message='Контакт добавлен!')

def popup_deleted():
    messagebox.showinfo(title='Удаление', message='Контакт  удален!')

def popup_null_saved():
    messagebox.showwarning(title='Ошибка', message='Не заполнено имя или фамилия пользователя')

def popup_nocontact():
    messagebox.showwarning(title='Ошибка', message='Такого контакта нет в справочнике')

def sure_deleted():
    global response
    response = messagebox.askyesno(message='Вы уверены, что хотите удалить контакт?')
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
        path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_7/Hometask.Tkinter/phonebook.json'
        with open(path, 'r') as ph_book_r:
            contacts = json.load(ph_book_r)
        
        with open(path, 'w') as ph_book:
            contacts.append(new_contact)
            json.dump(contacts, ph_book, indent=4, ensure_ascii=False)
        window.destroy()
        refresh()
        popup_saved()
    
    
def delete_btn_click():
    del_window = Toplevel()
    del_window.title('Удаление контакта')
    global del_entry
    del_lbl = Label(del_window, text='Введите номер контакта для удаления', justify=LEFT, padx=2)
    del_lbl.grid(row=0, column=0)
    del_entry = Entry(del_window, width=10)
    del_entry.grid(row=0, column=1)
    del_btn = Button(del_window, text='Удалить контакт', command=lambda: del_contact(del_window))
    del_btn.grid(row=1, column=0, columnspan=2)

def del_contact(window):
    contact_num = int(del_entry.get())
    path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_7/Hometask.Tkinter/phonebook.json'
    with open(path, 'r') as ph_book_r:
        contacts = json.load(ph_book_r)
    if contact_num in range(len(contacts)):
        sure_deleted()
        if response == True:
            with open(path, 'w') as ph_book:
                del contacts[contact_num]
                json.dump(contacts, ph_book, indent=4, ensure_ascii=False)
            window.destroy()
            refresh()
            popup_deleted()
    else:
        popup_nocontact()

    
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
    user_search_btn = Button(search_window, text='Поиск', width=5, command=user_search_btn_click)
    user_search_btn.grid(row=1, column=2)

def user_search_btn_click():
    path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_7.py/Hometask.Phonebook/phonebook.json'
    search_object = search_field_entry.get()
    search_choice = search_list.get()
    path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_7/Hometask.Tkinter/phonebook.json'
    with open(path, 'r') as ph_book_r:
        contacts = json.load(ph_book_r)
    for i in range(len(contacts)):
        if contacts[i][search_choice] == search_object:
            contacts_df = contacts[i]
            search_frame_lbl.config(text=contacts[i], width=NO)
    

def refresh():
    path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_7/Hometask.Tkinter/phonebook.json'
    tree.delete(*tree.get_children())
    with open(path, 'r') as ph_book_r:
        contacts = json.load(ph_book_r)

    # add data to the treeview
    for contact in contacts:
        tree.insert('', END, values=(contact["Имя"], contact["Фамилия"], contact["Моб."], contact["Email"], contact["Город"], contact["Год рождения"]))


frame = LabelFrame(phonebook, padx=5, pady=5)
frame.grid(row=1, column=3, sticky=N)


search_entry = Entry(phonebook)
search_entry.grid(row=0, column=0, columnspan=2, sticky=NSEW)
search_entry.insert(0, 'Поиск. Escape для отмены поиска')

search_item = StringVar()
items_list = [
    "Фамилия",
    "Имя",
    "Город",
    "Год рождения"
    ]
search_item.set(items_list[0])
search__items_drop = OptionMenu(phonebook, search_item, *items_list)
search__items_drop.grid(row=0, column=2, columnspan=2, sticky=NSEW)



def get_value(event):
    if event.keycode == 27:
            search_entry.delete("0", END)
            search_entry.insert(0, 'Поиск. Escape для отмены поиска')
            refresh()
    else:
        my_value = search_entry.get()
        search_value(my_value+event.char)

def clear_value(event):
    search_entry.delete("0", END)

def search_value(value):
    tree.delete(*tree.get_children())
    path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_7/Hometask.Tkinter/phonebook.json'
    with open(path, 'r') as ph_book_r:
        contacts = json.load(ph_book_r)
    for i in range(len(contacts)):
        if value in contacts[i][search_item.get()]:
            tree.insert('', END, values=(contacts[i]["Имя"], contacts[i]["Фамилия"], contacts[i]["Моб."], contacts[i]["Email"], contacts[i]["Город"], contacts[i]["Год рождения"]))

def clear_btn_click():
    search_entry.delete("0", END)
    search_entry.insert(0, 'Поиск. Escape для отмены поиска')
    refresh()


search_entry.bind('<Key>', get_value)
search_entry.bind('<Button-1>', clear_value)

# Buttons
clear_btn = Button(frame, text='Сброс', command=clear_btn_click, width=8)
clear_btn.grid(row=0, column=0, sticky=E)
search_btn = Button(frame, text='Поиск', command=search_btn_click, width=8)
search_btn.grid(row=1, column=0, sticky=E)
add_btn = Button(frame, text='Добавить', command=add_btn_click, width=8)
add_btn.grid(row=2, column=0, sticky=E)
delete_btn = Button(frame, text='Удалить', command=delete_btn_click, width=8)
delete_btn.grid(row=3, column=0, sticky=E)
open_btn = Button(frame, text='Открыть', width=8)
open_btn.grid(row=4, column=0, sticky=E)
change_btn = Button(frame, text='Изменить', width=8)
change_btn.grid(row=5, column=0, sticky=E)

# Table

my_columns = ('Имя', 'Фамилия', 'Моб.', 'Email', 'Город', 'Год рождения')
tree = ttk.Treeview(phonebook, columns=my_columns, show='headings')
tree.heading('Имя', text='Имя', anchor='center')
tree.heading('Фамилия', text='Фамилия', anchor='center')
tree.heading('Моб.', text='Моб.', anchor='center')
tree.heading('Email', text='Email', anchor='center')
tree.heading('Город', text='Город', anchor='center')
tree.heading('Год рождения', text='Год рождения')
tree.column('Имя', width=100, anchor='center')
tree.column('Фамилия', width=120, anchor='center')
tree.column('Моб.', width=120, anchor='center')
tree.column('Email', width=120, anchor='center')
tree.column('Город', width=100, anchor='center')
tree.column('Год рождения', width=100, anchor='center')


def get_contacts():
    global contacts
    path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_7/Hometask.Tkinter/phonebook.json'
    with open(path, 'r') as ph_book_r:
        contacts = json.load(ph_book_r)

get_contacts()

# add data to the treeview
for contact in contacts:
    tree.insert('', END, values=(contact["Имя"], contact["Фамилия"], contact["Моб."], contact["Email"], contact["Город"], contact["Год рождения"]))

tree.grid(row=1, column=0, columnspan=2, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(phonebook, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=2, sticky='ns')


refresh()
phonebook.mainloop() 