import random
from tictactoe import play_tictactoe
from print_blue import print_blue
from maps import thermo_nuclear_war
# import maps

ANSWER = ""
ACCESS_CODE_1 = "TORNADO"
ACCESS_CODE_2 = "JOSHUA"


print_blue("Greetings, Professor Grabowski!")
print_blue("Shall we play a game?")
ANSWER = input()
if ANSWER.lower() in ["yes", "y"]:
    print_blue("List of games: Choose a number")
    print_blue("1. Global Thermonuclear War")
    print_blue("2. Tic-Tac-Toe")
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




