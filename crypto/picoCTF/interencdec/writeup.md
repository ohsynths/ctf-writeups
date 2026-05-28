---
title: "interencdec"
date: 2026-05-28
category: crypto
description: "Three-layer decoding: base64 encoded bytes literal → base64 → ROT19 Caesar cipher"
---

# interencdec

## 🎯 Summary

A file containing an encoded flag goes through three layers of encoding — base64, a Python bytes literal containing another base64 string, and finally a ROT19 Caesar shift.

## 🧩 Solution

### Layer 1: Base64

The file content `Yidk...` decodes to a Python bytes representation:

```
b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2xoNjBsMDBpfQ=='
```

### Layer 2: Base64 (inside the bytes literal)

Parsing the bytes literal and base64-decoding yields:

```
wpjvJAM{jhlzhy_k3jy9wa3k_lh60l00i}
```

This looks like a flag format (`wpjvJAM` → `picoCTF`) with a Caesar shift.

### Layer 3: ROT19

Checking all 25 shifts, ROT19 produces readable text:

```
picoCTF{caesar_d3cr9pt3d_ea60e00b}
```

## 🚩 Flag

```
picoCTF{caesar_d3cr9pt3d_ea60e00b}
```
