from programFiles.menu import *
from programFiles.banner import *
import sys
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

def cliPro(argv):
    printBanner()
    print(argv)

    if '--brute' in argv and '-w' in argv and len(argv) >= 7:
        wordlist = argv[5]
        data = ' '.join(argv[6:])
        
    elif len(argv) >= 5:
        data = ' '.join(argv[4:])

    if len(argv) < 2:
        print('\n' + colors['error'] + 'No arguments specified! \
7uring --help for help menu.\n')
        sys.exit()

    elif len(argv) < 5:
        print('\n' + colors['error'] + 'All arguments not specified! \
7uring --help for help menu.\n')
        sys.exit()

    elif '--help' in argv or '-h' in argv:
        printMenu()

    elif argv[1].lower() not in subcommand:
        print(colors['error'] + 'Unrecognized subcommand.')
        sys.exit()

    elif argv[1].lower() == 'hash':
        if argv[2].lower() not in hashes:
            print(colors['error'] + 'Unrecognized hash type.')
            sys.exit()

        elif argv[3].lower() not in options:
            print(colors['error'] + 'Unrecognized option ' + '\'' + argv[3] + '\'')
            sys.exit()

        elif argv[2].lower() == '--md5':
            if argv[3] == '--enc':
                print(colors['success'] + stringToMD5(data))

            elif argv[3] == '--dec':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for hashes. Use --rainbow or --brute\
 instead.')
                sys.exit()

            elif argv[3] == '--rainbow':
                md5ToString(data)

            else:
                md5Brute(data, wordlist)
