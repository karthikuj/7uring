import hashlib, requests, bs4, re, os, sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def stringToSHA1(string):
    
    result = hashlib.sha1(string.encode()) #Create a SHA1 hash object

    return result.hexdigest() #Return the required hexadecimal hash

def verifySHA1(sha1):
    
    sha1Regex = re.compile(r'^[a-f0-9]{40}$') #SHA-1 regex object
    mo = sha1Regex.search(sha1.lower()) #Create a match object

    if mo == None:
        return False
    else:
        return True

def sha1ToString(sha1):
    
    if not verifySHA1(sha1):
        print(colors['error'] + 'Invalid hash')
        sys.exit()
    else:
        url = 'https://sha1.gromweb.com/?hash=' + sha1 #Create url for scraping

        res = requests.get(url) #Query the url
        res.raise_for_status()

        source = res.content

        soup = bs4.BeautifulSoup(source, 'lxml') #Create a beautiful soup object

        css_path = 'html body div#page.p-1.p-3-lg div#container section#section article div#content p em.long-content.string'
        elem = soup.select(css_path)

        try:
            print(colors['msg'] + 'Cracked!\n' + colors['success'] + sha1 + ':' + elem[0].text) #Print the cracked string
        except:
            print(colors['msg'] + 'Hash not found in databases')

def sha1Brute(sha1, wordlist):

    sha1 = sha1.lower()
    
    if os.path.exists(wordlist) and os.path.isfile(wordlist): #Check if the wordlist exists and if it is a file
        if not os.path.isabs(wordlist): #Check if it is an absolute path
            wordlist = os.path.abspath(wordlist)
    else:
        print(colors['error'] + 'Invalid path')
        sys.exit()

    if not verifySHA1(sha1): #Verify if hash is correct
        print(colors['error'] + 'Invalid hash')
        sys.exit()

    with open(wordlist, 'r', errors='replace') as w:
        words = w.readlines() #Store all words in a list

    for word in words:
        sha1String = stringToSHA1(word.rstrip())

        if sha1String == sha1: #Check if hash matches
            print(colors['msg'] + 'Cracked!')
            print(colors['success'] + sha1 + ':' + word)
            break
    else:
        print(colors['msg'] + 'Not found')
