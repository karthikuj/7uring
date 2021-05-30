import hashlib, requests, bs4, re, os

def stringToMD5(string):

    result = hashlib.md5(string.encode()) #Create an MD5 hash object

    return result.hexdigest() #Return the required hexadecimal hash

def md5ToString(md5):
    
    md5Regex = re.compile(r'^[0-9a-f]{32}$') #Create a regex object
    mo = md5Regex.search(md5.lower()) #Create a match object

    if mo == None:
        print('Invalid hash')
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

def md5brute(md5, wordlist):
    
