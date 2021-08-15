#!/usr/bin/python3
from turing.programfiles.menu import *
from turing.programfiles.banner import *
import sys
from turing.hashing.hashmd5 import *
from turing.hashing.hashsha512 import *
from turing.hashing.hashsha1 import *
from turing.hashing.hashsha256 import *
from turing.hashing.hashsha224 import *
from turing.hashing.hashsha384 import *
from turing.hashing.hashmd4 import *
from turing.hashing.hashblake2b import *
from turing.hashing.hashwhirlpool import *
from turing.hashing.hashntlm import *
from turing.cipher.caesar import *
from turing.cipher.morse import *
from turing.cipher.rot13 import *
from turing.cipher.transposition import *
from turing.cipher.multitapSMS import *
from turing.cipher.bacon import *
from turing.cipher.monoalphabetic import *
from turing.cipher.rot47 import *
from turing.encoder.binary import *
from turing.encoder.octal import *
from turing.encoder.hexadecimal import *
from turing.encoder.base64 import *

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'header':'\033[94;1m',
    'msg':'\033[33;1m[o] '
    }

def cliPro(argv):
    printBanner()

    if 'hash' in argv and '--brute' in argv and '-w' not in argv:
        print('\n' + colors['error'] + 'Wordlist (-w) not specified')
        sys.exit()

    if 'hash' in argv and '--brute' in argv and '-w' in argv and len(argv) < 7:
        print('\n' + colors['error'] + 'All arguments not specified! \
7uring --help for help menu.\n')
        sys.exit()

    if '--brute' in argv and '-w' in argv and len(argv) >= 7:
        wordlist = argv[5]
        data = ' '.join(argv[6:])
        
    elif len(argv) >= 5:
        data = ' '.join(argv[4:])

    if len(argv) < 2:
        print('\n' + colors['error'] + 'No arguments specified! \
7uring --help for help menu.\n')
        sys.exit()

    elif '--help' in argv or '-h' in argv:
        printMenu()

    elif len(argv) < 5:
        print('\n' + colors['error'] + 'All arguments not specified! \
7uring --help for help menu.\n')
        sys.exit()

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

        elif argv[2].lower() == '--blake2b':
            if argv[3] == '--enc':
                print(colors['success'] + stringToBlake2b(data))

            elif argv[3] == '--dec':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for hashes. Use --rainbow or --brute\
 instead.')
                sys.exit()

            elif argv[3] == '--rainbow':
                blake2bToString(data)

            else:
                blake2bBrute(data, wordlist)

        elif argv[2].lower() == '--md4':
            if argv[3] == '--enc':
                print(colors['success'] + stringToMD4(data))

            elif argv[3] == '--dec':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for hashes. Use --rainbow or --brute\
 instead.')
                sys.exit()

            elif argv[3] == '--rainbow':
                md4ToString(data)

            else:
                md4Brute(data, wordlist)

        elif argv[2].lower() == '--ntlm':
            if argv[3] == '--enc':
                print(colors['success'] + stringToNTLM(data))

            elif argv[3] == '--dec':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for hashes. Use --rainbow or --brute\
 instead.')
                sys.exit()

            elif argv[3] == '--rainbow':
                ntlmToString(data)

            else:
                ntlmBrute(data, wordlist)

        elif argv[2].lower() == '--sha1':
            if argv[3] == '--enc':
                print(colors['success'] + stringToSHA1(data))

            elif argv[3] == '--dec':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for hashes. Use --rainbow or --brute\
 instead.')
                sys.exit()

            elif argv[3] == '--rainbow':
                sha1ToString(data)

            else:
                sha1Brute(data, wordlist)

        elif argv[2].lower() == '--sha224':
            if argv[3] == '--enc':
                print(colors['success'] + stringToSHA224(data))

            elif argv[3] == '--dec':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for hashes. Use --rainbow or --brute\
 instead.')
                sys.exit()

            elif argv[3] == '--rainbow':
                sha224ToString(data)

            else:
                sha224Brute(data, wordlist)

        elif argv[2].lower() == '--sha256':
            if argv[3] == '--enc':
                print(colors['success'] + stringToSHA256(data))

            elif argv[3] == '--dec':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for hashes. Use --rainbow or --brute\
 instead.')
                sys.exit()

            elif argv[3] == '--rainbow':
                sha256ToString(data)

            else:
                sha256Brute(data, wordlist)

        elif argv[2].lower() == '--sha384':
            if argv[3] == '--enc':
                print(colors['success'] + stringToSHA384(data))

            elif argv[3] == '--dec':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for hashes. Use --rainbow or --brute\
 instead.')
                sys.exit()

            elif argv[3] == '--rainbow':
                sha384ToString(data)

            else:
                sha384Brute(data, wordlist)

        elif argv[2].lower() == '--sha512':
            if argv[3] == '--enc':
                print(colors['success'] + stringToSHA512(data))

            elif argv[3] == '--dec':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for hashes. Use --rainbow or --brute\
 instead.')
                sys.exit()

            elif argv[3] == '--rainbow':
                sha512ToString(data)

            else:
                sha512Brute(data, wordlist)

        elif argv[2].lower() == '--whirlpool':
            if argv[3] == '--enc':
                print(colors['success'] + stringToWhirlpool(data))

            elif argv[3] == '--dec':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for hashes. Use --rainbow or --brute\
 instead.')
                sys.exit()

            elif argv[3] == '--rainbow':
                whirlpoolToString(data)

            else:
                whirlpoolBrute(data, wordlist)

    elif argv[1].lower() == 'cipher':
        if argv[2].lower() not in ciphers:
            print(colors['error'] + 'Unrecognized cipher type.')
            sys.exit()

        elif argv[3].lower() not in options:
            print(colors['error'] + 'Unrecognized option ' + '\'' + argv[3] + '\'')
            sys.exit()

        elif argv[2].lower() == '--bacon':
            if argv[3] == '--enc':
                baconEncrypt(data)

            elif argv[3] == '--dec':
                baconDecrypt(data)

            elif argv[3] == '--rainbow':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for ciphers. Use --enc or --dec\
 instead.')
                sys.exit()

            else:
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for ciphers(except caesar). Use --enc or --dec\
 instead.')
                sys.exit()

        elif argv[2].lower() == '--caesar':
            
            if argv[3] == '--enc':
                shift = int(input(colors['msg'] + 'Enter shift value: '))
                caesarEncrypt(data, shift)

            elif argv[3] == '--dec':
                shift = int(input(colors['msg'] + 'Enter shift value: '))
                caesarDecrypt(data, shift)

            elif argv[3] == '--rainbow':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for ciphers. Use --enc or --dec\
 instead.')
                sys.exit()

            else:
                caesarBrute(data)
                sys.exit()

        elif argv[2].lower() == '--monoalphabetic':
            if argv[3] == '--enc':
                monoalphabeticEncrypt(data)

            elif argv[3] == '--dec':
                monoalphabeticDecrypt(data)

            elif argv[3] == '--rainbow':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for ciphers. Use --enc or --dec\
 instead.')
                sys.exit()

            else:
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for ciphers(except caesar). Use --enc or --dec\
 instead.')
                sys.exit()

        elif argv[2].lower() == '--morse':
            if argv[3] == '--enc':
                morseEncrypt(data)

            elif argv[3] == '--dec':
                morseDecrypt(data)

            elif argv[3] == '--rainbow':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for ciphers. Use --enc or --dec\
 instead.')
                sys.exit()

            else:
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for ciphers(except caesar). Use --enc or --dec\
 instead.')
                sys.exit()

        elif argv[2].lower() == '--multitapsms':
            if argv[3] == '--enc':
                multitapEncrypt(data)

            elif argv[3] == '--dec':
                multitapDecrypt(data)

            elif argv[3] == '--rainbow':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for ciphers. Use --enc or --dec\
 instead.')
                sys.exit()

            else:
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for ciphers(except caesar). Use --enc or --dec\
 instead.')
                sys.exit()

        elif argv[2].lower() == '--rot13':
            if argv[3] == '--enc':
                rot13Encrypt(data)

            elif argv[3] == '--dec':
                rot13Decrypt(data)

            elif argv[3] == '--rainbow':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for ciphers. Use --enc or --dec\
 instead.')
                sys.exit()

            else:
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for ciphers(except caesar). Use --enc or --dec\
 instead.')
                sys.exit()

        elif argv[2].lower() == '--rot47':
            if argv[3] == '--enc':
                rot47Encrypt(data)

            elif argv[3] == '--dec':
                rot47Decrypt(data)

            elif argv[3] == '--rainbow':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for ciphers. Use --enc or --dec\
 instead.')
                sys.exit()

            else:
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for ciphers(except caesar). Use --enc or --dec\
 instead.')
                sys.exit()

        elif argv[2].lower() == '--transposition':
            if argv[3] == '--enc':
                key = input(colors['msg'] + 'Enter key value: ')
                transpositionEncrypt(data, key)

            elif argv[3] == '--dec':
                key = input(colors['msg'] + 'Enter key value: ')
                transpositionDecrypt(data, key)

            elif argv[3] == '--rainbow':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for ciphers. Use --enc or --dec\
 instead.')
                sys.exit()

            else:
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for ciphers(except caesar). Use --enc or --dec\
 instead.')
                sys.exit()

    elif argv[1].lower() == 'encoder':
        if argv[2].lower() not in encoders:
            print(colors['error'] + 'Unrecognized encoding type.')
            sys.exit()

        elif argv[3].lower() not in options:
            print(colors['error'] + 'Unrecognized option ' + '\'' + argv[3] + '\'')
            sys.exit()

        elif argv[2].lower() == '--binary':
            if argv[3] == '--enc':
                binaryEncode(data)

            elif argv[3] == '--dec':
                binaryDecode(data)

            elif argv[3] == '--rainbow':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for encoders. Use --enc or --dec\
 instead.')
                sys.exit()

            else:
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for encoders. Use --enc or --dec\
 instead.')
                sys.exit()

        elif argv[2].lower() == '--octal':
            if argv[3] == '--enc':
                octalEncode(data)

            elif argv[3] == '--dec':
                octalDecode(data)

            elif argv[3] == '--rainbow':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for encoders. Use --enc or --dec\
 instead.')
                sys.exit()

            else:
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for encoders. Use --enc or --dec\
 instead.')
                sys.exit()

        elif argv[2].lower() == '--hexadecimal':
            if argv[3] == '--enc':
                hexadecimalEncode(data)

            elif argv[3] == '--dec':
                hexadecimalDecode(data)

            elif argv[3] == '--rainbow':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for encoders. Use --enc or --dec\
 instead.')
                sys.exit()

            else:
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for encoders. Use --enc or --dec\
 instead.')
                sys.exit()

        elif argv[2].lower() == '--base64':
            if argv[3] == '--enc':
                base64Encode(data)

            elif argv[3] == '--dec':
                base64Decode(data)

            elif argv[3] == '--rainbow':
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for encoders. Use --enc or --dec\
 instead.')
                sys.exit()

            else:
                print(colors['error'] + '\'' + argv[3] + '\'' +
                      ', this option is not for encoders. Use --enc or --dec\
 instead.')
                sys.exit()
