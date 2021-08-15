import hashlib, requests, bs4, re, os, sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def stringToBlake2b(string):

    result = hashlib.blake2b(string.encode()) #Create a blake2b hash object

    return result.hexdigest() #Return the required hexadecimal hash

def verifyBlake2b(blake2b):
    blake2bRegex = re.compile(r'^[0-9a-f]{128}$') #Create a regex object
    mo = blake2bRegex.search(blake2b.lower()) #Create a match object

    if mo == None:
        return False
    else:
        return True

def blake2bToString(blake2b):

    if not verifyBlake2b(blake2b):
        print(colors['error'] + 'Invalid hash')
        sys.exit()

    else:
        print(colors['msg'] + 'The online "de-hashing" facility for blake2b\
 is not available yet, you can still try to bruteforce the hash using 7uring.')
        sys.exit()

def blake2bBrute(blake2b, wordlist):

    blake2b = blake2b.lower()
    
    if os.path.exists(wordlist) and os.path.isfile(wordlist): #Check if the wordlist exists
        if not os.path.isabs(wordlist): #Check if it is an absolute path
            wordlist = os.path.abspath(wordlist)
    else:
        print(colors['error'] + 'Invalid path')
        sys.exit()

    if not verifyBlake2b(blake2b): #Verify if hash is correct
        print(colors['error'] + 'Invalid hash')
        sys.exit()

    with open(wordlist, 'r', errors='replace') as w:
        words = w.readlines() #Store all words in a list

    for word in words:
        blake2bString = stringToBlake2b(word.rstrip())

        if blake2bString == blake2b: #Check if hash matches
            print(colors['msg'] + 'Cracked!')
            print(colors['success'] + blake2b + ':' + word)
            break
    else:
        print(colors['msg'] + 'Not found')
