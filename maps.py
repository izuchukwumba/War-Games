us_map = '''
       ,__                                                  _,
    \~\|  ~~---___              ,                          | \\
     | Wash.| |   ~~~~~~~|~~~~~| ~~---,   _            VT_/,ME>
    /~-_--__| |  Montana |N Dak\ Minn/ ~\~_/Mich.     /~| ||,'
    |Oregon |  \         |------|   { WI / /~)     __-NY',|_\\,NH
   /       |Ida.|~~~~~~~~|S Dak.\    \\   | | '~\\  |_____,|~,-'Mass.
   |~~--__ |    | Wyoming|____  |~~~~~|--| |__ /_-'Penn.{,~Conn (RI)
   |   |  ~~~|~~|        |    ~~\\ Iowa/  `-' |`~ |~_____{/NJ
   |   | Nev |  '---------, Nebr.\\----|   |IN|OH,' ~/~\\,|`MD (DE)
   ',  \     |Utah| Colo. |~~~~~~~|    \\IL| ,'~~\\WV/ VA |
    |Cal\\    |    |       | Kansas| MO  \\_-~ KY /`~___--\\
    ',   \\  ,-----|-------+-------'_____/__----~~/N Car./
     '_   '\\|     |      |~~~|Okla.|    | Tenn._/-,~~-,/
       \\    |Ariz.| New  |   |_    |Ark./~~|~~\\    \\,/S Car.
        ~~~-'     | Mex. |     `~~~\\___|MS |AL | GA /
            '-,_  | _____|          |  /   | ,-~---~\\
                `~'~  \\    Texas    |LA`--,~~~~-~~,FL\\
                       \\/~\\      /~~~`---`         |  \\
                           \\    /                   \\  | 
                            \\  |                     '\\'
                             `~'
'''

def print_blue(text):
    red_code = "\033[1;36m"  
    reset_code = "\033[0m" 
    print(f"{red_code}{text}{reset_code}")

print_blue(us_map)
