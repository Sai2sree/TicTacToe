print('Welcome to Tic Tac Toe!');


"""
This function asks whether to start the game.
Use while loop to continually ask until we get a correct answer.
"""
def start_game():

    while True:

        response = input('Do you want to start the game, Yes or No?'  );
        if response.lower() == 'yes':
            return True;
        elif response.lower() == 'no':
            print("ok, bye! See you later!");
            return False;
        else:
            print("Please type Yes or No");

            
            
"""
This function returns a boolean indicating whether a space on the board is freely available.
"""
def space_check(board):
    for i in board[1:]:
        if i==' ':
            return True;
    return False;



"""
This function can take in a player input and assign their marker as 'X' or 'O'. 
It uses while loop to continually ask until we get a correct answer.
"""
def player_input():
    player1 = input('Player 1, do you want to be "X" or "O"? ');
    print(player1);
    while (player1.lower() !='x' and player1.lower() !='o'):
        print("Invalid input. Please select one of them");
        player1 = input('Do you want to be "X" or "O"? ');
    else:
        print("Thanks! You have selected {}".format(player1));
        print("So, the players indicators are as follows");
        if player1.lower() == 'x':
            player2 = 'O';
        else:
            player2 = 'X';
        print('player1 : {}'.format(player1.upper()));
        print('player2 : {}'.format(player2.upper()));
        print("Player 1 will go first!");
    return (player1, player2);



"""
This function prints out a board. 
Sets up the board as a list, where each index 1-9 corresponds with a number on a number pad, 
so that we get a 3 by 3 board representation.
"""
def display_board(board):
    print('         |              |        ');
    print('    {}    |      {}       |      {}'.format(board[7], board[8], board[9]));
    print('         |              |        ');
    print('---------------------------------');
    print('         |              |        ');
    print('    {}    |      {}       |      {}'.format(board[4], board[5], board[6]));
    print('         |              |        ');
    print('---------------------------------');
    print('         |              |        ');
    print('    {}    |      {}       |      {}'.format(board[1], board[2], board[3]));
    print('         |              |        ');

    
    
"""
This function that takes in the board list object, a marker ('X' or 'O'), 
and a desired position (number 1-9) and assigns it to the board.

"""
def place_marker(board, marker, position):
    board[position] = marker;
    return board;        



"""
This function takes in the board list object,
Validates the position object, given by the user.
It uses while loops to continually ask until we get a correct answer.
"""
def select_position(board):
    while True:
        
        try:
            n = int(input("Please select a number in range (1-9): "));
            if board[n] == ' ' and n/n:
                return n;
            else:
                print("This position is already filled. Please select another number.")
        except:
            print("Invalid input. Please select a number in range (1-9)")

            
                        
"""
This function takes in a board and a mark (X or O) 
and then checks to see if that mark has won.
"""
def win_check(board, a):
    if board[1] == board [2] == board [3] == a:
        return True;
    
    elif board[4] == board [5] == board [6] == a:
        return True;
    
    elif board[7] == board [8] == board [9] == a:
        return True;
    
    elif board[1] == board [5] == board [9] == a:
        return True;
    
    elif board[3] == board [5] == board [7] == a:
        return True;
    
    elif board[1] == board [4] == board [7] == a:
        return True;
    
    elif board[2] == board [5] == board [8] == a:
        return True;
    
    elif board[3] == board [6] == board [9] == a:
        return True;

    else:
        return False;

    
    
"""
This function asks the player if they want to play again
and returns a boolean True if they do want to play again.
It uses while loop to continually ask until we get correct answer. 
"""
def replay():

    while True:

        response = input('Do you want to play again, Yes or No?'  );
        if response.lower() == 'yes':
            ticTacToe();
            return True;
        elif response.lower() == 'no':
            print("ok, bye! See you later!");
            return False;
        else:
            print("Please type Yes or No");

        

"""
This is the main function that runs the game using all the above functions. 
"""
def ticTacToe():
    board = [' ']*10;
    if start_game():
        while True:
            print("Game has started!");
            player_input();
            break;

        while True :

            if space_check(board):
                    
                #Player 1 Turn
                print("Hi, Player 1");
                display_board(place_marker(board, 'X', select_position(board)));
                if win_check(board, 'X'):
                    print("Player 1 has won!");
                    break;

            if space_check(board):
                print("Now, its Player 2 turn");

                # Player2's turn.
                print("Hi, Player 2");
                display_board(place_marker(board, 'O', select_position(board)));
                if win_check(board, 'O'):
                    print("Player 2 has won!");
                    break;

            else:
                print("It's  a draw!!!")
                break;

        replay();


ticTacToe();
