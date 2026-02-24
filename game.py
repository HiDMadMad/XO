import lib

while(True):

    # it's const!
    board = {"top-left":' ', "top-mid":' ', "top-right":' ',
            "mid-left":' ', "mid-mid":' ', "mid-right":' ',
            "low-left":' ', "low-mid":' ', "low-right":' '}

    lib.awesome_print("\n\n1.play with bot\n2.play with another player\n3.exit", 0.01)
    game_mode = input(">> ")
    match(game_mode):
        case '1':
            player_sign = lib.get_player_sign()
            if(player_sign == 'E'):
                lib.awesome_print("back to main menu..")
                continue
            bot_sign = 'O' if player_sign=='X' else 'X'

            lib.awesome_print("\nplayer is : " + player_sign + "\nbot is : " + bot_sign)

            whose_turn = lib.who_plays_first()
            lib.awesome_print('\n' + whose_turn + " play's first")

            lib.awesome_print("let's play..\n")
            while(lib.there_is_empty(board)):
                if(whose_turn == 'player'):
                    lib.player_choose(board, player_sign)
                    if(lib.is_winner(board, player_sign)):
                        lib.awesome_print("YOU WIN!!!")
                        break
                    whose_turn = 'bot'
                elif(whose_turn == 'bot'):
                    lib.bot_choose(board, bot_sign)
                    if(lib.is_winner(board, bot_sign)):
                        lib.awesome_print("BOT WINS!!!")
                        break
                    whose_turn = 'player'
            else:
                lib.awesome_print("DRAW.")
            lib.awesome_print("well played.")


        case '2':
            player1_sign = lib.get_player_sign()
            if(player1_sign == 'E'):
                lib.awesome_print("back to main menu..")
                continue
            player2_sign = 'O' if player1_sign=='X' else 'X'

            lib.awesome_print("\nplayer1 is : " + player1_sign + "\nplayer2 is : " + player2_sign)

            whose_turn = lib.who_plays_first("player1", "player2")
            lib.awesome_print('\n' + whose_turn + " play's first")

            lib.awesome_print("let's play..\n")
            while(lib.there_is_empty(board)):
                if(whose_turn == 'player1'):
                    lib.player_choose(board, player1_sign, "player1")
                    if(lib.is_winner(board, player1_sign)):
                        lib.awesome_print("player1 WINS!!!")
                        break
                    whose_turn = 'player2'
                elif(whose_turn == 'player2'):
                    lib.player_choose(board, player2_sign, "player2")
                    if(lib.is_winner(board, player2_sign)):
                        lib.awesome_print("player2 WINS!!!")
                        break
                    whose_turn = 'player1'
            else:
                lib.awesome_print("DRAW.")
            lib.awesome_print("well played.")


        case '3':
            lib.awesome_print("hope to see you soon.\n")
            break

        case _:
            lib.awesome_print("look at menu more careful :)\n")
#MadMad_81