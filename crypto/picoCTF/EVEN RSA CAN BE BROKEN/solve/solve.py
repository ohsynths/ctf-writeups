#!/usr/bin/env python3
"""EVEN RSA CAN BE BROKEN - picoCTF
The prime generation is broken and N is even. Factor N = 2 * (N/2) and decrypt."""

import socket
import re

HOST = "verbal-sleep.picoctf.net"
PORT = 64554

# Connect and get N, e, c
s = socket.socket()
s.settimeout(10)
s.connect((HOST, PORT))
data = b""
while True:
    try:
        chunk = s.recv(4096)
        if not chunk:
            break
        data += chunk
    except:
        break
s.close()

text = data.decode()
N = int(re.search(r"N:\s*(\d+)", text).group(1))
e = int(re.search(r"e:\s*(\d+)", text).group(1))
c = int(re.search(r"cyphertext:\s*(\d+)", text).group(1))

# N is even — p must be 2
p = 2
q = N // 2

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, m):
    g, x, _ = egcd(a, m)
    assert g == 1
    return x % m

phi = (p - 1) * (q - 1)
d = modinv(e, phi)
m = pow(c, d, N)

flag = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()
print(f"Flag: {flag}")
