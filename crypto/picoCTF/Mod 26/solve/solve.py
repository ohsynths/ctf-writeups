#!/usr/bin/env python3
"""Mod 26 - picoCTF
Simple ROT13 Caesar cipher."""

import codecs

data = open(__file__).parent.parent / "src" / "values.txt"
data = data.read_text().strip()
flag = codecs.decode(data, 'rot13')
print(f"Flag: {flag}")
