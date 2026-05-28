---
title: "Transformation"
date: 2026-05-28
category: rev
description: "Two ASCII bytes packed into each Unicode character via (byte1 << 8) | byte2"
---

# Transformation

## 🎯 Summary

The `enc` file contains Unicode characters where each character encodes two ASCII bytes: the high byte shifted left by 8, OR'd with the low byte.

## 🧩 Solution

Reverse the transformation:

```python
flag = ''.join(chr(ord(c) >> 8) + chr(ord(c) & 0xFF) for c in enc)
```

Split each character into high and low bytes.

## 🚩 Flag

```
picoCTF{16_bits_inst34d_of_8_b7f62ca5}
```
