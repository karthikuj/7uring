import hashlib, re, sys, requests, bs4, os

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }
 
def stringToWhirlpool(string):

    result = hashlib.new('whirlpool', string.encode('utf-8')) #Create a whirlpool hash object

    return result.hexdigest() #Return the required hexadecimal hash

def verifyWhirlpool(whirlpool):
    whirlpoolRegex = re.compile(r'^[0-9a-f]{128}$') #Create a regex object
    mo = whirlpoolRegex.search(whirlpool.lower()) #Create a match object

    if mo == None:
        return False
    else:
        return True

def whirlpoolToString(whirlpool):

    if not verifyWhirlpool(whirlpool):
        print(colors['error'] + 'Invalid hash')
        sys.exit()

    else:
        print(colors['msg'] + 'The online "de-hashing" facility for whirlpool\
 is not available yet, you can still try to bruteforce the hash using 7uring.')
        sys.exit()


def whirlpoolBrute(whirlpool, wordlist):

    whirlpool = whirlpool.lower()

    if os.path.exists(wordlist) and os.path.isfile(wordlist): #Check if the wordlist exists
        if not os.path.isabs(wordlist): #Check if it is an absolute path
            wordlist = os.path.abspath(wordlist)
    else:
        print(colors['error'] + 'Invalid path') #Exit program if invalid path
        sys.exit()

    if not verifyWhirlpool(whirlpool): #Verify if hash is correct
        print(colors['error'] + 'Invalid path') #Exit program if invalid path
        sys.exit()

    with open(wordlist, 'r', errors='replace') as w:
        words = w.readlines() #Store all lines in a list

    for word in words:
        whirlpoolString = stringToWhirlpool(word.rstrip())

        if whirlpoolString == whirlpool: #Check if hash matches
            print(colors['msg'] + 'Cracked!')
            print(colors['success'] + whirlpool + ':' + word)
            break
    else:
        print(colors['msg'] + 'Not found')
