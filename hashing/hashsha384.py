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
