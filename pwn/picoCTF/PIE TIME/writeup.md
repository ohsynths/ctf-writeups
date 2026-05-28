---
title: "PIE TIME"
date: 2026-05-28
category: pwn
description: "PIE binary leaks main() address — calculate win() offset and jump to it"
---

# PIE TIME

## 🎯 Summary

A PIE-enabled binary prints the runtime address of `main()`. The user can supply any address to jump to. Calculate `win()`'s address using the known offset difference.

## 🧩 Solution

From `readelf`:
- `win`  offset: `0x12a7`
- `main` offset: `0x133d`
- Delta: `0x96`

Receive the leaked `main` address, subtract the delta, send the resulting `win` address.

```python
win_addr = main_addr - (0x133d - 0x12a7)
```

## 🚩 Flag

```
picoCTF{b4s1c_p051t10n_1nd3p3nd3nc3_28a46dcd}
```
