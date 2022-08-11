from timeit import repeat
from tkinter import *
from tkinter import messagebox
import json
from tkinter import ttk

phonebook = Tk()
phonebook.title('Phonebook')
path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_7/Hometask.Tkinter/phonebook.json'

class SearchWindow:
    def __init__(self):
        search_window = Toplevel()
        search_window.title('Поиск контакта')
        parameters = [
            "Фамилия",
            "Имя",
            "Город",
            "Год рождения"
        ]
        self.search_list = StringVar()
        search_drop = OptionMenu(search_window, self.search_list, *parameters)
        search_drop.grid(row=0, column=1)
        search_lbl = Label(search_window, text='Параметр поиска')
        search_lbl.grid(row=0, column=0, sticky=W)
        search_field_lbl = Label(search_window, text='Поле поиска')
        search_field_lbl.grid(row=1, column=0, sticky=W)
        user_search_btn = Button(search_window, text='Поиск', width=5, command=self.user_search_btn_click)
        user_search_btn.grid(row=1, column=2)
        search_frame = LabelFrame(search_window, width=350, height=200)
        search_frame.grid(row=2, column=0, columnspan=3, sticky=N)
        
        # self options
        self.search_list.set(parameters[0])
        self.search_field_entry = Entry(search_window, width=15, borderwidth=3)
        self.search_field_entry.grid(row=1, column=1)
        self.search_frame_lbl = Label(search_frame, text='Результаты поиска', justify=LEFT, width=35)
        self.search_frame_lbl.grid(row=0, column=0)


    def user_search_btn_click(self):
        contacts = get_contacts()
        for i in range(len(contacts)):
            if contacts[i][self.search_list.get()].lower() == self.search_field_entry.get().lower():
                self.search_frame_lbl.config(text=contacts[i], width=NO)

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
            contacts = get_contacts()
            with open(path, 'w') as ph_book:
                contacts.append(new_contact)
                json.dump(contacts, ph_book, indent=4, ensure_ascii=False)
            window.destroy()
            refresh()
            self.popup_saved()

    def popup_null_saved(self):
        messagebox.showwarning(title='Ошибка', message='Не заполнено имя или фамилия пользователя')

    def popup_saved(self):
        messagebox.showinfo(title='Контакт добавлен!', message='Контакт добавлен!')
       
class DeleteWindow: # Больше не испоьзуется
    def __init__(self):
        self.del_window = Toplevel()
        self.del_window.title('Удаление контакта')
        self.del_lbl = Label(self.del_window, text='Введите номер контакта для удаления', justify=LEFT, padx=2)
        self.del_lbl.grid(row=0, column=0)
        self.del_entry = Entry(self.del_window, width=10)
        self.del_entry.grid(row=0, column=1)
        self.del_btn = Button(self.del_window, text='Удалить контакт', command=lambda: self.del_contact(self.del_window))
        self.del_btn.grid(row=1, column=0, columnspan=2)
        self.contacts = get_contacts()
        
    def del_contact(self, window):
        global contact_num
        contact_num = int(self.del_entry.get())
        path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_7/Hometask.Tkinter/phonebook.json'
        if contact_num in range(len(self.contacts)):
            self.sure_deleted()
            if self.response == True:
                with open(path, 'w') as ph_book:
                    del self.contacts[contact_num]
                    json.dump(self.contacts, ph_book, indent=4, ensure_ascii=False)
                window.destroy()
                refresh()
                self.popup_deleted()
        else:
            self.popup_nocontact()

    def popup_deleted(self):
        messagebox.showinfo(title='Удаление', message='Контакт удален!')

    def sure_deleted(self):
        self.response = messagebox.askyesno(message=f"Вы уверены, что хотите удалить контакт? {self.contacts[contact_num]['Фамилия']} {self.contacts[contact_num]['Имя']}")

    def popup_nocontact(self):
        messagebox.showwarning(title='Ошибка', message='Такого контакта нет в справочнике')

class ChangeWindow:
    def __init__(self):
        my_item = tree.item(tree.focus())['values']
        self.change_window = Toplevel()
        self.change_window.title("Изменение контакта")
        self.contacts = list(get_contacts())
        for i in self.contacts:
            if str(i["Имя"]) == str(my_item[0]) and str(i["Фамилия"]) == str(my_item[1]) and str(i["Моб."]) == str(my_item[2]):
                self.my_index = self.contacts.index(i)
                break
            else:
                self.my_index = 0
        self.name_lbl = Label(self.change_window, text='Имя:')
        self.name_lbl.grid(row=0, column=0, sticky=W)
        self.name_str = Entry(self.change_window, width=20, borderwidth=3)
        self.name_str.grid(row=0, column=1, sticky=W)
        self.name_str.insert(0, my_item[0])
        self.surname_lbl = Label(self.change_window, text='Фамилия:')
        self.surname_lbl.grid(row=1, column=0, sticky=W)
        self.surname_str = Entry(self.change_window, width=20, borderwidth=3)
        self.surname_str.grid(row=1, column=1)
        self.surname_str.insert(0, my_item[1])
        self.mob_lbl = Label(self.change_window, text='Мобильный:')
        self.mob_lbl.grid(row=2, column=0, sticky=W)
        self.mob_str = Entry(self.change_window, width=20, borderwidth=3)
        self.mob_str.grid(row=2, column=1)
        self.mob_str.insert(0, my_item[2])
        self.mail_lbl = Label(self.change_window, text='Email:')
        self.mail_lbl.grid(row=3, column=0, sticky=W)
        self.mail_str = Entry(self.change_window, width=20, borderwidth=3)
        self.mail_str.grid(row=3, column=1)
        self.mail_str.insert(0, my_item[3])
        self.city_lbl = Label(self.change_window, text='Город:')
        self.city_lbl.grid(row=4, column=0, sticky=W)
        self.city_str = Entry(self.change_window, width=20, borderwidth=3)
        self.city_str.grid(row=4, column=1)
        self.city_str.insert(0, my_item[4])
        self.birthyear_lbl = Label(self.change_window, text='Год рождения:')
        self.birthyear_lbl.grid(row=5, column=0, sticky=W)
        self.birthyear_str = Entry(self.change_window, width=20, borderwidth=3)
        self.birthyear_str.grid(row=5, column=1)
        self.birthyear_str.insert(0, my_item[5])

        # Save Button
        self.save_btn = Button(self.change_window, text='Сохранить', command=lambda: self.save_change_click(self.change_window))
        self.save_btn.grid(row=6, column=1, sticky=E)

    def save_change_click(self, window):
        changed_contact = {
            'Имя': self.name_str.get(),
            'Фамилия': self.surname_str.get(),
            'Моб.': self.mob_str.get(),
            'Email': self.mail_str.get(),
            'Город': self.city_str.get(),
            'Год рождения': self.birthyear_str.get()
        }
        self.contacts[self.my_index] = changed_contact
        with open(path, 'w') as ph_book:
            json.dump(self.contacts, ph_book, indent=4, ensure_ascii=False)
        window.destroy()
        refresh()
        self.popup_changed_saved()

    def popup_null_saved(self):
        messagebox.showwarning(title='Ошибка', message='Не заполнено имя или фамилия пользователя')

    def popup_changed_saved(self):
        messagebox.showinfo(title='Изменения сохранены!', message='Изменения сохранены!')
    pass


def delete_contact():
    my_item = tree.item(tree.focus())['values']
    contacts = list(get_contacts())
    for i in contacts:
        if str(i["Имя"]) == str(my_item[0]) and str(i["Фамилия"]) == str(my_item[1]) and str(i["Моб."]) == str(my_item[2]):
            my_ind = contacts.index(i)
            break
    response = messagebox.askyesno(message=f"Вы уверены, что хотите удалить контакт? {contacts[my_ind]['Фамилия']} {contacts[my_ind]['Имя']}")
    if response == True:
        with open(path, 'w') as ph_book:
            del contacts[my_ind]
            json.dump(contacts, ph_book, indent=4, ensure_ascii=False)
        refresh()
        messagebox.showinfo(title='Удаление', message='Контакт удален!')

def refresh():
    tree.delete(*tree.get_children())
    for contact in get_contacts():
        tree.insert('', END, values=(list(contact[i] for i in my_columns)))

def get_contacts():
    with open(path, 'r') as ph_book_r:
        contacts = json.load(ph_book_r)
    return contacts

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
    contacts = get_contacts()
    for i in range(len(get_contacts())):
        if value.lower() in contacts[i][search_item.get()].lower():
            tree.insert('', END, values=(contacts[i]["Имя"], contacts[i]["Фамилия"], contacts[i]["Моб."], contacts[i]["Email"], contacts[i]["Город"], contacts[i]["Год рождения"]))

def clear_btn_click():
    search_entry.delete("0", END)
    search_entry.insert(0, 'Поиск. Escape для отмены поиска')
    refresh()


# Search Field
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
search_entry.bind('<Key>', get_value)
search_entry.bind('<Button-1>', clear_value)

# Frame for Buttons
frame = LabelFrame(phonebook, padx=5, pady=5)
frame.grid(row=1, column=3, sticky=N)

# Buttons
clear_btn = Button(frame, text='Сброс', command=clear_btn_click, width=8)
clear_btn.grid(row=0, column=0, sticky=E)
search_btn = Button(frame, text='Поиск', command=SearchWindow, width=8)
search_btn.grid(row=1, column=0, sticky=E)
add_btn = Button(frame, text='Добавить', command=AddWindow, width=8)
add_btn.grid(row=2, column=0, sticky=E)
delete_btn = Button(frame, text='Удалить', command=delete_contact, width=8)
delete_btn.grid(row=3, column=0, sticky=E)
open_btn = Button(frame, text='Открыть', width=8)
open_btn.grid(row=4, column=0, sticky=E)
change_btn = Button(frame, text='Изменить', command=ChangeWindow, width=8)
change_btn.grid(row=5, column=0, sticky=E)

# Table
my_columns = ('Имя', 'Фамилия', 'Моб.', 'Email', 'Город', 'Год рождения')
tree = ttk.Treeview(phonebook, columns=my_columns, show='headings')
for i in my_columns:
    tree.heading(i, text=i, anchor='center')
    tree.column(i, width=100, anchor='center')
tree.grid(row=1, column=0, columnspan=2, sticky='nsew')

# Scrollbar for Table
scrollbar = ttk.Scrollbar(phonebook, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=2, sticky='ns')

refresh()
phonebook.mainloop() 