---
title: "Information"
date: 2026-05-27
category: forensics
description: "Files can always be changed in a secret way. Can you find the flag?"
---

# Information

## 🎯 Summary
A JPEG with a base64-encoded flag hidden in the XMP metadata's `cc:license` field.

## 🧩 Solution

The XMP metadata contains `<cc:license rdf:resource='cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'/>`. Decoding this base64 string reveals the flag.

```bash
echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d
```

## 🚩 Flag

```
picoCTF{the_m3tadata_1s_modified}
```
