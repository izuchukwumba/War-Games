def print_blue(text):
    red_code = "\033[1;36m"  
    reset_code = "\033[0m" 
    print(f"{red_code}{text}{reset_code}")



usa = '''
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

soviet='''
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

padding = '\n' * 6

# Split the strings into lines
usa_lines = usa.split('\n')
soviet_lines = soviet.split('\n')

# Zip the lines together and print side by side
for usa_line, soviet_line in zip(usa_lines, soviet_lines):
    print_blue(f"{usa_line.ljust(40)}{soviet_line}")






map = '''

  ,------~~v,                                                       
 |'         Ż\   ,__/Ż||                                                            
/             \,/     /                                                         
|                    /                                                                  
\                   |                                                                   
 \                 /                                                                    
  ^Ż~_            /                                                                 
      '~~,  ,Ż~Ż\ \                                                                         
          \/     \/                                                                                                                                                 

'''
