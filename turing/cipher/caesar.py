import sys, enchant

small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def caesarEncrypt(text, shift):
    res = ''

    if shift < 0 or shift > 25:
        print(colors['error'] + 'Shift value should be 0-25') #Shift value check

    for i in range(len(text)):

        if text[i].isupper():
            ind = small.index(text[i].lower()) #Find the index of character
            res += small[(ind + shift)%26].upper() #Shift the character
            
        elif text[i].islower():
            ind = small.index(text[i]) #Find the index of character
            res += small[(ind + shift)%26] #Shift the character

        elif text[i] == ' ':
            res += ' '

        else:
            print(colors['error'] + 'Invalid characters!') #Check for invalid characters
            sys.exit()
            
    print(colors['success'] + res)

def caesarDecrypt(text, shift):
    res = ''

    if shift < 0 or shift > 25:
        print(colors['error'] + 'Shift value should be 0-25') #Shift value check

    for i in range(len(text)):

        if text[i].isupper():
            ind = small.index(text[i].lower()) #Find the index of character
            res += small[ind - shift].upper() #Shift the character

        elif text[i].islower():
            ind = small.index(text[i]) #Find the index of character
            res += small[ind - shift] #Shift the character

        elif text[i] == ' ':
            res += ' '

        else:
            print(colors['error'] + 'Invalid characters!') #Check for invalid characters
            sys.exit()

    print(colors['success'] + res)

def caesarBrute(text):

    possible = set()
    
    for shift in range(26):
        res = ''

        for i in range(len(text)):

            if text[i].isupper():
                ind = small.index(text[i].lower()) #Find the index of character
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

        dic = enchant.Dict('en_US') #Create a US english Dictionary
        
        for j in res.split():
            if len(j) > 2 and dic.check(j): #Check for english words
                possible.add('shift(' + "{:02d}".format(shift) +
                             ')' + ' : ' + res)
                
    if len(possible) > 0:
        print(colors['success'][:-4] + '\nMost possible solutions:') #Print most possible solutions
        for k in possible:
            print(colors['success'] + k)
