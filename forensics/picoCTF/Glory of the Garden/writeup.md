---
title: "Glory of the Garden"
date: 2026-05-27
category: forensics
description: "This file contains more than it seems."
---

# Glory of the Garden

## 🎯 Summary
A JPEG image with the flag appended as plaintext after the EOI marker.

## 🧩 Solution

Data was appended to the JPEG after the `FF D9` (EOI) marker. Reading the trailing bytes reveals the flag.

```bash
strings garden.jpg | grep picoCTF
# or
tail -c 60 garden.jpg
```

## 🚩 Flag

```
picoCTF{more_than_m33ts_the_3y339140129}
```
