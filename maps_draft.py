# us_map = '''
#        ,__                                                  _,
#     \~\|  ~~---___              ,                          | \\
#      | Wash.| |   ~~~~~~~|~~~~~| ~~---,   _            VT_/,ME>
#     /~-_--__| |  Montana |N Dak\ Minn/ ~\~_/Mich.     /~| ||,'
#     |Oregon |  \         |------|   { WI / /~)     __-NY',|_\\,NH
#    /       |Ida.|~~~~~~~~|S Dak.\    \\   | | '~\\  |_____,|~,-'Mass.
#    |~~--__ |    | Wyoming|____  |~~~~~|--| |__ /_-'Penn.{,~Conn (RI)
#    |   |  ~~~|~~|        |    ~~\\ Iowa/  `-' |`~ |~_____{/NJ
#    |   | Nev |  '---------, Nebr.\\----|   |IN|OH,' ~/~\\,|`MD (DE)
#    ',  \     |Utah| Colo. |~~~~~~~|    \\IL| ,'~~\\WV/ VA |
#     |Cal\\    |    |       | Kansas| MO  \\_-~ KY /`~___--\\
#     ',   \\  ,-----|-------+-------'_____/__----~~/N Car./
#      '_   '\\|     |      |~~~|Okla.|    | Tenn._/-,~~-,/
#        \\    |Ariz.| New  |   |_    |Ark./~~|~~\\    \\,/S Car.
#         ~~~-'     | Mex. |     `~~~\\___|MS |AL | GA /
#             '-,_  | _____|          |  /   | ,-~---~\\
#                 `~'~  \\    Texas    |LA`--,~~~~-~~,FL\\
#                        \\/~\\      /~~~`---`         |  \\
#                            \\    /                   \\  | 
#                             \\  |                     '\\'
#                              `~'
# '''

# def print_blue(text):
#     red_code = "\033[1;36m"  
#     reset_code = "\033[0m" 
#     print(f"{red_code}{text}{reset_code}")

# print_blue(us_map)



def replace_state_with_emoji(file_name, state_name, emoji):
    with open(file_name, 'r') as file:
        map_content = file.read()

    modified_content = map_content.replace(state_name, emoji)

    with open(file_name, 'w') as file:
        file.write(modified_content)
        print(modified_content)

# File name containing the map text
file_path = 'map.txt'

# State name to replace and the emoji to use
state_to_replace = input("Where? ")
bomb_emoji = 'Yam'

# Replace the state name with the bomb emoji in the file
replace_state_with_emoji(file_path, state_to_replace, bomb_emoji)
