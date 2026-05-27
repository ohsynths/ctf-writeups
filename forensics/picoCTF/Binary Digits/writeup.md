---
title: "Binary Digits"
date: 2026-05-27
category: forensics
description: "This file doesn't look like much... just a bunch of 1s and 0s. But maybe it's not just random noise. Can you recover anything meaningful from this?"
---

# Binary Digits

## 🎯 Summary
A file of seemingly random 1s and 0s — can anything meaningful be recovered?

## 🧩 Solution

The file `digits.bin` contains 71,016 ASCII `0` and `1` characters. Converting each 8-bit chunk to a byte reveals a JPEG image header (`FF D8 FF E0`). Writing the raw bytes as a `.jpg` file produces an 800x500 image displaying the flag.

### Step 1: Convert binary string to bytes

```python
with open('digits.bin') as f:
    bits = f.read().strip()

data = bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))

with open('output.jpg', 'wb') as f:
    f.write(data)
```

## 🚩 Flag

```
picoCTF{h1dd3n_1n_th3_b1n4ry_cc2099d3}
```
