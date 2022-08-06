from tkinter import *
from controller import root
import clicks as cl

# Numbers
btn_1 = Button(root, text='1', padx=20, pady=20, command=lambda: cl.btn_click(1))
btn_2 = Button(root, text='2', padx=20, pady=20, command=lambda: cl.btn_click(2))
btn_3 = Button(root, text='3', padx=20, pady=20, command=lambda: cl.btn_click(3))
btn_4 = Button(root, text='4', padx=20, pady=20, command=lambda: cl.btn_click(4))
btn_5 = Button(root, text='5', padx=20, pady=20, command=lambda: cl.btn_click(5))
btn_6 = Button(root, text='6', padx=20, pady=20, command=lambda: cl.btn_click(6))
btn_7 = Button(root, text='7', padx=20, pady=20, command=lambda: cl.btn_click(7))
btn_8 = Button(root, text='8', padx=20, pady=20, command=lambda: cl.btn_click(8))
btn_9 = Button(root, text='9', padx=20, pady=20, command=lambda: cl.btn_click(9))
btn_0 = Button(root, text='0', padx=20, pady=20, command=lambda: cl.btn_click(0))

# Operations
btn_plus = Button(root, text='+', padx=20, pady=20, command=cl.btn_oper_plus)
btn_minus = Button(root, text='-', padx=20, pady=20, command=cl.btn_oper_minus)
btn_delenie = Button(root, text='/', padx=20, pady=20, command=cl.btn_oper_delenie)
btn_umnojenie = Button(root, text='*', padx=20, pady=20, command=cl.btn_oper_umnojenie)
btn_ravno = Button(root, text='=', padx=60, pady=20, command=cl.btn_oper_ravno)
btn_stepen = Button(root, text='^', padx=20, pady=20, command=cl.btn_oper_stepen)
btn_ostatok = Button(root, text='%', padx=18, pady=20, command=cl.btn_oper_ostatok)
btn_clear = Button(root, text='Clear', padx=55, pady=20, command=cl.btn_oper_clear)
