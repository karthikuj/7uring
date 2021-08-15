import hashlib, re, sys, requests, bs4, os

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }
 
def stringToMD4(string):

    result = hashlib.new('md4',string.encode('utf-8')) #Create an MD4 hash object

    return result.hexdigest() #Return the required hexadecimal hash

def verifyMD4(md4):
    md4Regex = re.compile(r'^[0-9a-f]{32}$') #Create a regex object
    mo = md4Regex.search(md4.lower()) #Create a match object

    if mo == None:
        return False
    else:
        return True

def md4ToString(md4):

    if not verifyMD4(md4):
        print(colors['error'] + 'Invalid hash')
        sys.exit()
    else:
        URL = 'https://md5decrypt.net/en/Md4/' #Create a url
        myobj = {
            'hash':md4,
            'captcha65':'',
            'ahah65':'ea1f3b6fdf11511d0a4fa2ae757132db',
            'decrypt':'Decrypt'
            }

        res = requests.post(url=URL, data=myobj) #Send a POST request
        res.raise_for_status()
        
        source = res.content

        soup = bs4.BeautifulSoup(source, 'lxml') #Create a beautiful soup object

        css_path = 'html body div#corps fieldset#answer b'
        elem = soup.select(css_path) #Find the required element

        try:
            print(colors['msg'] + 'Cracked!' + '\n' + colors['success'] + md4 + ':' + elem[0].text) #Print the cracked string
        except:
            print(colors['msg'] + 'Hash not found in databases')

def md4Brute(md4, wordlist):

    md4 = md4.lower()
    
    if os.path.exists(wordlist) and os.path.isfile(wordlist): #Check if the wordlist exists and if it is a file
        if not os.path.isabs(wordlist): #Check if it is an absolute path
            wordlist = os.path.abspath(wordlist)
    else:
        print(colors['error'] + 'Invalid path') #Exit program if invalid path
        sys.exit()

    if not verifyMD4(md4):  #Verify if hash is correct
        print(colors['error'] + 'Invalid hash')
        sys.exit()

    with open(wordlist, 'r', errors='replace') as w:
        words = w.readlines()   #Store all lines in a list

    for word in words:
        md4String = stringToMD4(word.rstrip())

        if md4String == md4:    #Check if hash matches
            print(colors['msg'] + 'Cracked!')
            print(colors['success'] + md4 + ":" + word)
            break
    else:
        print(colors['msg'] + "Not found")
