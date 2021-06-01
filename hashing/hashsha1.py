import hashlib, requests, bs4, re, os, sys

def stringToSHA1(string):
    result = hashlib.sha1(string.encode()) #Create a SHA1 hash object

    return result.hexdigest()
