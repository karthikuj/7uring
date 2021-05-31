import hashlib, requests, bs4, re, os, sys

def stringToMD5(string):

    result = hashlib.md5(string.encode()) #Create an MD5 hash object

    return result.hexdigest() #Return the required hexadecimal hash

def verifyMD5(md5):
    md5Regex = re.compile(r'^[0-9a-f]{32}$') #Create a regex object
    mo = md5Regex.search(md5.lower()) #Create a match object

    if mo == None:
        return False
    else:
        return True

def md5ToString(md5):

    if not verifyMD5(md5):
        print('Invalid hash')
        sys.exit()
    else:
        url = 'https://md5.gromweb.com/?md5=' + md5 #Create a url

        res = requests.get(url) #Query the url
        res.raise_for_status()
        
        source = res.content

        soup = bs4.BeautifulSoup(source, 'lxml') #Create a beautiful soup object

        css_path = 'html body div#page.p-1.p-3-lg div#container section#section article div#content p em.long-content.string'
        elem = soup.select(css_path)

        try:
            print(elem[0].text)
        except:
            print('Hash not found in databases')

def md5Brute(md5, wordlist):
    
    if os.path.exists(wordlist) and os.path.isfile(wordlist): #Check if the wordlist exists and if it is a file
        if not os.path.isabs(wordlist): #Check if it an absolute path
            wordlist = os.path.abspath(wordlist)
    else:
        print('Invalid path') #Exit program if invalid path
        sys.exit()

    if not verifyMD5(md5):  #Verify if hash is correct
        print('Invalid hash')
        sys.exit()

    with open(wordlist, 'r', errors='replace') as w:
        words = w.readlines()   #Store all lines in a list

    for word in words:
        md5String = stringToMD5(word.rstrip())

        if md5String == md5:    #Check if hash matches
            print('\nCracked!')
            print(md5 + ":" + word)
            break
    else:
        print("Not found")
