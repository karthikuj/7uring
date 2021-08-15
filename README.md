<h1 align="center">
  <br>
  <a href="https://github.com/karthikuj/7uring"><img src="https://raw.githubusercontent.com/karthikuj/karthikuj/master/images/7uring.png" alt="7uring" title="7uring"></a>
  <br>
  7uring: Not your ordinary hashcracker.
  <br>
</h1>


## [-] About 7uring:

7uring is an advanced cryptography tool which works with some of the most popular hashes, encodings and ciphers. 7uring's advanced hash functions can check online rainbow tables before you try to bruteforce the hashes, because of which your hashes are cracked in a matter of seconds.

In the future, we plan to incorporate steganography, cryptanalysis and much more.

In short 7uring can take your CTF rank up a notch.


## [-] Installing 7uring:

You can install `7uring` like this:

1. Clone the repository:
```
git clone https://github.com/karthikuj/7uring.git
```

2. Change the directory:
```
cd 7uring/
```

3. Install required modules:
```
python -m pip install -r requirements.txt
```

4. Install the package:
```
pip install .
```


## [-] Using 7uring:

### Syntax:
```
7uring [subcommand] [format] [option] [suboption] data
```

### Subcommands:
```
hash
```
```
cipher
```
```
encoder
```

### Formats:

#### Hash:
```
--blake2b
```
```
--md4
```
```
--md5
```
```
--ntlm
```
```
--sha1
```
```
--sha224
```
```
--sha256
```
```
--sha384
```
```
--sha512
```
```
--whirlpool
```

#### Ciphers:
```
--bacon
```
```
--caesar
```
```
--monoalphabetic
```
```
--morse
```
```
--multitapsms
```
```
--rot13
```
```
--rot47
```
```
--transposition
```

#### Encodings:
```
--binary
```
```
--octal
```
```
--hexadecimal
```
```
--base64
```

#### Options: 

To encrypt:
```
--enc
```

To decrypt:
```
--dec
```

To check online rainbow tables (for hashes only!):
```
--rainbow
```

To bruteforce:
```
--brute
```

#### Suboptions:
The only suboption is ```-w``` to specify wordlist while using ```--brute```

## [-] Examples:
```
7uring --help
```
```
7uring hash --md5 --enc spongebob
```
```
7uring hash --md5 --rainbow e1964798cfe86e914af895f8d0291812
```
```
7uring cipher --caesar --enc spongebob
```
```
7uring hash --md5 --brute -w /usr/share/wordlists/rockyou.txt e1964798cfe86e914af895f8d0291812
```

## [-] Uninstalling 7uring:
#### Sorry to see you go :(
```
pip uninstall 7uring
```

#### Made with ❤️ by <a href="https://www.instagram.com/5up3r541y4n/" target="_blank">@5up3r541y4n</a>
