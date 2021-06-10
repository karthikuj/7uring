import hashlib, requests, bs4, re, os, sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def stringToBlake2b(string):

    result = hashlib.blake2b(string.encode()) #Create a blake2b hash object

    return result.hexdigest() #Return the required hexadecimal hash
