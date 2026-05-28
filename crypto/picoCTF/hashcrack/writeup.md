---
title: "hashcrack"
date: 2026-05-28
category: crypto
description: "Crack three rounds of weakly-hashed passwords (MD5, SHA1, SHA256) to access a breached server's secret"
---

# hashcrack

## 🎯 Summary

A server breach revealed weakly-hashed passwords. Connect to the challenge server, crack three successive hashes (MD5, SHA1, SHA256) from a common-password wordlist, and recover the flag.

## 🧩 Solution

### Step 1: Connect and analyze

Connecting to the server presents three rounds of hashes to crack:

| Round | Hash | Type |
|-------|------|------|
| 1 | `482c811da5d5b4bc6d497ffa98491e38` | MD5 (32 hex chars) |
| 2 | `b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3` | SHA1 (40 hex chars) |
| 3 | `916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745` | SHA256 (64 hex chars) |

### Step 2: Crack each hash

Using a common-password wordlist (SecLists 100k NCSC list), each hash cracks to a weak password:

- `482c811da5d5b4bc6d497ffa98491e38` → **password123**
- `b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3` → **letmein**
- `916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745` → **qwerty098**

### Step 3: Submit passwords in sequence

Each correct submission advances to the next round. After the SHA256 hash is cracked, the server reveals the secret—the flag.

## 🚩 Flag

```
picoCTF{UseStr0nG_h@shEs_&PaSswDs!_4c95d69f}
```
