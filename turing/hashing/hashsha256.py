import os, hashlib, requests, bs4, re, sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def stringToSHA256(string):

    result = hashlib.sha256(string.encode()) #Create a SHA256 hash object

    return result.hexdigest() #Return the required hexadecimal hash

def verifySHA256(sha256):
    sha256Regex = re.compile(r'^[0-9a-f]{64}$') #Create a regex object
    mo = sha256Regex.search(sha256.lower()) #Create a match object

    if mo == None:
        return False
    else:
        return True
    
def sha256ToString(sha256):

    if not verifySHA256(sha256):
        print(colors['error'] + 'Invalid hash')
        sys.exit()
        
    else:
        URL = 'https://md5decrypt.net/en/Sha256/' #Create a url
        myobj = {
            'hash':sha256,
            'captcha65684':'',
            'ahah65684':'30beb54b674b10bf73888fda4d38893f',
            'decrypt':'Decrypt'
            }

        res = requests.post(url=URL, data=myobj) #Send a POST request
        res.raise_for_status()

        source = res.content

        soup = bs4.BeautifulSoup(source, 'lxml') #Create a beautiful soup object

        css_path = 'html body div#corps fieldset#answer b'
        elem = soup.select(css_path) #Find the required element

        try:
            print(colors['msg'] + 'Cracked!\n' + colors['success'] + sha256 + ':' + elem[0].text) #Print the cracked string
        except:
            print(colors['msg'] + 'Hash not found in databases')

def sha256Brute(sha256, wordlist):

    sha256 = sha256.lower()

    if os.path.exists(wordlist) and os.path.isfile(wordlist): #Check if the wordlist exists
        if not os.path.isabs(wordlist): #Check if it is an absolute path
            wordlist = os.path.abspath(wordlist)
    else:
        print(colors['error'] + 'Invalid path')
        sys.exit()

    if not verifySHA256(sha256): #Verify if hash is correct
        print(colors['error'] + 'Invalid hash')
        sys.exit()

    with open(wordlist, 'r', errors='replace') as w:
        words = w.readlines() #Store all words in a list

    for word in words:
        sha256String = stringToSHA256(word.rstrip())

        if sha256String == sha256: #Check if hash matches
            print(colors['msg'] + 'Cracked!')
            print(colors['success'] + sha256 + ':' + word)
            break
    else:
        print(colors['msg'] + 'Not found')
