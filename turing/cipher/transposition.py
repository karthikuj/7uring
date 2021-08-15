import sys, math

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def transpositionEncrypt(text, key):
    textl = list(text)
    
    if ' ' in textl:
        for i in range(textl.count(' ')):
            textl.remove(' ')

    text = ''.join(textl)
    
    cipher = ''
    k = list(key)
    ksort = sorted(k)
    
    perm = []
    for i in k:
        perm.append(ksort.index(i))
        ksort[ksort.index(i)] = '§'
        
    message = []
    for i in range(math.ceil(len(text)/len(key))): #Create matrix
        message.append(list())
        message[i] = list(text[i*len(key):(i*len(key))+len(key)])
        if len(message[i]) < len(key):
            message[i].extend(list(' '*(len(key)-len(message[i]))))

    for i in range(len(key)):
        for j in range(math.ceil(len(text)/len(key))):
            if i == perm[i]:
                cipher += message[j][i]
            else:
                cipher += message[j][perm.index(i)]

    print(colors['success'] + cipher)

def transpositionDecrypt(text, key):
    decipher = ''
    k = list(key)
    ksort = sorted(k)
    
    perm = []
    for i in k:
        perm.append(ksort.index(i))
        ksort[ksort.index(i)] = '§'

    #permNew = list(range(len(key)))
        
    message = []
    for i in range(math.ceil(len(text)/len(key))):
        message.append(list())
        message[i].extend(list(' '*len(key)))

    c = 0
    for i in range(len(key)):
        for j in range(math.ceil(len(text)/len(key))):
            try:
                message[j][i] = text[c]
            except:
                message[j][i] = ' '

            c += 1

    for i in range(math.ceil(len(text)/len(key))):
        for j in range(len(key)):
            if j == perm[j]:
                decipher += message[i][j]
            else:
                decipher += message[i][perm[j]]

    print(colors['success'] + decipher)
