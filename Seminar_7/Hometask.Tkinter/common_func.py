from tkinter import *
from tkinter import ttk
import json
from tkinter import messagebox
from init_main_window import MainWindow

def refresh():
    MainWindow.tree.delete(*MainWindow.tree.get_children())
    for contact in get_contacts():
        MainWindow.tree.insert('', END, values=(list(contact[i] for i in MainWindow.my_columns)))

def get_contacts():
    path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_7/Hometask.Tkinter/phonebook.json'
    with open(path, 'r') as ph_book_r:
        contacts = json.load(ph_book_r)
    return contacts