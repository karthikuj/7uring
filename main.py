from hashing.hashmd5 import *
from hashing.hashsha1 import *
from hashing.hashsha256 import *
from hashing.hashsha224 import *
from hashing.hashsha384 import *
from cipher.caesar import *

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m',
    'orange':'\033[33m',
    'msg':'\033[33;1m[o] '
    }

print(colors['orange'] + '''
    _________             .__                
    \______  \__ _________|__| ____    ____  
        /    /  |  \_  __ \  |/    \  / ___\ 
       /    /|  |  /|  | \/  |   |  \/ /_/  >
      /____/ |____/ |__|  |__|___|  /\___  / 
                                  \//_____/
    Drink all the booze, hack all the things!!
    By @5up3r541y4n (karthikuj2001@gmail.com)
'''
     )

caesarEncrypt('Ambarsariya', 5)
caesarDecrypt('Ftqk emk', 12)
caesarBrute('Ftqk emk uf ue itmf kag ymwq U emk uf ue gbfa rmfq')
