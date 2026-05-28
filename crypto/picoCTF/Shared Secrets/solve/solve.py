#!/usr/bin/env python3
# Shared Secrets - picoCTF
# Diffie-Hellman: client secret b leaked, compute shared = A^b mod p, XOR decrypt

from pathlib import Path

src = Path(__file__).parent / ".." / "src"

# Read challenge data
with open(src / "message.txt") as f:
    lines = f.readlines()

g = int(lines[0].split("=")[1].strip())
p = int(lines[1].split("=")[1].strip())
A = int(lines[2].split("=")[1].strip())
b = int(lines[3].split("=")[1].strip())
enc_hex = lines[4].split("=")[1].strip()

# Compute shared secret
shared = pow(A, b, p)
key_byte = shared % 256

# Decrypt (single-byte XOR keystream)
enc = bytes.fromhex(enc_hex)
flag = bytes([x ^ key_byte for x in enc])

flag_str = flag.decode().strip()
print(f"Flag: {flag_str}")

# Save to solve directory
out = Path(__file__).parent / "flag.txt"
out.write_text(flag_str)
