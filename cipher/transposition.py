import sys, math

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def transpositionEncrypt(text, key):
    cipher = ''
    k = list(key)
    ksort = sorted(k)
    
    perm = []
    for i in ksort:
        perm.append(k.index(i))
        k[k.index(i)] = '§'
        
    message = []
    for i in range(math.ceil(len(text)/len(key))):
        message.append(list())
        message[i] = list(text[i*len(key):(i*len(key))+len(key)])
        if len(message[i]) < len(key):
            message[i].extend(list(' '*(len(key)-len(message[i]))))

    for i in range(len(key)):
        for j in range(math.ceil(len(text)/len(key))):
            if i == perm[i]:
                cipher += message[j][i]
            else:
                cipher += message[j][perm[i]]

    print(colors['success'] + cipher)

transpositionEncrypt('message', 'code')
