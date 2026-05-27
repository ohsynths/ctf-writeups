---
title: "Flag in Flame"
date: 2026-05-27
category: forensics
description: "The SOC team discovered a suspiciously large log file after a recent breach. When they opened it, they found an enormous block of encoded text instead of typical logs. Could there be something hidden within?"
---

# Flag in Flame

## 🎯 Summary
A large text file containing base64-encoded PNG image data. The image displays a hex string which decodes to the flag.

## 🧩 Solution

The file `logs.txt` is base64-encoded data. Decoding it reveals a 896×1152 PNG image. The image displays a hex string — convert each pair of hex digits to ASCII to get the flag.

```bash
base64 -d logs.txt > output.png
# Read the hex string from the image, then:
echo "7069636F435446..." | xxd -r -p
```

## 🚩 Flag

```
picoCTF{forensics_analysis_is_amazing_5ccc7cb0}
```
