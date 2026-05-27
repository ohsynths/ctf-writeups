---
title: "Ph4nt0m 1ntrud3r"
date: 2026-05-27
category: forensics
description: "A digital ghost has breached my defenses, and my sensitive data has been stolen! Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag."
---

# Ph4nt0m 1ntrud3r

## 🎯 Summary
A PCAP file containing crafted TCP packets. Each packet's payload is a base64-encoded chunk. Sorting by timestamp and concatenating the decoded bytes reveals the flag.

## 🧩 Solution

Each packet carries a base64 string in its TCP payload. Ordering by timestamp and concatenating all decoded bytes produces the flag.

```python
packets.sort(key=lambda x: x[0])  # sort by timestamp
decoded = b''.join(base64.b64decode(b64) for _, b64 in packets)
```

## 🚩 Flag

```
picoCTF{1t_w4snt_th4t_34sy_tbh_4r_36f4a666}
```
