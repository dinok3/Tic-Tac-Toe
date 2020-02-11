#TIC-TAC-TOE

#board
#display board
#play game
#handle turn
#check win
   #chech rows
   #check colums
   #chech diagnols
#check tie
#flip player

#----Global variable----

#game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

#if game is still going
game_still_going = True

#Who won?orTie
winner = None

#Whos turn is it
current_player = 'X'

#display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#Play TIC-TAC-TOE
#MAIN FUNCTION
def play_game():

    #display initial board
    display_board()

    #While game is still going
    while game_still_going:
        
        #handle a single turn of an arbitrary player
        handle_turn(current_player)
        
        #check if game has ended
        check_if_game_over()
        
        #Flip to other player
        flip_player()

    #The game has ended
    if winner =='X' or winner == 'O':
        print(winner + ' won.')
    elif winner == None:
        print('Tie.')
        


def handle_turn(player):
    
    #tells whos player is turn and ask to give some position
    print(player + "'s turn.")
    position = input("Chose a position from 1-9: ")

    valid = False
    #while they input smth wrong ask them to input again
    while not valid:
        
        #while position is not in board
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            #ask them to input again
            position = input("Invalid input.Chose a position from 1-9: ")
            
        #python is from 0 - 8 so if input is 1 that will be on 0 python position(first)
        position = int(position) - 1
        
        if board[position] == "-":
            valid = True
        else:
            print('You cant go there.Go again.')
            
    #in board[position] will show off X or O
    board[position] = player
    
    #display board
    display_board()
    
#check if game is over
def check_if_game_over():
    #check if win
    check_if_win()
    #check if tie
    check_if_tie()


def check_if_win():
    #we need this for acces to global variables
    global winner
    
    #check_rows
    row_winner = check_rows()
    #check_columns
    column_winner = check_columns()
    #check_diagnols
    diagonal_winner = check_diagonals()
    
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
   

def check_rows():
    
    #include variable game_still going from global variables
    global game_still_going
    
    #check if theres any row winner
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    #if theres any row winner then the game is over
    if row_1 or row_2 or row_3:
        game_still_going = False
        
    #if X is on position board[0] it will print X
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]


def check_columns():
    
    #include variable game_still going from global variables
    global game_still_going
    
    #check if theres any column winner
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    #if theres any column winner then the game is over
    if column_1 or column_2 or column_3:
        game_still_going = False
        
    #if X is on position board[0] it will print X
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]

    
def check_diagonals():
    #include variable game_still going from global variables
    global game_still_going
    
    #check if theres any diagonal winner
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    #if theres any diagonal winner then the game is over
    if diagonal_1 or diagonal_2:
        game_still_going = False
        
    #if X is on position board[0] it will print X
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[6]
    return

#check if tie
def check_if_tie():
    
    #include variable game_still going from global variables
    global game_still_going
    
    #If theres no free spot game is tie
    if "-" not in board:
        game_still_going = False
    
#Flip player
def flip_player():
    
    #include variable game_still going from global variables
    global current_player
    
    #if current player is X,then change it to O
    if current_player =='X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
   



#start the game
play_game()
