import hashlib, requests, bs4, re, os, sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def stringToSHA512(string):

    result = hashlib.sha512(string.encode()) #Create a SHA512 hash object

    return result.hexdigest() #Return the required hexadecimal hash
