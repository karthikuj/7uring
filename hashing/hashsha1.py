import hashlib, requests, bs4, re, os, sys

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
