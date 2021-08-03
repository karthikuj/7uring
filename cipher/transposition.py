import sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def transpositionEncrypt(text, key):
    k = list(key)
    ksort = sorted(k)
    
    perm = []
    for i in ksort:
        perm.append(k.index(i)+1)
        k[k.index(i)] = '§'
        
    message = list(text)
    for i in range(len(message)):
        
    print(perm)

transpositionEncrypt('hello', 'cooode')
