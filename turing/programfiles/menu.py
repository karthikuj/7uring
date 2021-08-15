#!/usr/bin/python3
colors = {
    'error':'\033[31;1m[x] ',
    'success':'\033[36;1m[-] ',
    'msg':'\033[33;1m '
    }

subcommand = ['hash', 'cipher', 'encoder']

hashes = ['--blake2b', '--md4', '--md5', '--ntlm', '--sha1',
          '--sha224', '--sha256', '--sha384', '--sha512', '--whirlpool']

ciphers = ['--bacon', '--caesar', '--monoalphabetic', '--morse',
           '--multitapsms', '--rot13', '--rot47', '--transposition']

encoders = ['--binary', '--octal', '--hexadecimal', '--base64']

options = ['--enc', '--dec', '--brute', '--rainbow']

menu = colors['msg'] + '''
Usage: 7uring [subcommand] [format] [option] [suboptions] data

[SUBCOMMANDS]
hash    -  To use hash functions and crack hashes.
cipher  -  To use cipher tools.
encoder -  To encode in some popular encoding mechanisms.


[FORMATS]

[Hashes]           [Ciphers]              [Encodings]
--blake2b          --bacon                --binary
--md4              --caesar               --octal
--md5              --monoalphabetic       --hexadecimal
--ntlm             --morse                --base64
--sha1             --multitapsms
--sha224           --rot13
--sha256           --rot47
--sha384           --transposition
--sha512
--whirlpool

[OPTIONS]
--enc     -   To encrypt using that format.
--dec     -   To decrypt that format. (Not for hashes)
--brute   -   To bruteforce the hashes and ciphers. Available for all hashes and
              caesar cipher.
--rainbow -   To crack hashes using rainbow tables.
              (Faster than brute but low chances)

[SUBOPTIONS]

[For --brute]
-w  -  To specify the wordlist path

'''

def printMenu():
    print(menu)
