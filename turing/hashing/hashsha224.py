import os, re, sys, hashlib

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def stringToSHA224(string):

    result = hashlib.sha224(string.encode()) #Create a sha224 hash object

    return result.hexdigest() #Return the required hexadecimal hash

def verifySHA224(sha224):
    sha224Regex = re.compile(r'^[0-9a-f]{56}$') #Create a regex object
    mo = sha224Regex.search(sha224.lower()) #Create a match object

    if mo == None:
        return False
    else:
        return True

def sha224ToString(sha224):
    print(colors['msg'] + 'The online "de-hashing" facility for sha224\
 is not available yet, you can still try to bruteforce the hash using 7uring.')
    sys.exit()

def sha224Brute(sha224, wordlist):

    sha224 = sha224.lower()

    if os.path.exists(wordlist) and os.path.isfile(wordlist): #Check if wordlist exists
        if not os.path.isabs(wordlist): #Check if it is an absolute path
            wordlist = os.path.abspath(wordlist)
    else:
        print(colors['error'] + 'Invalid path')
        sys.exit()

    if not verifySHA224(sha224): #Verify if hash is correct
        print(colors['error'] + 'Invalid hash')
        sys.exit()

    with open(wordlist, 'r', errors='replace') as w:
        words = w.readlines() #Store all words in a list

    for word in words:
        sha224String = stringToSHA224(word.rstrip())

        if sha224String == sha224: #Check if hash matches
            print(colors['msg'] + 'Cracked!')
            print(colors['success'] + sha224 + ':' + word)
            break
    else:
        print(colors['msg'] + 'Not found')
