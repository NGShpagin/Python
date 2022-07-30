for i in range(3):
    i = {}
    for j in range(3):
        i[j] = ''
        print('|   ', end=' | ')
    print()
    print('--------------------')





def player2():
    if run_game:
        print('Player 1')
        posintion = input('x(1 - 3), y(1 - 3): ')
        pos = posintion.split()
        new_list = []
        for i in pos:
            new_list.append(int(i))
        print(new_list)
        if new_list[0][1] == '':
            new_list[0][1] = 'X'
        if 0[0] == 1[1] == 2[2] or 0[2] == 1[1] == 2[0] or 0[0] == 0[1] == 0[2] or 1[0] == 1[1] == 1[2] or 2[0] == 2[1] == 2[2] or 0[0]==1[0]==2[0] or 0[1]==1[1]==2[1] or 0[2]==1[2]==2[2]:
            run_game = False
            print('Player 2 win')
        else: 
            current_field
            player1

def player1():
    if run_game:
        print('Player 1')
        posintion = input('x(1 - 3), y(1 - 3): ')
        pos = posintion.split()
        new_list = []
        for i in pos:
            new_list.append(int(i))
        print(new_list)
        if new_list[0][new_list[1]] == '':
            new_list[0][new_list[1]] = 'X'
        if 0[0] == 1[1] == 2[2] or 0[2] == 1[1] == 2[0] or 0[0] == 0[1] == 0[2] or 1[0] == 1[1] == 1[2] or 2[0] == 2[1] == 2[2] or 0[0]==1[0]==2[0] or 0[1]==1[1]==2[1] or 0[2]==1[2]==2[2]:
            run_game = False
            print('Player 1 win')
        else: 
            current_field
            player2


def current_field():
    for el in range(3):
        for m in el.values():
            print(m, end='')
            print('|   ', end=' | ')
        print()
        print('--------------------')
    

run_game = True
player1


