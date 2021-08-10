from hashing.hashmd5 import *
from hashing.hashsha512 import *
from hashing.hashsha1 import *
from hashing.hashsha256 import *
from hashing.hashsha224 import *
from hashing.hashsha384 import *
from hashing.hashmd4 import *
from hashing.hashblake2b import *
from hashing.hashwhirlpool import *
from cipher.caesar import *
from cipher.morse import *
from cipher.rot13 import *
from cipher.transposition import *
from cipher.multitapSMS import *
from cipher.bacon import *
from cipher.monoalphabetic import *
from encoder.binary import *

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

binaryEncode('These are the nights that never die!')
binaryDecode('01010100 01101000 01100101 01110011 01100101 00100000 01100001 01110010 01100101 00100000 01110100 01101000 01100101 00100000 01101110 01101001 01100111 01101000 01110100 01110011 00100000 01110100 01101000 01100001 01110100 00100000 01101110 01100101 01110110 01100101 01110010 00100000 01100100 01101001 01100101 00100001')
