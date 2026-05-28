#!/usr/bin/env python3
"""Transformation - picoCTF
Each character in the encoded file packs two flag bytes: (byte1 << 8) | byte2."""

data = open(__file__).parent.parent / "src" / "enc"
flag = ''.join(chr(ord(c) >> 8) + chr(ord(c) & 0xFF) for c in data.read_text())
print(f"Flag: {flag}")
