from tkinter import *

root = Tk()
root.title('Калькулятор')
root.iconbitmap('/Users/nikolaishpagin/Desktop/GeekBrains/Programmer_1st_quarter/Python/Seminar_7.py/Calculator/calc.ico')
my_string = Entry(root, width=35, borderwidth=5)
my_string.grid(row=0, column=0, columnspan = 5, padx=10, pady=20)

# Functions
def btn_click(number: str):
    current = my_string.get()
    my_string.delete(0, END)
    my_string.insert(0, current + str(number))

def btn_oper_clear():
    my_string.delete(0, END)

def btn_oper_plus():
    first_number = my_string.get()
    global f_num
    global math
    math = 'plus'
    if '.'in first_number:
        f_num = float(first_number)
    else:
        f_num = int(first_number)
    my_string.delete(0, END)

def btn_oper_minus():
    first_number = my_string.get()
    global f_num
    global math
    math = 'minus'
    if '.'in first_number:
        f_num = float(first_number)
    else:
        f_num = int(first_number)
    my_string.delete(0, END)

def btn_oper_delenie():
    first_number = my_string.get()
    global f_num
    global math
    math = 'delenie'
    if '.'in first_number:
        f_num = float(first_number)
    else:
        f_num = int(first_number)
    my_string.delete(0, END)

def btn_oper_umnojenie():
    first_number = my_string.get()
    global f_num
    global math
    math = 'umnojenie'
    if '.'in first_number:
        f_num = float(first_number)
    else:
        f_num = int(first_number)
    my_string.delete(0, END)

def btn_oper_stepen():
    first_number = my_string.get()
    global f_num
    global math
    math = 'stepen'
    if '.'in first_number:
        f_num = float(first_number)
    else:
        f_num = int(first_number)
    my_string.delete(0, END)

def btn_oper_ostatok():
    first_number = my_string.get()
    global f_num
    global math
    math = 'ostatok'
    if '.'in first_number:
        f_num = float(first_number)
    else:
        f_num = int(first_number)
    my_string.delete(0, END)

def btn_oper_ravno():
    second_num = my_string.get()
    my_string.delete(0, END)
    if '.'in second_num:
        second_num = float(second_num)
    else:
        second_num = int(second_num)
    
    if math == 'plus':
        my_string.insert(0, f_num + second_num)

    if math == 'minus':
        my_string.insert(0, f_num - second_num)

    if math == 'umnojenie':
        my_string.insert(0, f_num * second_num)

    if math == 'delenie':
        my_string.insert(0, f_num / second_num)
            
    if math == 'stepen':
        my_string.insert(0, f_num**second_num)

    if math == 'ostatok':
        my_string.insert(0, f_num % second_num)

# Numbers
btn_1 = Button(root, text='1', width=5, pady=20, command=lambda: btn_click('1'))
btn_2 = Button(root, text='2', width=5, pady=20, command=lambda: btn_click('2'))
btn_3 = Button(root, text='3', width=5, pady=20, command=lambda: btn_click('3'))
btn_4 = Button(root, text='4', width=5, pady=20, command=lambda: btn_click('4'))
btn_5 = Button(root, text='5', width=5, pady=20, command=lambda: btn_click('5'))
btn_6 = Button(root, text='6', width=5, pady=20, command=lambda: btn_click('6'))
btn_7 = Button(root, text='7', width=5, pady=20, command=lambda: btn_click('7'))
btn_8 = Button(root, text='8', width=5, pady=20, command=lambda: btn_click('8'))
btn_9 = Button(root, text='9', width=5, pady=20, command=lambda: btn_click('9'))
btn_0 = Button(root, text='0', width=15, pady=20, command=lambda: btn_click('0'))
btn_comma = Button(root, text=',', width=5, pady=20, command=lambda: btn_click('.'))

# Operations
btn_plus = Button(root, text='+', width=5, pady=20, background='blue', command=btn_oper_plus)
btn_minus = Button(root, text='-', width=5, pady=20, command=btn_oper_minus)
btn_delenie = Button(root, text='/', width=5, pady=20, command=btn_oper_delenie)
btn_umnojenie = Button(root, text='*', width=5, pady=20, command=btn_oper_umnojenie)
btn_ravno = Button(root, text='=', width=5, pady=20, command=btn_oper_ravno)
btn_stepen = Button(root, text='^', width=5, pady=20, command=btn_oper_stepen)
btn_ostatok = Button(root, text='%', width=5, pady=20, command=btn_oper_ostatok)
btn_clear = Button(root, text='C', width=5, pady=20, command=btn_oper_clear)

# Buttons place
btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)
btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)
btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_0.grid(row=5, column=0, columnspan=2)

btn_clear.grid(row=1, column=0)
btn_stepen.grid(row=1, column=1)
btn_ostatok.grid(row=1, column=2)
btn_delenie.grid(row=1, column=3)
btn_umnojenie.grid(row=2, column=3)
btn_minus.grid(row=3, column=3)
btn_plus.grid(row=4, column=3)
btn_comma.grid(row=5, column=2)
btn_ravno.grid(row=5, column=3)


root.mainloop()