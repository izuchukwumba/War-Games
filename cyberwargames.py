COUNTRIES = [
    {"NAME": "UnitedStates", "CITIES": [
        {"NAME": "NewYork", "CYBER-INTEGRITY": random.randint(0, 100)},
        {"NAME": "WashingtonDC", "CYBER-INTEGRITY": random.randint(0, 100)}
    ]},
    {"NAME": "Ghana", "CITIES": [
        {"NAME": "Accra", "CYBER-INTEGRITY": random.randint(0, 100)},
        {"NAME": "Kumasi", "CYBER-INTEGRITY": random.randint(0, 100)}
    ]},
    {"NAME": "DominicanRepublic", "CITIES": [
        {"NAME": "SantoDomingo", "CYBER-INTEGRITY": random.randint(0, 100)},
        {"NAME": "Santiago", "CYBER-INTEGRITY": random.randint(0, 100)}
    ]}
]

print("Simulated computer system activated.")
print("Potential targets:")
for COUNTRY_INDEX in range(1, 4):
    print(COUNTRY_INDEX, ". ", COUNTRIES[COUNTRY_INDEX]["NAME"])
    print("Select a target:")
ANSWER = input()
print("Selected target: ", COUNTRIES[ANSWER]["NAME"])
print("Commencing simulated cyberwar attack on ", COUNTRIES[ANSWER]["NAME"], "...")
WAIT_FOR_RESPONSE()
print("Cyber integrity status: ", COUNTRIES[ANSWER]["CITIES"][1]["NAME"], " - ", COUNTRIES[ANSWER]["CITIES"][1]["CYBER-INTEGRITY"], "%")
print(COUNTRIES[ANSWER]["CITIES"][2]["NAME"], " - ", COUNTRIES[ANSWER]["CITIES"][2]["CYBER-INTEGRITY"], "%")

# def PLAY_TIC_TAC_TOE():
#     BOARD = [[" " for _ in range(3)] for _ in range(3)]
#     print("Let's play Tic-Tac-Toe!")
#     DISPLAY_BOARD()
#     while not GAME_OVER:
#         MOVE_PLAYER('X')
#         DISPLAY_BOARD()
#         if GAME_OVER:
#             break
#         MOVE_PLAYER('O')
#         DISPLAY_BOARD()

# def MOVE_PLAYER(PLAYER):
#     print("Player ", PLAYER, ", enter your move (row[1-3] column[1-3]): ")
#     ANSWER = input()
#     BOARD[int(ROW_FROM_ANSWER)][int(COLUMN_FROM_ANSWER)] = PLAYER


# def display_board():
#     board =[
#         [" ", " ", " "],
#         [" ", " ", " "],
#         [" ", " ", " "]
#         ]
#     print("Current Tic-Tac-Toe Board:")
#     print("   1   2   3")
#     print("1", board[0][0], "|", board[0][1], "|", board[0][2])
#     print("  ---+---+---")
#     print("2", board[1][0], "|", board[1][1], "|", board[1][2])
#     print("  ---+---+---")
#     print("3", board[2][0], "|", board[2][1], "|", board[2][2])
#     print()

# display_board()

# def game_over():
#     pass

#     if (BOARD[0][0] == BOARD[0][1] == BOARD[0][2] != " "):
#         print("Player", BOARD[0][0], "wins!")
#         return True
#     elif (BOARD[1][0] == BOARD[1][1] == BOARD[1][2] != " "):
#         print("Player", BOARD[1][0], "wins!")
#         return True
#     elif (BOARD[2][0] == BOARD[2][1] == BOARD[2][2] != " "):
#         print("Player", BOARD[2][0], "wins!")
#         return True
#     elif (BOARD[0][0] == BOARD[1][0] == BOARD[2][0] != " "):
#         print("Player", BOARD[0][0], "wins!")
#         return True
#     elif (BOARD[0][1] == BOARD[1][1] == BOARD[2][1] != " "):
#         print("Player", BOARD[0][1], "wins!")
#         return True
#     elif (BOARD[0][2] == BOARD[1][2] == BOARD[2][2] != " "):
#         print("Player", BOARD[0][2], "wins!")
#         return True
#     elif (BOARD[0][0] == BOARD[1][1] == BOARD[2][2] != " "):
#         print("Player", BOARD[0][0], "wins!")
#         return True
#     elif (BOARD[0][2] == BOARD[1][1] == BOARD[2][0] != " "):
#         print("Player", BOARD[0][2], "wins!")
#         return True
#     elif (not any(" " in row for row in BOARD)):
#         print("It's a draw!")
#         return True
#     else:
#         return False

# ROW_FROM_ANSWER = int(ANSWER[0])
# COLUMN_FROM_ANSWER = int(ANSWER[2])

while True:
    print("Awaiting simulated response from", COUNTRIES[ANSWER].NAME, "...")
    ANSWER = input()
    print("Simulated response received:", ANSWER)
    print("Processing simulated response...")
    ANSWER = input()
    print("Processing simulated response...")
    ANSWER = input()



MAP = [
    {
        "NAME": "",
        "CITIES": [
            {
                "NAME": "",
                "CYBER-INTEGRITY": ""
            },
            {
                "NAME": "",
                "CYBER-INTEGRITY": ""
            }
        ]
    },
    {
        "NAME": "",
        "CITIES": [
            {
                "NAME": "",
                "CYBER-INTEGRITY": ""      
            },
            {
                "NAME": "",
                "CYBER-INTEGRITY": ""
            }
        ]
    },
    {
        "NAME": "",
        "CITIES": [
            {
                "NAME": "",
                "CYBER-INTEGRITY": ""
            },
            {
                "NAME": "",
                "CYBER-INTEGRITY": ""
            }
        ]
    }
]

def init_map():
    for country in MAP:
        country["NAME"] = ""
        for city in country["CITIES"]:
            city["NAME"] = ""
            city["CYBER-INTEGRITY"] = ""

def display_cities():
    for country in MAP:
        for city in country["CITIES"]:
            print(city["NAME"])


# Main procedure
init_map()