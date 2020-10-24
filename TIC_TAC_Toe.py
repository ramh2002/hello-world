# Tic Tac Toe Game in Python


def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3']+'|')
    print(' --------')
    print(board['4'] + '|' + board['5'] +'|' + board['6']+'|')
    print(' --------')
    print(board['7'] + '|' + board['8'] + '|' + board['9']+'|')
    print(' --------')

def checkValidMove():
    print("That place is already filled.\nselect the new position")

def checkWin(won):
    print(" player " + won + " won"+" Game Over \n ")
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        tttGamePlay()
# Now we'll write the main function which has all the gameplay functionality.
def tttGamePlay():
    theBoard = {'1': '1', '2': '2', '3': '3',
                '4': '4', '5': '5', '6': '6',
                '7': '7', '8': '8', '9': '9'}

    board_keys = []

    for key in theBoard:
        board_keys.append(key)

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)

        move = input("Enter the number you want to move :")

        print("Player " + turn +" move: "+ move)
        if theBoard[move] == str(move):
            theBoard[move] = turn

            count += 1
        else:
            checkValidMove()
            continue


        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the top
                printBoard(theBoard)
                checkWin(turn)
                break

            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
                printBoard(theBoard)
                checkWin(turn)
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
                printBoard(theBoard)
                checkWin(turn)
                break

            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
                printBoard(theBoard)
                checkWin(turn)
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
                printBoard(theBoard)
                checkWin(turn)
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
                printBoard(theBoard)
                checkWin(turn)
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
                printBoard(theBoard)
                checkWin(turn)
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
                printBoard(theBoard)
                checkWin(turn)
                break

                # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
            restart = input("Do want to play Again?(y/n)")
            if restart == "y" or restart == "Y":
                tttGamePlay()

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

            # Now we will ask if player wants to restart the game or not.




tttGamePlay()