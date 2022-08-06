from tkinter import *
import buttons as bt


root = Tk()
root.title('Калькулятор')
my_string = Entry(root, width=40, borderwidth=5)
my_string.grid(row=0, column=0, columnspan = 5, padx=10, pady=20)


# Buttons place
bt.btn_1.grid(row=1, column=0)
bt.btn_2.grid(row=1, column=1)
bt.btn_3.grid(row=1, column=2)
bt.btn_4.grid(row=2, column=0)
bt.btn_5.grid(row=2, column=1)
bt.btn_6.grid(row=2, column=2)
bt.btn_7.grid(row=3, column=0)
bt.btn_8.grid(row=3, column=1)
bt.btn_9.grid(row=3, column=2)
bt.btn_0.grid(row=4, column=0)

bt.btn_clear.grid(row=4, column=1, columnspan=2)
bt.btn_ravno.grid(row=4, column=3, columnspan=2)

bt.btn_plus.grid(row=1, column=3)
bt.btn_minus.grid(row=1, column=4)
bt.btn_umnojenie.grid(row=2, column=3)
bt.btn_delenie.grid(row=2, column=4)
bt.btn_stepen.grid(row=3, column=3)
bt.btn_ostatok.grid(row=3, column=4)

root.mainloop()