from tkinter import *
import controller as ct

def btn_click(number: int):
    current = ct.my_string.get()
    ct.my_string.delete(0, END)
    ct.my_string.insert(0, str(current) + str(number))

def btn_oper_clear():
    ct.my_string.delete(0, END)

def btn_oper_plus():
    first_number = ct.my_string.get()
    global f_num
    global math
    math = 'plus'
    f_num = int(first_number)
    ct.my_string.delete(0, END)

def btn_oper_minus():
    first_number = ct.my_string.get()
    global f_num
    global math
    math = 'minus'
    f_num = int(first_number)
    ct.my_string.delete(0, END)

def btn_oper_delenie():
    first_number = ct.my_string.get()
    global f_num
    global math
    math = 'delenie'
    f_num = int(first_number)
    ct.my_string.delete(0, END)

def btn_oper_umnojenie():
    first_number = ct.my_string.get()
    global f_num
    global math
    math = 'umnojenie'
    f_num = int(first_number)
    ct.my_string.delete(0, END)

def btn_oper_stepen():
    first_number = ct.my_string.get()
    global f_num
    global math
    math = 'stepen'
    f_num = int(first_number)
    ct.my_string.delete(0, END)

def btn_oper_ostatok():
    first_number = ct.my_string.get()
    global f_num
    global math
    math = 'ostatok'
    f_num = int(first_number)
    ct.my_string.delete(0, END)

def button_oper_ravno():
    second_num = ct.my_string.get()
    ct.my_string.delete(0, END)
    
    if math == 'plus':
        ct.my_string.insert(0, f_num + int(second_num))

    if math == 'minus':
        ct.my_string.insert(0, f_num - int(second_num))

    if math == 'umnojenie':
        ct.my_string.insert(0, f_num * int(second_num))

    if math == 'delenie':
        ct.my_string.insert(0, f_num / int(second_num))
