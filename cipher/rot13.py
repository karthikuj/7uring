from . import caesar

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def rot13Encrypt(text):
    caesar.caesarEncrypt(text, 13)

def rot13Decrypt(text):
    caesar.caesarDecrypt(text, 13)
