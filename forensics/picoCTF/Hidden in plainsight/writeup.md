---
title: "Hidden in plainsight"
date: 2026-05-27
category: forensics
description: "You're given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag."
---

# Hidden in plainsight

## 🎯 Summary
A JPEG image harbors a steghide-embedded payload. The password is found in the JPEG comment metadata.

## 🧩 Solution

The JPEG comment field contains `c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9`, which decodes to `steghide:pAzzword`. Using steghide with password `pAzzword` extracts the flag.

```bash
# Find the hint in the JPEG comment
file img.jpg
# Output: ... comment: "c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9" ...

# Decode the base64 hint
echo "c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9" | base64 -d
# steghide:pAzzword

# Extract the hidden payload
steghide extract -sf img.jpg -p "pAzzword"
```

## 🚩 Flag

```
picoCTF{h1dd3n_1n_1m4g3_5d4cba73}
```
