---
title: "DISKO 1"
date: 2026-05-27
category: forensics
description: "Can you find the flag in this disk image?"
---

# DISKO 1

## 🎯 Summary
A FAT32 disk image containing a Kali Linux `/bin` directory. The flag is stored as a plaintext string within the image.

## 🧩 Solution

Mount the disk image and search for the flag string, or simply run `strings` on the raw image.

```bash
strings disko-1.dd | grep -oE "picoCTF\{[^}]+\}"
```

## 🚩 Flag

```
picoCTF{1t5_ju5t_4_5tr1n9_e3408eef}
```
