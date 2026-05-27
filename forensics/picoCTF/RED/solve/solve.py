from struct import unpack
import zlib
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
data = (BASE / 'src' / 'red.png').read_bytes()

idx = data.find(b'IDAT')
length = unpack('>I', data[idx-4:idx])[0]
raw = data[idx+4:idx+4+length]
decoded = zlib.decompress(raw)

width, height = 128, 128
bpp = 4
stride = width * bpp

# Reverse PNG filters
pos = 0
prev_row = [0] * stride
pixels = []
for y in range(height):
    filter_type = decoded[pos]
    pos += 1
    row = list(decoded[pos:pos+stride])
    pos += stride
    for x in range(stride):
        if filter_type == 0:
            pass
        elif filter_type == 1:
            row[x] = (row[x] + (row[x-bpp] if x >= bpp else 0)) & 0xFF
        elif filter_type == 2:
            row[x] = (row[x] + prev_row[x]) & 0xFF
        elif filter_type == 3:
            a = row[x-bpp] if x >= bpp else 0
            b = prev_row[x]
            row[x] = (row[x] + (a + b)//2) & 0xFF
        elif filter_type == 4:
            a = row[x-bpp] if x >= bpp else 0
            b = prev_row[x]
            c = prev_row[x-bpp] if x >= bpp else 0
            p = a + b - c
            pa = abs(p - a); pb = abs(p - b); pc = abs(p - c)
            pr = a if pa <= pb and pa <= pc else (b if pb <= pc else c)
            row[x] = (row[x] + pr) & 0xFF
    pixels.extend(row)
    prev_row = row

# LSB from all channels
bits = [str(b & 1) for b in pixels]
chars = []
for i in range(0, len(bits), 8):
    byte = bits[i:i+8]
    if len(byte) == 8:
        chars.append(chr(int(''.join(byte), 2)))
result = ''.join(chars)

import base64, re
# Take only first valid base64 chunk (the repeated pattern)
b64 = re.search(r'[A-Za-z0-9+/]{20,}={0,2}', result)
if b64:
    decoded = base64.b64decode(b64.group()).decode()
    # Extract just the flag
    flag = re.search(r'picoCTF\{[^}]+\}', decoded)
    if flag:
        print(flag.group())
