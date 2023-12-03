def print_blue(text):
    red_code = "\033[1;36m"  
    reset_code = "\033[0m" 
    print(f"{red_code}{text}{reset_code}")
