# from tkinter import *
# import pandas as pd

# def refresh():
#     path = '/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_7.py/Hometask.Phonebook/phonebook.json'
#     contacts_df = pd.read_json(path)
#     global contacts
#     contacts = contacts_df.head()
#     if len(contacts):
#         text_frame_lbl.config(text=(contacts['Фамилия'] + ' ' + contacts['Имя']), justify=LEFT)
#         if len(contacts) > 1:
#             open_btn.config(state='disabled')
#     else:
#         text_frame_lbl.config(text='Контакты отсутствуют')