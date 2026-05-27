---
title: "RED"
date: 2026-05-27
category: forensics
description: "RED, RED, RED, RED"
---

# RED

## 🎯 Summary
A 128×128 RGBA PNG image. The tEXt chunk contains a poem whose first letters spell "CHECKLSB". Extracting the LSB from all pixel channels reveals a repeated base64 string containing the flag.

## 🧩 Solution

1. The PNG metadata has a `tEXt` chunk with a poem. The first letter of each line spells `CHECKLSB`.
2. Reverse the PNG filters (Sub/Up/Average/Paeth) to get raw pixel data.
3. Extract the LSB from every RGBA byte, group into 8-bit chunks, and decode as ASCII.
4. The resulting string is a base64 payload. Decoding it yields the flag.

```python
# After reversing PNG filters and extracting LSB from all channels:
bits = [str(b & 1) for b in pixels]
result = ''.join(chr(int(''.join(bits[i:i+8]), 2)) for i in range(0, len(bits), 8))
# Extract base64 substring and decode
import base64, re
b64 = re.search(r'[A-Za-z0-9+/=]{20,}', result)
flag = base64.b64decode(b64.group()).decode()
```

## 🚩 Flag

```
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}
```
