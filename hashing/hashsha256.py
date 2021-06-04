import os, hashlib, requests, bs4, re, sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def stringToSHA256(string):

    result = hashlib.sha256(string.encode()) #Create a SHA256 hash object

    return result.hexdigest() #Return the required hexadecimal hash
