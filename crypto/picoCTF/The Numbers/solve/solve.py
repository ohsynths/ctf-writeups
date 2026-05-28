#!/usr/bin/env python3
"""The Numbers - picoCTF
A1Z26 cipher: each number maps to its position in the alphabet."""

s = "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }"
flag = ''.join(chr(int(n) + 64) if n.isdigit() else n for n in s.split())
print(f"Flag: {flag}")
