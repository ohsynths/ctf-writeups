---
title: "Shared Secrets"
date: 2026-05-28
category: crypto
description: "Diffie-Hellman key exchange with a leaked client secret — recover the shared secret and decrypt the flag"
---

# Shared Secrets

## 🎯 Summary

A Diffie-Hellman key exchange was used to establish a shared secret for encrypting the flag. The server's secret `a` is unknown, but the client's secret `b` leaked into the output file. With `b` and the server's public key `A`, we can compute the shared secret `A^b mod p` and XOR-decrypt.

## 🧩 Solution

### Step 1: Analyze the encryption

From `encryption.py`:

- Public params: `g = 2`, `p` (1048-bit prime)
- Server's public key: `A = g^a mod p`
- Client's secret `b` and encrypted flag are written to file
- Encryption: `enc = bytes([x ^ (shared % 256) for x in flag])`
- Shared secret: `shared = A^b mod p`

The file `message.txt` contains `b` — one side of the exchange leaked their secret.

### Step 2: Compute the shared secret

Since we know both `A` and `b`, compute:

```python
shared = pow(A, b, p)
key_byte = shared % 256
```

### Step 3: Decrypt

The encryption is a single-byte XOR keystream (`shared % 256` XOR'd with every byte):

```python
flag = bytes([x ^ key_byte for x in enc])
```

## 🚩 Flag

```
picoCTF{dh_s3cr3t_bd38f376}
```
