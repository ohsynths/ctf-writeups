#!/usr/bin/env python3
"""HashCrack - picoCTF
Crack three rounds of weak password hashes (MD5, SHA1, SHA256) to reveal the flag."""

import socket
import sys

HOST = "verbal-sleep.picoctf.net"
PORT = 51255

# Known cracked passwords for each hash
ROUNDS = {
    "482c811da5d5b4bc6d497ffa98491e38": "password123",  # MD5
    "b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3": "letmein",  # SHA1
    "916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745": "qwerty098",  # SHA256
}

s = socket.socket()
s.settimeout(20)
s.connect((HOST, PORT))

buf = b""
flag = None

while True:
    try:
        data = s.recv(4096)
        if not data:
            break
        buf += data
        text = buf.decode(errors="replace")
        print(f"[<] {text.strip()}")

        # Check for flag
        if "picoCTF" in text:
            flag = text.split("picoCTF{")[1].split("}")[0]
            flag = f"picoCTF{{{flag}}}"
            break

        # Check if we need to send a password
        if "Enter the password" in text:
            for hash_val, pwd in ROUNDS.items():
                if hash_val in text:
                    print(f"[>] {pwd}")
                    s.sendall(pwd.encode() + b"\n")
                    buf = b""
                    break

    except socket.timeout:
        break

s.close()
print(f"\nFlag: {flag}" if flag else "\nFlag not found - check output above")
