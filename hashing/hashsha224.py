import os, re, sys, bs4, requests, hashlib

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def stringToSHA224(string):

    result = hashlib.sha224(string.encode()) #Create a sha224 hash object

    return result.hexdigest() #Return the required hexadecimal hash
