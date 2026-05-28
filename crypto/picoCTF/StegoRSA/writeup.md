---
title: "StegoRSA"
date: 2026-05-28
category: crypto
description: "RSA-encrypted message with the private key hidden in a JPEG comment via hex encoding"
---

# StegoRSA

## 🎯 Summary

We're given an RSA-encrypted file (`flag.enc`) and a JPEG image (`image.jpg`). The public key is missing, but the private key was carelessly embedded in the image's metadata.

## 🧩 Solution

### Step 1: Inspect the image

Running `file` on the JPEG reveals a comment field containing hex-encoded data:

```
$ file image.jpg
JPEG image data, ..., comment: "2d2d2d2d2d424547494e..."
```

Decoding the hex prefix `2d2d2d2d2d` → `-----` and `424547494e20` → `BEGIN ` — it's a PEM private key encoded as a hex string.

### Step 2: Extract the private key

Parse the JPEG comment marker (`FF FE`) from the binary, read the comment length, extract the hex string, and decode it to a PEM file.

### Step 3: Decrypt the flag

Use the recovered RSA private key with `openssl pkeyutl -decrypt` to decrypt `flag.enc`:

```
$ openssl pkeyutl -decrypt -inkey private.pem -in flag.enc
```

## 🚩 Flag

```
picoCTF{rs4_k3y_1n_1mg_ce170c3d}
```
