from tkinter import *
from tkinter import ttk
import json
from tkinter import messagebox
import common_func
from init_add_window import AddWindow
from init_delete_window import DeleteWindow
from init_search_window import SearchWindow
from init_search_field import SearchField

class MainWindow: 
    def __init__(self):
        self.phonebook = Tk()
        self.phonebook.title('Phonebook')
        
        # Frame for Buttons
        self.frame = LabelFrame(self.phonebook, padx=5, pady=5)
        self.frame.grid(row=1, column=3, sticky=N)

        # Buttons
        clear_btn = Button(self.frame, text='Сброс', command=SearchField, width=8)
        clear_btn.grid(row=0, column=0, sticky=E)
        search_btn = Button(self.frame, text='Поиск', command=SearchWindow, width=8)
        search_btn.grid(row=1, column=0, sticky=E)
        add_btn = Button(self.frame, text='Добавить', command=AddWindow, width=8)
        add_btn.grid(row=2, column=0, sticky=E)
        delete_btn = Button(self.frame, text='Удалить', command=DeleteWindow, width=8)
        delete_btn.grid(row=3, column=0, sticky=E)
        open_btn = Button(self.frame, text='Открыть', width=8)
        open_btn.grid(row=4, column=0, sticky=E)
        change_btn = Button(self.frame, text='Изменить', width=8)
        change_btn.grid(row=5, column=0, sticky=E)

        # Main table
        self.my_columns = ('Имя', 'Фамилия', 'Моб.', 'Email', 'Город', 'Год рождения')
        self.tree = ttk.Treeview(self.phonebook, columns=self.my_columns, show='headings')


    def init_main_able(self):
        for i in self.my_columns:
            self.tree.heading(i, text=i, anchor='center')
            self.tree.column(i, width=100, anchor='center')
        self.tree.grid(row=1, column=0, columnspan=2, sticky='nsew')