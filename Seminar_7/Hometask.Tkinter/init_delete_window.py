from tkinter import *
from tkinter import ttk
import json
from tkinter import messagebox
import common_func


class DeleteWindow:
    def __init__(self):
        self.del_window = Toplevel()
        self.del_window.title('Удаление контакта')
        self.del_lbl = Label(self.del_window, text='Введите номер контакта для удаления', justify=LEFT, padx=2)
        self.del_lbl.grid(row=0, column=0)
        self.del_entry = Entry(self.del_window, width=10)
        self.del_entry.grid(row=0, column=1)
        self.del_btn = Button(self.del_window, text='Удалить контакт', command=lambda: self.del_contact(self.del_window))
        self.del_btn.grid(row=1, column=0, columnspan=2)
        self.contacts = common_func.get_contacts()
        
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
                common_func.refresh()
                self.popup_deleted()
        else:
            self.popup_nocontact()

    def popup_deleted(self):
        messagebox.showinfo(title='Удаление', message='Контакт удален!')

    def sure_deleted(self):
        self.response = messagebox.askyesno(message=f"Вы уверены, что хотите удалить контакт? {self.contacts[contact_num]['Фамилия']} {self.contacts[contact_num]['Имя']}")
        if self.response == True:
            self.popup_deleted()

    def popup_nocontact(self):
        messagebox.showwarning(title='Ошибка', message='Такого контакта нет в справочнике')

