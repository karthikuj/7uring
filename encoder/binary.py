import sys, re

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0

    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1

    return decimal

def binaryEncode(text):
    res = ' '.join(format(ord(i), '08b').lstrip('0') for i in text)

    print(colors['success'] + res)

def verifyBinary(binary):
    binaryRegex = re.compile(r'^(0|1|\s)+$') #Create a regex object
    mo = binaryRegex.search(binary) #Create a match object

    if mo == None:
        return False
    else:
        return True

def binaryDecode(binary):

    res = ''
    
    if ' ' in binary:
        binList = binary.split()

    for i in binList:
        decimal = binaryToDecimal(int(i))

        res += chr(decimal)

    print(colors['success'] + res)
