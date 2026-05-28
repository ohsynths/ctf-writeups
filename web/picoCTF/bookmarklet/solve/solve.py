#!/usr/bin/env python3
# Bookmarklet - Solve Script
# The bookmarklet contains a Vigenère-like decryption of the flag

import urllib.request
import re

resp = urllib.request.urlopen("http://titan.picoctf.net:50897/")
html = resp.read().decode("utf-8")

match = re.search(r'var encryptedFlag = "([^"]+)";', html)
encrypted = match.group(1)
key = "picoctf"

flag = ""
for i in range(len(encrypted)):
    flag += chr((ord(encrypted[i]) - ord(key[i % len(key)]) + 256) % 256)

print(flag)
