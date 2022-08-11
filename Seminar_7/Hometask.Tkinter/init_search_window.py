from tkinter import *
from tkinter import ttk
import json
from tkinter import messagebox
import common_func

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
        self.search_list = StringVar()
        self.search_list.set(parameters[0])
        self.search_field_entry = Entry(search_window, width=15, borderwidth=3)
        self.search_field_entry.grid(row=1, column=1)
        self.search_frame_lbl = Label(search_frame, text='Результаты поиска', justify=LEFT, width=35)
        self.search_frame_lbl.grid(row=0, column=0)


    def user_search_btn_click(self):
        contacts = common_func.get_contacts()
        for i in range(len(contacts)):
            if contacts[i][self.search_list.get()] == self.search_field_entry.get():
                self.search_frame_lbl.config(text=contacts[i], width=NO)
