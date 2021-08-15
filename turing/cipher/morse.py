import sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

keyList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
           ',', '.', '?', ':', '-', '"', '(', '=', '/', "'", '_', ')', '+', '@']

valList = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
           '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
           '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----',
           '..---', '...--', '....-', '.....', '-....', '--...', '---..',
           '----.', '-----', '--..--', '.-.-.-', '..--..', '---...', '-...-',
           '.-..-.', '-.--.', '-...-', '-..-.', '.---.', '..--.-', '-.--.-',
           '.-.-.', '.--.-.']

def morseEncrypt(text):
    res = ''

    for i in text:

        if i == ' ':
            res += ' '
        
        elif i.isupper():
            res += valList[keyList.index(i.lower())] + ' '

        else:
            try:
                res += valList[keyList.index(i)] + ' '
            except:
                print(colors['error'] + 'Invalid characters found! (' + i + ')')
                sys.exit()

    print(colors['success'] + res)

def morseDecrypt(morse):
    res = ''

    words = morse.split('  ')

    for i in words:
        
        chars = i.split()
        for j in chars:
            try:
                res += keyList[valList.index(j)]
            except:
                print(colors['error'] + 'Invalid morse code!')
                print(j)
                sys.exit()

        res += ' '

    print(colors['success'] + res)
