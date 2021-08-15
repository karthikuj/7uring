import sys

small = ['!', '"', '#', '$', '%', '&', "'", '(', ')',
         '*', '+', ',', '-', '.', '/', '0', '1', '2',
         '3', '4', '5', '6', '7', '8', '9', ':', ';',
         '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D',
         'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_',
         '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
         'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
         'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         '{', '|', '}', '~']

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def rot47Encrypt(text):
    res = ''

    for i in range(len(text)):

        if text[i] in small:
            ind = small.index(text[i]) #Find the index of character
            res += small[(ind + 47)%94] #Shift the character

        elif text[i] == ' ':
            res += ' '

        else:
            print(colors['error'] + 'Invalid characters!') #Check for invalid characters
            print(text[i])
            sys.exit()

    print(colors['success'] + res)

def rot47Decrypt(text):
    res = ''

    for i in range(len(text)):

        if text[i] in small:
            ind = small.index(text[i]) #Find the index of character
            res += small[ind - 47] #Shift the character

        elif text[i] == ' ':
            res += ' '

        else:
            print(colors['error'] + 'Invalid characters!') #Check for invalid characters
            sys.exit()

    print(colors['success'] + res)
