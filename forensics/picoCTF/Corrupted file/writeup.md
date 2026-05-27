---
title: "Corrupted file"
date: 2026-05-27
category: forensics
description: "This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life?"
---

# Corrupted file

## 🎯 Summary
A corrupted file with `\x` replacing the JPEG SOI marker (`FF D8`). Fixing the header restores the image which displays the flag.

## 🧩 Solution

The file has `\x` (0x5c 0x78) at the start instead of `FF D8` (JPEG SOI marker). Replacing those two bytes with `FF D8` recovers the image.

```python
data = open('file', 'rb').read()
fixed = b'\xff\xd8' + data[2:]
open('fixed.jpg', 'wb').write(fixed)
```

## 🚩 Flag

```
picoCTF{r3st0r1ng_th3_by73s_b67c1558}
```
