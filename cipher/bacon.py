import sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

chars = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

codes = [
    'AAAAA', 'AAAAB', 'AAABA', 'AAABB', 'AABAA', 'AABAB', 'AABBA', 'AABBB', 
    'ABAAA', 'ABAAA', 'ABAAB', 'ABABA', 'ABABB', 'ABBAA', 'ABBAB', 'ABBBA',
    'ABBBB', 'BAAAA', 'BAAAB', 'BAABA', 'BAABB', 'BAABB', 'BABAA', 'BABAB',
    'BABBA', 'BABBB'
    ]

def baconEncrypt(text):
    for i in text:
        if not i.isalpha() and not i.isspace(): #Check if characters are valids
            print(colors['error'] + 'Only english alphabets and \
whitespaces allowed!')
            sys.exit()
            
    cipher = ''
    for i in text:
        if i == ' ':
            cipher += ' '
        else:
            cipher += codes[chars.index(i.lower())] #Find and join the codes

    print(colors['success'] + cipher) #Print the result

def baconDecrypt(cipher):
    '''for i in cipher:
        if (not i.lower() == 'a' or not i.lower() == 'b') and not i.isspace():
            print(colors['error'] + 'Only works with bacon cipher of \'A\' \
and \'B\' as of now')
            sys.exit()'''

    decipher = ''
    i = 0
    while i < len(cipher):
        if cipher[i] == ' ':
            decipher += ' '
            i += 1
        else:
            decipher += chars[codes.index(cipher[i:i+5])]
            i += 5

    print(colors['success'] + decipher)
