import os, hashlib, requests, bs4, re, sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def stringToNTLM(string):

    result = hashlib.new('md4', string.encode('utf-16le'))

    return result.hexdigest()

def verifyNTLM(ntlm):
    
