import os, hashlib, requests, bs4, re, sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def stringToNTLM(string):

    result = hashlib.new('md4', string.encode('utf-16le'))

    return result.hexdigest()

def verifyNTLM(ntlm):
    ntlmRegex = re.compile(r'^[0-9a-f]{32}$') #Create a regex object
    mo = ntlmRegex.search(ntlm.lower()) #Create a match object

    if mo == None:
        return False
    else:
        return True

def ntlmToString(ntlm):

    if not verifyNTLM(ntlm):
        print(colors['error'] + 'Invalid hash')
        sys.exit()

    else:
        print(colors['msg'] + 'The online "de-hashing" facility for NTLM\
 is not available yet, you can still try to bruteforce the hash using 7uring.')
    sys.exit()

def ntlmBrute(ntlm, wordlist):

    ntlm = ntlm.lower()

    if os.path.exists(wordlist) and os.path.isfile(wordlist): #Check if the wordlist exists
        if not os.path.isabs(wordlist): #Check if it is an absolute path
            wordlist = os.path.abspath(wordlist)
    else:
        print(colors['error'] + 'Invalid path')
        sys.exit()

    if not verifyNTLM(ntlm): #Verify if hash is correct
        print(colors['error'] + 'Invalid hash')
        sys.exit()

    with open(wordlist, 'r', errors='replace') as w:
        words = w.readlines() #Store all words in a list

    for word in words:
        ntlmString = stringToNTLM(word.rstrip())

        if ntlmString == ntlm: #Check if hash matches
            print(colors['msg'] + 'Cracked!')
            print(colors['success'] + ntlm + ':' + word)
            break

    else:
        print(colors['msg'] + 'Not found')
