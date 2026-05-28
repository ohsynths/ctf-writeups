#!/usr/bin/env python3
"""Quizploit - picoCTF
Answer 13 questions about the ELF binary to get the flag."""

import socket
import time

HOST = "lonely-island.picoctf.net"
PORT = 59129

answers = [
    "64-bit",           # Q1: ELF class
    "dynamic",          # Q2: linking type
    "not stripped",     # Q3: debugging symbols present
    "0x15",            # Q4: buffer size
    "0x90",            # Q5: bytes read via fgets
    "yes",             # Q6: buffer overflow possible?
    "fgets",           # Q7: vulnerable function
    "win",             # Q8: uncalled function
    "buffer overflow", # Q9: attack type
    "0x7B",            # Q10: overflow bytes (0x90 - 0x15)
    "NX",              # Q11: enabled protection
    "ROP",             # Q12: NX bypass technique
    "0x401176",        # Q13: win() address
]

s = socket.socket()
s.settimeout(10)
s.connect((HOST, PORT))
time.sleep(1)

for ans in answers:
    s.sendall((ans + "\n").encode())
    time.sleep(0.4)

time.sleep(1)
data = b""
try:
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        data += chunk
except:
    pass

text = data.decode(errors='replace')
for line in text.split('\n'):
    if 'Flag' in line or 'flag' in line or 'picoCTF' in line:
        print(line.strip())

s.close()
