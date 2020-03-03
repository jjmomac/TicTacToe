#---Global Variables--- begin

#game_playing is True while game is ON, when board is filled, it is turned off and check for winner or tie
game_playing = True
#initialize current player
current_player = ''

#initialize playing board
board = list(range(0, 10))

#----Global Variables--- end
 
#Patterns of winning combinations in tictactoe to check against
win_combinations = (
                (1, 2, 3),
                (4, 5, 6),
                (7, 8, 9),
                (1, 4, 7),
                (2, 5, 8),
                (3, 6, 9),
                (1, 5, 9),
                (3, 5, 7)
                )
 

# Function to call the game's functions to begin running the code             
def play_TicTacToe():

    global game_playing

    print("\n Welcome to Tic Tac Toe \n ")

    choose_token()

    print_board()

    while game_playing is True:

        choose_cell(current_player)
        
        if check_game_status():
            break

        change_player()


#Function to choose X or O
def choose_token():
 
    global current_player
 
    while not (current_player == 'X' or current_player == 'O'):
        current_player = input('Player 1, choose X or O?: \n').upper()

    if current_player == 'X':
        player1 = 'X'
        player2 = 'O'
        print('Player 1 is {} and player 2 is {}. Player {} goes first \n'.format(player1, player2, current_player))

    elif current_player == 'O':
        player1 = 'O'
        player2 = 'X'
        print('Player 2 is {} and player 1 is {}. Player {} goes first. \n'.format(player2, player1, current_player))

#This function will printout the playing board
def print_board():
    global board
    print(" {} | {} | {}".format(board[1], board[2], board[3]))
    print("__________")
    print(" {} | {} | {}".format(board[4], board[5], board[6]))
    print("__________")
    print(" {} | {} | {}".format(board[7], board[8], board[9]))
 

#This function will handle the cell choice and positioning on the board
def choose_cell(player):
 
    global current_player
    global board
    print("pick the appropriate number to choose slot: \n")
    valid_answer = False
 
    while valid_answer is False:

            position = int(input('player {} Choose a position on the board (1 - 9): \n'.format(current_player)))
            if position in range(0, 10) and board[position] != 'X' and board[position] != 'O':
                board[position] = player
                valid_answer = True
            else:
                print('You have entered an invalid position.')

    print_board()

#This function switches the players when the choose_cell() function is satisfied
def change_player():
    global current_player
 
    if current_player == "X":
        current_player = "O"
 
    elif current_player == "O":
        current_player = "X"

#Will check the board for any winning combinations or tie
def check_game_status():
    global game_playing
    global board
    valid_answer = False
 
    while valid_answer is False:
        
            if any (board[x] == board[y] == board[z] for x, y, z in win_combinations):
                print('congratulations Player {} you have won!'.format(current_player))
                valid_answer = True
                game_playing = False

            elif 9 == sum((cell == 'X' or cell == 'O') for cell in board):
                print("It's a tie!")
                valid_answer = True
                game_playing = False

            else:
                valid_answer = True
                pass


if __name__ == "__main__":
    play_TicTacToe()

#----------#
# I know that my work is not all that beautiful, but I try to make it understandable
# wish to be employed and to train further, I want to experience working in a team
# and be an effective member of the company
# My skills are still elementary as I am a fresh graduate, but everyday I learn new things
# and I want to learn more..