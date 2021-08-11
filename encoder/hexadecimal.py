import sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def hexadecimalEncode(text):
    res = ' '.join(format(ord(i), '08x').lstrip('0') for i in text)

    print(colors['success'] + res)

def hexadecimalDecode(hexadecimal):

    bytesObj = bytes.fromhex(hexadecimal)

    res = bytesObj.decode('ASCII')

    print(colors['success'] + res)
