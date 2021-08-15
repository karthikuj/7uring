import hashlib, requests, bs4, re, os, sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def stringToSHA512(string):

    result = hashlib.sha512(string.encode()) #Create a SHA512 hash object

    return result.hexdigest() #Return the required hexadecimal hash

def verifySHA512(sha512):
    sha512Regex = re.compile(r'^[0-9a-f]{128}$') #Create a regex object
    mo = sha512Regex.search(sha512) #Create a match object

    if mo == None:
        return False
    else:
        return True

def sha512ToString(sha512):

    sha512 = sha512.lower()

    if not verifySHA512(sha512):
        print(colors['error'] + 'Invalid hash')
        sys.exit()
    else:

        URL='https://md5decrypt.net/en/Sha512/' #Create a url
        myobj = {
            'hash':sha512,
            'captcha13126':'',
            'ahah13126':'8239e6d5b8e2f67f34cfbd3c77b05523',
            'decrypt':'Decrypt'
            }

        res = requests.post(url=URL, data=myobj) #Send a POST request
        res.raise_for_status()

        source = res.content

        soup = bs4.BeautifulSoup(source, 'lxml') #Create a beautiful soup bject

        css_path = 'html body div#corps fieldset#answer b'
        elem = soup.select(css_path) #Find the required element

        try:
            print(colors['msg'] + 'Cracked!\n' + colors['success'] + sha512 + ':' + elem[0].text) #Print the cracked string
        except:
            print(colors['msg'] + 'Hash not found in databases')

def sha512Brute(sha512, wordlist):

    if os.path.exists(wordlist) and os.path.isfile(wordlist): #Check if the wordlist exists
        if not os.path.isabs(wordlist): #Check if it is an absolute path
            wordlist = os.path.abspath(wordlist)
    else:
        print(colors['error'] + 'Invalid path')
        sys.exit()

    if not verifySHA512(sha512): #Verify if hash is correct
        print(colors['error'] + 'Invalid hash')
        sys.exit()

    with open(wordlist, 'r', errors='replace') as w:
        words = w.readlines() #Store all words in a list

    for word in words:
        sha512String = stringToSHA512(word.rstrip())

        if sha512String == sha512: #Check if hash matches
            print(colors['msg'] + 'Cracked!')
            print(colors['success'] + sha512 + ':' + word)
            break
    else:
        print(colors['msg'] + 'Not found')
