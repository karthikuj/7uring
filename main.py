from hashing.hashmd5 import *
from hashing.hashsha512 import *
from hashing.hashsha1 import *
from hashing.hashsha256 import *
from hashing.hashsha224 import *
from hashing.hashsha384 import *
from hashing.hashmd4 import *
from hashing.hashblake2b import *
from hashing.hashwhirlpool import *
from hshing.hashntlm import *
from cipher.caesar import *
from cipher.morse import *
from cipher.rot13 import *
from cipher.transposition import *
from cipher.multitapSMS import *
from cipher.bacon import *
from cipher.monoalphabetic import *
from encoder.binary import *
from encoder.octal import *

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

octalEncode('These are the nights that never die!')
octalDecode('124 150 145 163 145 40 141 162 145 40 164 150 145 40 156 151 147 150 164 163 40 164 150 141 164 40 156 145 166 145 162 40 144 151 145 41')
binaryEncode('These are the nights that never die!')
binaryDecode('1010100 1101000 1100101 1110011 1100101 100000 1100001 1110010 1100101 100000 1110100 1101000 1100101 100000 1101110 1101001 1100111 1101000 1110100 1110011 100000 1110100 1101000 1100001 1110100 100000 1101110 1100101 1110110 1100101 1110010 100000 1100100 1101001 1100101 100001')
