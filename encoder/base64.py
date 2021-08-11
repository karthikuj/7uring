import base64, re, sys

colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m[o] '
    }

def base64Encode(text):
    textBytes = text.encode('ascii')

    base64Bytes = base64.b64encode(textBytes)
    b64 = base64Bytes.decode('ascii')

    print(colors['success'] + b64)

def verifyBase64(b64):
    base64Regex = re.compile(r'^[0-9a-zA-Z+=/]+$') #Create a regex object
    mo = base64Regex.search(b64) #Create a match object

    if mo == None:
        return False
    else:
        return True

def base64Decode(b64):
    
    if not verifyBase64(b64): #Check if bse64 string is valid
        print(colors['error'] + 'Invalid base64 string')
        sys.exit()
        
    base64Bytes = b64.encode('ascii')

    textBytes = base64.b64decode(base64Bytes)
    text = textBytes.decode('ascii')

    print(colors['success'] + text)
