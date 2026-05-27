---
title: "Riddle Registry"
date: 2026-05-27
category: forensics
description: "Hi, intrepid investigator! You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as appears. Amidst the chaos lies a hidden treasure — an elusive flag waiting to be uncovered."
---

# Riddle Registry

## 🎯 Summary
A PDF full of lorem ipsum gibberish — the flag is hidden in the document metadata.

## 🧩 Solution

The PDF's `/Author` field in the metadata contains a base64-encoded string. Decoding it reveals the flag.

```bash
# Extract the Author field and decode
pdfinfo confidential.pdf | grep "^Author:" | sed 's/^Author:\s*//' | tr -d '()' | sed 's/\\075/=/g' | base64 -d
```

Or simply inspect the raw PDF — the string `cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9mOTQzMDBjNH0=` is visible in the `/Author` entry.

## 🚩 Flag

```
picoCTF{puzzl3d_m3tadata_f0und!_f94300c4}
```
