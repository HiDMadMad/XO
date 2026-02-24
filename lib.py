import random
from time import sleep


def draw_board(board:dict) ->None :
    print(board['top-left'] + ' | ' + board['top-mid'] + ' | ' + board['top-right'] + '\n' +
          "---------" + '\n' +
          board['mid-left'] + ' | ' + board['mid-mid'] + ' | ' + board['mid-right'] + '\n' +
          "---------" + '\n' +
          board['low-left'] + ' | ' + board['low-mid'] + ' | ' + board['low-right'] + '\n' )


def awesome_print(text:str, delay:float=0.02):
    for t in text:
        print(t, end='')
        sleep(delay)
    print()


def get_player_sign() ->str :
    while(True):
        awesome_print("\nyou wanna be 'X' or 'O' ?")
        sign = input(">> ")
        if(sign.upper() == 'E'):
            return 'E'
        elif(sign.upper() == 'X'):
            return 'X'
        elif(sign.upper() == 'O'):
            return 'O'
        else:
            awesome_print("enter 'X' or 'O'... (or E to exit)\n")


def who_plays_first(name1:str="bot", name2:str="player") ->str :
    if(random.randint(0, 1) == 0):
        return name1
    else:
        return name2


def is_empty(board:dict, board_index:str) ->bool :
    return (board[board_index] == ' ')


def there_is_empty(board:dict):
    for b in board.values():
        if(b == ' '):
            return True
    else:
        return False
    

def player_choose(board:dict, player_sign:str, player_name:str="you") ->None :
    while(True):
        awesome_print("what row do you want to play? (top, mid, low)")
        row = input(">> " )
        if(row in ["top", "mid", "low"]):
            awesome_print("\nwhat column do you want to play? (left, mid, right)")
            col = input(">> " )
            if(col in ["left", "mid", "right"]):
                key = row+'-'+col
                awesome_print('\n\n' + player_name + " choose \'" + key + '\'\n')
                if(is_empty(board, key)):
                    board[key] = player_sign
                    draw_board(board)
                    break
                else:
                    awesome_print("it's already chosen\n")
            else:
                awesome_print("choose between 'left', 'mid' and 'right'\n")
        else:
            awesome_print("choose between 'top', 'mid' and 'low'\n")
    

def bot_choose(board:dict, bot_sign:str):
    empties = []
    for b in board.items():
        if(b[1] == ' '):
            empties.append(b[0])

    bot_key = random.choice(empties)
    board[bot_key] = bot_sign
    awesome_print("\nbot choose \'" + bot_key + '\'')
    draw_board(board)


def is_winner(board:dict, sign:str) ->bool :
    return (
        (board["top-left"]==sign and board["top-mid"]==sign and board["top-right"]==sign)
        or
        (board["mid-left"]==sign and board["mid-mid"]==sign and board["mid-right"]==sign)
        or
        (board["low-left"]==sign and board["low-mid"]==sign and board["low-right"]==sign)
        or
        (board["top-left"]==sign and board["mid-left"]==sign and board["low-left"]==sign)
        or
        (board["top-mid"]==sign and board["mid-mid"]==sign and board["low-mid"]==sign)
        or
        (board["top-right"]==sign and board["mid-right"]==sign and board["low-right"]==sign)
        or
        (board["top-left"]==sign and board["mid-mid"]==sign and board["low-right"]==sign)
        or
        (board["top-right"]==sign and board["mid-mid"]==sign and board["low-left"]==sign)
    )
#MadMad_105