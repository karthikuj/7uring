import sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def octalToDecimal(octal):
    octal1 = octal
    decimal, base, temp = 0, 1, octal1

    while(temp):
        lastDigit = temp % 10
        temp = int(temp / 10)
        decimal += lastDigit * base
        base *= 8

    return decimal

def octalEncode(text):
    res = ' '.join(format(ord(i), '08o').lstrip('0') for i in text)

    print(colors['success'] + res)

def octalDecode(octal):

    res = ''
    
    if ' ' in octal:
        octList = octal.split()

    for i in octList:
        decimal = octalToDecimal(int(i))

        res += chr(decimal)

    print(colors['success'] + res)
