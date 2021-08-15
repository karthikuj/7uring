import sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

code = ['l', 'd', 'm', 'g', 'b', 'v', 's', 'u', 'x', 'i', 't', 'q', 'r',
        'z', 'c', 'y', 'w', 'a', 'j', 'f', 'h', 'e', 'o', 'k', 'n', 'p']

def monoalphabeticEncrypt(text):
    cipher = ''

    for i in text:
        if i in char:
            cipher += code[char.index(i)] #Find and join correct code
        else:
            cipher += i

    print(colors['success'] + cipher)

def monoalphabeticDecrypt(cipher):
    print('\n' + colors['msg'] + 'Monoalphabetic cipher uses mixed sequence of alphabets \
for encryption, so the message encrypted using other tool cannot be decrypted by \
7uring using it\'s default alphabet sequence.\n')
    decipher = ''

    for i in cipher:
        if i in code:
            decipher += char[code.index(i)] #Find and join correct character
        else:
            decipher += i

    print(colors['success'] + decipher)
