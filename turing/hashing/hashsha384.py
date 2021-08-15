import hashlib, requests, bs4, re, os, sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def stringToSHA384(string):
    
    result = hashlib.sha384(string.encode()) #Create a SHA384 object

    return result.hexdigest() #Return the required hexadecimal hash

def verifySHA384(sha384):
    sha384Regex = re.compile(r'^[0-9a-f]{96}$') #Create a regex object
    mo = sha384Regex.search(sha384.lower()) #Create a match object

    if mo == None:
        return False
    else:
        return True
    
def sha384ToString(sha384):

    sha384 = sha384.lower()

    if not verifySHA384(sha384):
        print(colors['error'] + 'Invalid hash')
        sys.exit()
    else:
        
        URL = 'https://md5decrypt.net/en/Sha384/' #Create a url
        myobj = {
            'hash':sha384,
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
            print(colors['msg'] + 'Cracked!\n' + colors['success'] + sha384 + ':' + elem[0].text) #Print the cracked string
        except:
            print(colors['msg'] + 'Hash not found in databases')

def sha384Brute(sha384, wordlist):

    if os.path.exists(wordlist) and os.path.isfile(wordlist): #Check if the wordlist exists and if it is a file
        if not os.path.isabs(wordlist): #Check if it is an absolute path
            wordlist = os.path.abspath(wordlist)
    else:
        print(colors['error'] + 'Invalid path') #Exit program if invalid path
        sys.exit()

    if not verifySHA384(sha384): #Verify if hash is correct
        print(colors['error'] + 'Invalid hash')
        sys.exit()

    with open(wordlist, 'r', errors='replace') as w:
        words = w.readlines() #Store all lines in a list

    for word in words:
        sha384String = stringToSHA384(word.rstrip())

        if sha384String == sha384: #Check if hash matches
            print(colors['msg'] + 'Cracked!')
            print(colors['success'] + sha384 + ':' + word)
            break
    else:
        print(colors['msg'] + 'Not found')
