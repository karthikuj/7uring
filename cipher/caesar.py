import sys

small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def caesarEncrypt(text, shift):
    res = ''

    for i in range(len(text)):

        if text[i].isupper():
            ind = small.index(text[i].upper()) #Find the index of character
            res += small[(ind + shift)%26].upper() #Shift the character
            
        elif text[i].islower():
            ind = small.index(text[i]) #Find the index of character
            res += small[(ind + shift)%26] #Shift the character

        elif text[i] == ' ':
            res += ' '

        else:
            print(colors['error'] + 'Invalid characters!') #Check for invalid characters
            sys.exit()
            
    print(colors['success'] + text + ' : ' + res)

def caesarDecrypt(text, shift):
    res = ''

    for i in range(len(text)):

        if text[i].isupper():
            ind = small.index(text[i].upper()) #Find the index of character
            res += small[ind - shift].upper() #Shift the character

        elif text[i].islower():
            ind = small.index(text[i]) #Find the index of character
            res += small[ind - shift] #Shift the character

        elif text[i] == ' ':
            res += ' '

        else:
            print(colors['error'] + 'Invalid characters!') #Check for invalid characters
            sys.exit()

    print(colors['success'] + text + ' : ' + res)

def caesarBrute(text):

    for shift in range(26):
        res = ''

        for i in range(len(text)):

            if text[i].isupper():
                ind = small.index(text[i].upper()) #Find the index of character
                res += small[ind - shift].upper() #Shift the character

            elif text[i].islower():
                ind = small.index(text[i]) #Find the index of character
                res += small[ind - shift] #Shift the character

            elif text[i] == ' ':
                res += ' '

            else:
                print(colors['error'] + 'Invalid characters!') #Check for invalid characters
                sys.exit()

        print(colors['success'] + 'shift(' + "{:02d}".format(shift) +
              ')' + ' : ' + res)
