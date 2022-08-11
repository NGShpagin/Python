from tkinter import *
from tkinter import ttk
import json
from tkinter import messagebox
from init_main_window import MainWindow
import common_func

class SearchField:
    def __init__(self):
        self.search_entry = Entry(MainWindow.phonebook)
        self.search_item = StringVar()
        self.items_list = [
            "Фамилия",
            "Имя",
            "Город",
            "Год рождения"
            ]
        self.search_items_drop = OptionMenu(MainWindow.phonebook, self.search_item, *self.items_list)
        self.search_item.set(self.items_list[0])
        self.search_entry.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        self.search_entry.insert(0, 'Поиск. Escape для отмены поиска')   
        self.search_entry.bind('<Key>', self.get_value)
        self.search_entry.bind('<Button-1>', self.clear_value)
        self.search_items_drop.grid(row=0, column=2, columnspan=2, sticky=NSEW)
        
    def get_value(self, event):
        if event.keycode == 27:
                self.search_entry.delete("0", END)
                self.search_entry.insert(0, 'Поиск. Escape для отмены поиска')
                common_func.refresh()
        else:
            my_value = self.search_entry.get()
            self.search_value(my_value+event.char)

    def clear_value(self, event):
        self.search_entry.delete("0", END)

    def search_value(self, value):
        MainWindow.tree.delete(*MainWindow.tree.get_children())
        contacts = common_func.get_contacts()
        for i in range(len(contacts)):
            if value.lower() in contacts[i][self.search_item.get()].lower():
                MainWindow.tree.insert('', END, values=(contacts[i]["Имя"], contacts[i]["Фамилия"], contacts[i]["Моб."], contacts[i]["Email"], contacts[i]["Город"], contacts[i]["Год рождения"]))

    def clear_btn_click(self):
        self.clear_value()
        self.search_entry.insert(0, 'Поиск. Escape для отмены поиска')
        common_func.refresh()