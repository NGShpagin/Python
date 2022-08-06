# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# # tkinter

from tkinter import *
import random


def click_button_plvspl():
    global game_run
    game_run = False
    window_2


def start_game_vs_player():
    window_2.destroy()
    global first_pl
    global second_pl
    first_pl = entry_lb1.get()
    second_pl = entry_lb2.get()


def click_button_plvsbot():
    nameWindow = Toplevel(window_1)
    nameWindow.title("Крестики - Нолики")
    nameWindow.geometry("300x300")
    lbl_pl1 = Label(nameWindow, text="Введите имя игрока:").pack()
    entry_lb1 = Entry(nameWindow)
    entry_lb1.pack()
    btn_start = Button(
        nameWindow,
        text="Начать игру",
        width=15,
        height=1,
        bg="blue",
        fg="black",
        command=start_game_vs_bot()
    ).pack()


def start_game_vs_bot():
    vsBotGameWindow = Toplevel(window_1)
    vsBotGameWindow.title("Крестики - Нолики. Player VS Bot")
    vsBotGameWindow.geometry("300x300")
    game_run = True
    field = []
    for row in range(3):
        line = []
        for column in range(3):
            button = Button(
                vsBotGameWindow, text=' ', 
                width=4, height=2, 
                font=('Verdana', 20, 'bold'),
                background='lavender',
                command=lambda row=row, column=column: click(row, column)
            )
            button.grid(row=row, column=column, sticky='nsew')
            line.append(button)
        field.append(line)

    def click(row, column):
        if game_run and field[row][column]['text'] == ' ':
            field[row][column]['text'] = 'X'
            global cross_count
            cross_count += 1
            check_win('X')
            if game_run and cross_count < 5:
                computer_move()
                check_win('O')
    
    def check_win(symbol):
        for i in range(3):
            check_line(field[i][0], field[i][1], field[i][2], symbol)
            check_line(field[0][i], field[1][i], field[2][i], symbol)
        check_line(field[0][0], field[1][1], field[2][2], symbol)
        check_line(field[2][0], field[1][1], field[0][2], symbol)


    def check_line(pos1, pos2, pos3, symbol):
        if pos1['text'] == symbol and pos2['text'] == symbol and pos3['text'] == symbol:
            pos1['background'] = pos2['background'] = pos3['background'] = 'green'
            global game_run
            game_run = False

    def computer_move():
        for i in range(3):
            if can_win(field[i][0], field[i][1], field[i][2], 'O'):
                return
            if can_win(field[0][i], field[1][i], field[2][i], 'O'):
                return
        if can_win(field[0][0], field[1][1], field[2][2], 'O'):
            return
        if can_win(field[2][0], field[1][1], field[0][2], 'O'):
            return
        for i in range(3):
            if can_win(field[i][0], field[i][1], field[i][2], 'X'):
                return
            if can_win(field[0][i], field[1][i], field[2][i], 'X'):
                return
        if can_win(field[0][0], field[1][1], field[2][2], 'X'):
            return
        if can_win(field[2][0], field[1][1], field[0][2], 'X'):
            return
        while True:
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            if field[row][column]['text'] == ' ':
                field[row][column]['text'] = 'O'
                break

    def can_win(pos1, pos2, pos3, symbol):
        result = False
        if pos1['text'] == symbol and pos2['text'] == symbol and pos3['text'] == ' ':
            pos3['text'] = 'O'
            result = True
        if pos1['text'] == symbol and pos2['text'] == ' ' and pos3['text'] == symbol:
            pos2['text'] = 'O'
            result = True
        if pos1['text'] == ' ' and pos2['text'] == symbol and pos3['text'] == symbol:
            pos1['text'] = 'O'
            result = True
        return result

    def new_game():
        for row in range(3):
            for column in range(3):
                field[row][column]['text'] = ' '
                field[row][column]['background'] = 'lavender'
        global game_run
        game_run = True
        global cross_count
        cross_count = 0

    new_game_button = Button(vsBotGameWindow, text='Новая игра', width='20', command=new_game)
    new_game_button.grid(row=3, column=0, columnspan=3)


window_1 = Tk()
window_1.title("Крестики-Нолики")
game_run = True

greeting = Label(
    window_1,
    text="Добро пожаловать в игру!",
    fg="red",
    bg="black", 
    width=0,
    height=0)
greeting.grid(row=0, column=0, columnspan=2)

my_lbl = Label(window_1, text=' ')
my_lbl.grid(row=1, column=0, columnspan=2)

btn_plvspl = Button(
    window_1,
    text="Player VS Player",
    width=15,
    height=1,
    bg="blue",
    fg="black",
    command=click_button_plvspl)
btn_plvspl.grid(row=2, column=1)

btn_plvsbott = Button(
    window_1,
    text="Player VS Bot",
    width=15,
    height=1,
    bg="blue",
    fg="black",
    command=click_button_plvsbot)
btn_plvsbott.grid(row=2, column=0)

while game_run:
    window_1.mainloop() 


window_2 = Tk()
window_2.title("Крестики - Нолики")
window_2.geometry("450x300")

lbl_pl1 = Label(window_2, text="Введите имя игрока 1:", borderwidth=3)
lbl_pl1.grid(row=0, column=0)

entry_lb1 = Entry(window_2, borderwidth=5)
entry_lb1.grid(row=0, column=1)

lbl_pl2 = Label(window_2, text="Введите имя игрока 2:", borderwidth=3)
lbl_pl2.grid(row=1, column=0)

entry_lb2 = Entry(window_2, borderwidth=5)
entry_lb2.grid(row=1, column=1)

btn_start = Button(
    window_2,
    text="Начать игру",
    width=15,
    height=1,
    bg="blue",
    fg="black",
    command=start_game_vs_player)
btn_start.grid(row=2, column=0, columnspan=2)


window_2.mainloop()