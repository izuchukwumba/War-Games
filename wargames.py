import random
from tictactoe import play_tictactoe

def print_blue(text):
    red_code = "\033[1;36m"  
    reset_code = "\033[0m" 
    print(f"{red_code}{text}{reset_code}")


ANSWER = ""
ACCESS_CODE = "TORNADO"

print_blue("Greetings, Professor Grabowski!")
print_blue("Shall we play a game?")
ANSWER = input()
if ANSWER.lower() in ["yes", "y"]:
    print_blue("List of games:")
    print_blue("1. CyberWar")
    print_blue("2. Tic-Tac-Toe")
    answer_second = input()
    if answer_second.upper() == "CYBERWAR":
        print_blue("Access to the simulated computer system is restricted.")
        print_blue("Hint: Think of the code associated with your college\'s mascot.")
        print_blue("Enter access code:")
        answer_third = input()
        if answer_third.upper() == ACCESS_CODE:
            print_blue("Access granted. Initiating simulated cyberwar scenario...")
            # display_cities()
        else:
            print_blue("Access denied. Terminating session.")
    elif answer_second.upper() == "TIC-TAC-TOE" or answer_second.upper() == "TICTACTOE" or answer_second.upper() == "TIC":
        play_tictactoe()
    else:
        print_blue("Invalid game choice.")
else:
    print_blue("Farewell! Maybe next time.")


