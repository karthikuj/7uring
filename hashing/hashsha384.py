import hashlib, requests, bs4, re, os, sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def stringToSHA384(string):
    
    result = hashlib.sha384(string.encode()) #Create a SHA384 object

    return result.hexdigest() #Return the required hexadecimal hash
