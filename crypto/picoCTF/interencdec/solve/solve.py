#!/usr/bin/env python3
"""interencdec - picoCTF
Three-layer decoding: base64 → Python bytes literal → base64 → ROT19 cipher."""

import base64
import ast
from pathlib import Path

data = Path(__file__).parent.parent / "src" / "enc_flag"
data = data.read_text().strip()

# Layer 1: Base64 → Python bytes literal
layer1 = base64.b64decode(data).decode().strip()
inner = ast.literal_eval(layer1)

# Layer 2: Base64 → ciphertext
ciphertext = base64.b64decode(inner).decode()

# Layer 3: ROT19 (Caesar shift of 19)
flag = ''.join(
    chr((ord(c) - 97 + 19) % 26 + 97) if 'a' <= c <= 'z' else
    chr((ord(c) - 65 + 19) % 26 + 65) if 'A' <= c <= 'Z' else c
    for c in ciphertext
)

print(f"Flag: {flag}")
