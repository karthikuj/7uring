#!/usr/bin/python3
colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m',
    'header':'\033[94;1m',
    'msg':'\033[33;1m[o] '
    }

banner = (colors['header'] + '''
    _________             .__                
    \______  \__ _________|__| ____    ____  
        /    /  |  \_  __ \  |/    \  / ___\ 
       /    /|  |  /|  | \/  |   |  \/ /_/  >
      /____/ |____/ |__|  |__|___|  /\___  / 
                                  \//_____/
    Not your ordinary hashcracker.
    By @5up3r541y4n (karthikuj2001@gmail.com)
'''
     )

def printBanner():
    print(banner)
#Drink all the booze, hack all the things!!
