from hashing.hashmd5 import *
from hashing.hashsha512 import *
from hashing.hashsha1 import *
from hashing.hashsha256 import *
from hashing.hashsha224 import *
from hashing.hashsha384 import *
from hashing.hashmd4 import *
from hashing.hashblake2b import *
from hashing.hashwhirlpool import *
from hashing.hashntlm import *
from cipher.caesar import *
from cipher.morse import *
from cipher.rot13 import *
from cipher.transposition import *
from cipher.multitapSMS import *
from cipher.bacon import *
from cipher.monoalphabetic import *
from cipher.rot47 import *
from encoder.binary import *
from encoder.octal import *
from encoder.hexadecimal import *
from encoder.base64 import *

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m',
    'header':'\033[94;1m',
    'msg':'\033[33;1m[o] '
    }

print(colors['header'] + '''
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

rot47Encrypt('karthik123@|}~')
rot47Decrypt('<2CE9:<`aboMNO')


