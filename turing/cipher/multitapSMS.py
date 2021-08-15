import sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
         'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
         's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

codes = ['2', '22', '222', '3', '33', '333', '4', '44', '444',
         '5', '55', '555', '6', '66', '666', '7', '77', '777',
         '7777', '8', '88', '888', '9', '99', '999', '9999', '0']

def multitapEncrypt(text):
    for i in text:
        if not i.isalpha() and not i.isspace(): #Check if characters are valid
            print(colors['error'] + 'Only english alphabets and\
whitespaces allowed!')
            sys.exit()
            
    cipher = ''
    
    for i in text:
        cipher += codes[chars.index(i.lower())] #Find and join codes
        cipher += ' '

    print(colors['success'] + cipher) #Print the result

def multitapDecrypt(cipher):
    for i in cipher:
        if not i.isdigit() and not i.isspace(): #Check if cipher is valid
            print(colors['error'] + 'Only digits and whitespaces allowed!')
            sys.exit()

    decipher = ''

    for i in cipher.split():
        if not i == ' ':
            try:
                decipher += chars[codes.index(i)] #Find and join characters
            except:
                print(colors['error'] + 'Invalid code')
                sys.exit()

    print(colors['success'] + decipher) #Print the result
