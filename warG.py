ANSWER = ""
ACCESS_CODE_1 = "TORNADO"
ACCESS_CODE_2 = "JOSHUA"

#Blue Text
def print_blue(text):
    red_code = "\033[1;36m"  
    reset_code = "\033[0m" 
    print(f"{red_code}{text}{reset_code}")

#TICTACTOE GAMEPLAY STARTS HERE
def play_tictactoe():    
    def intro():
    # This function introduces the rules of the game Tic Tac Toe
        print_blue("Let's play Tic-Tac-Toe!")
        input("Press enter to continue.")
        print_blue("\n")

    def create_grid():
    # This function creates a blank playboard
        print_blue("Here is the playboard: ")
        board = [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]]        
        return board

    def sym():
    # This function decides the players' symbols
        symbol_1 = input("Player 1, do you want to be X or O? ")
        if symbol_1 == "X":
            symbol_2 = "O"
            print_blue("Player 2, you are O. ")
        else:
            symbol_2 = "X"
            print_blue("Player 2, you are X. ")
        input("Press enter to continue.")
        print_blue("\n")
        return (symbol_1, symbol_2)

    def startGamming(board, symbol_1, symbol_2, count):
    # This function starts the game.

        # Decides the turn
        if count % 2 == 0:
            player = symbol_1
        elif count % 2 == 1:
            player = symbol_2
        print_blue("Player "+ player + ", it is your turn. ")
        row = int(input("Pick a row:"
                        "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                        "[left column: enter 0, middle column: enter 1, right column enter 2]"))
        # Check if players' selection is out of range
        while (row > 2 or row < 0) or (column > 2 or column < 0):
            outOfBoard(row, column)
            row = int(input("Pick a row[upper row:"
                            "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
            column = int(input("Pick a column:"
                            "[left column: enter 0, middle column: enter 1, right column enter 2]"))
            # Check if the square is already filled
        while (board[row][column] == symbol_1)or (board[row][column] == symbol_2):
            filled = illegal(board, symbol_1, symbol_2, row, column)
            row = int(input("Pick a row[upper row:"
                            "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
            column = int(input("Pick a column:"
                                "[left column: enter 0, middle column: enter 1, right column enter 2]"))    
        # Locates player's symbol on the board
        if player == symbol_1:
            board[row][column] = symbol_1
                
        else:
            board[row][column] = symbol_2
        
        return (board)

    def isFull(board, symbol_1, symbol_2):
        count = 1
        winner = True
    # This function check if the board is full
        while count < 10 and winner == True:
            gaming = startGamming(board, symbol_1, symbol_2, count)
            pretty = printPretty(board)
            
            if count == 9:
                print_blue("The board is full. Game over.")
                if winner == True:
                    print_blue("There is a tie. ")
            # Check if here is a winner
            winner = isWinner(board, symbol_1, symbol_2, count)
            count += 1
        if winner == False:
            print_blue("Game over.")
        # This is function gives a report 
        report(count, winner, symbol_1, symbol_2)

    def outOfBoard(row, column):
    # This function tells the players that their selection is out of range
        print_blue("Out of boarder. Pick another one. ")
        
    def printPretty(board):
    # This function print_blues the board nice!
        rows = len(board)
        cols = len(board)
        print_blue("---+---+---")
        for r in range(rows):
            print(board[r][0], " |", board[r][1], "|", board[r][2])
            print_blue("---+---+---")
        return board

    def isWinner(board, symbol_1, symbol_2, count):
    # This function checks if any winner is winning
        winner = True
        # Check the rows
        for row in range (0, 3):
            if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
                winner = False
                print_blue("Player " + symbol_1 + ", you won!")
    
            elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
                winner = False
                print_blue("Player " + symbol_2 + ", you won!")
                
        # Check the columns
        for col in range (0, 3):
            if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
                winner = False
                print_blue("Player " + symbol_1 + ", you won!")
            elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
                winner = False
                print_blue("Player " + symbol_2 + ", you won!")

        # Check the diagnoals
        if board[0][0] == board[1][1] == board[2][2] == symbol_1:
            winner = False 
            print_blue("Player " + symbol_1 + ", you won!")

        elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
            winner = False
            print_blue("Player " + symbol_2 + ", you won!")

        elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
            winner = False
            print_blue("Player " + symbol_1 + ", you won!")

        elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
            winner = False
            print_blue("Player " + symbol_2 + ", you won!")

        return winner
        
    def illegal(board, symbol_1, symbol_2, row, column):
        print_blue("The square you picked is already filled. Pick another one.")

    def report(count, winner, symbol_1, symbol_2):
        print_blue("\n")
        input("Press enter to see the game summary. ")
        if (winner == False) and (count % 2 == 1 ):
            print_blue("Winner : Player " + symbol_1 + ".")
        elif (winner == False) and (count % 2 == 0 ):
            print_blue("Winner : Player " + symbol_2 + ".")
        else:
            print_blue("There is a tie. ")
    
    # The main command
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    symbol_1, symbol_2 = sym()
    full = isFull(board, symbol_1, symbol_2) # The function that starts the game is also in here.


# CYBERWAR STARTS HERE

def thermo_nuclear_war():

    #MAPS
    usa_map = '''
            UNITED STATES
        ,------~~v,                
        |'         Ż\   ,__/Ż||    
        /             \,/     /     
        |                    /      
        \                   |       
        \                 /        
        ^Ż~_            /         
            '~~,  ,Ż~Ż\ \         
                \/     \/ '''

    soviet_map='''
                SOVIET UNION      
                    _--^\\
                    _/    /,_
        ,,   ,,/^      Ż  vŻv-__
        |'~^Ż                   Ż\\
        _/                     _  /^
        /                   ,~~^/|ŻŻ
        |          __,,  v__\   \/
        ^~       /    ~Ż  //
        \~,  ,/         Ż
            ~~'''



    def maps_both():
        # Split the strings into lines
        usa_lines = usa_map.split('\n')
        soviet_lines = soviet_map.split('\n')

        # Zip the lines together and print side by side
        for usa_line, soviet_line in zip(usa_lines, soviet_lines):
            print_blue(f"{usa_line.ljust(40)}{soviet_line}")

    initial_prompt = "Simulated computer system activated."
    maps = maps_both()
    ANSWER = ""
    print_blue("Simulated computer system activated.")
    print_blue("Pick a side (input number).")
    print_blue("1. USA")
    print_blue("2. Soviet Union")
    ANSWER = input()
    if ANSWER.upper() == "USA" or ANSWER == str(1):
        print_blue("You are now fighting for the United States of America!")
        print_blue(usa_map)
    else:
        print_blue("You are now fighting for the Soviet Union.")
        print_blue(soviet_map)


    





#Initial Text Prompt
def _init_():
    print_blue("Greetings, Professor Grabowski!")
    print_blue("Shall we play a game?")
    ANSWER = input()
    if ANSWER.lower() in ["yes", "y"]:
        print_blue("List of games: Choose a number")
        print_blue("1. Global Thermonuclear War")
        print_blue("2. Tic-Tac-Toe")
        print_blue("3. Chess")
        print_blue("4. Cyberwar")
        print_blue("5. Battleship")



        answer_second = input()
        if answer_second == str(1) or answer_second.upper() == "CYBERWAR" or answer_second.upper() == "WAR" or answer_second.upper() == "NUCLEAR" or answer_second.upper() == "THERMO" or answer_second.upper() == "GTW":
            print_blue("Access to the simulated computer system is restricted.")
            print_blue("Hint: Think of the code associated with your college\'s mascot.")
            print_blue("Enter access code:")
            answer_third = input()
            if answer_third.upper() == ACCESS_CODE_1 or answer_third.upper() == ACCESS_CODE_2:
                print_blue("Access granted. Initiating simulated cyberwar scenario...")
                thermo_nuclear_war()
            else:
                print_blue("Access denied. Terminating session.")
        elif answer_second == str(2) or answer_second.upper() == "TIC-TAC-TOE" or answer_second.upper() == "TICTACTOE" or answer_second.upper() == "TIC":
            play_tictactoe()
        else:
            print_blue("Invalid game choice.")
    else:
        print_blue("Farewell! Maybe next time.")

_init_()
