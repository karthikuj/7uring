import os, re, sys, bs4, requests, hashlib

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
    pass
    '''if not verifySHA224(sha224):
        print(colors['error'] + 'Invalid hash')
        sys.exit()
    else:
        url = '''
