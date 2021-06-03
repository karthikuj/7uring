from hashing.hashmd5 import *
from hashing.hashsha1 import *

print(stringToSHA1('ironman'))
print(verifySHA1(stringToSHA1('ironman')))
sha1ToString(stringToSHA1('ironman'))
sha1ToString(stringToSHA1('ironmankijai'))
sha1Brute(stringToSHA1('ironman'), '/usr/share/wordlists/rockyou.txt')
