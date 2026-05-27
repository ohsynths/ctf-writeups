---
title: "CanYouSee"
date: 2026-05-27
category: forensics
description: "How about some hide and seek?"
---

# CanYouSee

## 🎯 Summary
A JPEG image with a base64-encoded flag hidden in the XMP metadata (ExifTool attribution URL).

## 🧩 Solution

The JPEG's APP1 (EXIF/XMP) segment contains an `cc:attributionURL` field with the value `cGljb0NURntNRTc0RDQ3QV9ISUREM05fM2I5MjA5YTJ9Cg==`. Decoding this base64 string reveals the flag.

```bash
echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fM2I5MjA5YTJ9Cg==" | base64 -d
```

## 🚩 Flag

```
picoCTF{ME74D47A_HIDD3N_3b9209a2}
```
