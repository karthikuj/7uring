import os, re, sys, bs4, requests, hashlib

def stringToSHA224(string):

    result = hashlib.sha224(string.encode()) #Create a sha224 hash object

    return result.hexdigest() #Return the required hexadecimal hash
