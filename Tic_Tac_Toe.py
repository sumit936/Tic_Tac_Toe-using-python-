#Imnporting relevant libraries
from random import randint
import os

#function for displying the board

def display_board(board):
    print(f'|\t{board[1]}\t|\t{board[2]}\t|\t{board[3]}\t|')
    print('|\t\t|\t\t|\t\t|')
    print('-'*50)
    print(f'|\t{board[4]}\t|\t{board[5]}\t|\t{board[6]}\t|')
    print('|\t\t|\t\t|\t\t|')
    print('-'*50)
    print(f'|\t{board[7]}\t|\t{board[8]}\t|\t{board[9]}\t|')
    print('|\t\t|\t\t|\t\t|')
    print('-'*50)

#function for taking player's input
def player_input():
    while True:
        player1 = input("Please pick a marker 'X' or 'O': ").upper()
        if player1!='X' and player1!='O':
            continue
        else:
            if player1 == "X":
                player2 = "O"
            else:
                player2 = "X"
            break
    return (player1, player2)

#function for updataing the board list object
def place_marker(board, marker, position):
    board[position] = marker

# function to check the win of either player

def win_check(board, mark):

    if ((board[1]==board[2]==board[3]==mark) or (board[4]==board[5]==board[6]==mark) or (board[7]==board[8]==board[9]==mark) or
    (board[1]==board[4]==board[7]==mark) or (board[2]==board[5]==board[8]==mark) or (board[3]==board[6]==board[9]==mark) or
    (board[1]==board[5]==board[9]==mark) or (board[3]==board[5]==board[7]==mark)
    ):
        return True
    return False


# function to decide which player goes first
def choose_first():
    if randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
# function to check if the particular position is available

def space_check(board,position):

    return board[position]==''

# function to check if the board is full 

def full_board_check(board):
    for i in board:
        if i=='':
            return False
    return True

#function to ask for the palyer's next position

def player_choice(board):
    while True:
        pos = int(input("Enter your position: "))
        if pos<=9:
            if not space_check(board,pos):
                print('space is not available!\nPlease choose different position')
                continue
            else:
                break
        else:
            print('\nPlease enter valid position')
            continue
    return pos

#function to ask if player wants to replay
def replay():
    while True:
        rep = input('Want to replay? [y/n]: ').lower()
        if rep!='y' and rep!='n':
            print('Enter valid input!')
            continue
        elif rep=='y':
            return True
        else:
            break
    return False

#function to clear the output screen

def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 

#Driver Function
if __name__ == '__main__':
    while True:
        try:
            print("Welcome to Tic Tac Toe game!\n\n".center(80))
            b = ['#','1','2','3','4','5','6','7','8','9']
            while True:
                real_board = ['']*10
                display_board(b)
                print('\n\nNumbers is representing the positions!')
                player1, player2 = player_input()
                turn = choose_first()
                play_game = input('\n\nAre you ready to play? [y/n].')
    
                if play_game.lower()[0] == 'y':
                    game_on = True
                else:
                    game_on = False

                while game_on:
                    if not full_board_check(real_board):
                        if turn=='player1':
                            print("\n\nPlayer1's turn!")
                            turn = 'player2'
                            pos = player_choice(real_board)
                            place_marker(real_board, player1, pos)
                            clear()
                            display_board(real_board)
                            if win_check(real_board, player1):
                                print("\n\nPlayer1 wins!".center(80))
                                break
                            else:
                                continue
                        else:
                            print("\n\nPlayer2's turn!")
                            turn = 'player1'
                            if not full_board_check(real_board):
                                pos = player_choice(real_board)
                                place_marker(real_board, player2, pos)
                                clear()
                                display_board(real_board)
                                if win_check(real_board, player2):
                                    print("\n\nPlayer2 wins!".center(80))
                                    break
                                else:
                                    continue
                    else:
                        print("\n\nGame Draw!".center(80))
                        break
                if not replay():
                    break
            break
        except:
            print("\n\nSomething went wrong!\n")
            while True:
                inp = input('Do you want to restart the game [y/n]: ').lower()
                if inp!='y' and inp!='n':
                    print('Please enter valid input!')
                    continue
                else:
                    break
            if inp=='y':
                continue
            else:
                break