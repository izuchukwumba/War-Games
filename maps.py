from print_blue import print_blue

def thermo_nuclear_war():
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

    
    


