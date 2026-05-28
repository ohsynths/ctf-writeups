---
title: "head-dump"
date: "2026-05-28"
category: "web"
description: "Swagger API docs expose a `/heapdump` endpoint — Node.js heap snapshot contains the flag in plaintext."
---

## 🎯 Summary

A news blog site uses Swagger UI for API documentation. The `/api-docs` page (linked from a blog post about "#API Documentation") reveals an endpoint `/heapdump` that generates Node.js heap snapshots. The flag is stored as a string in the server's memory heap.

## 🧩 Solution

1. Blog post links to `/api-docs` (Swagger UI) — found via `#API Documentation` tag.
2. Swagger spec lists a `/heapdump` endpoint alongside standard CRUD endpoints.
3. `GET /heapdump` returns a ~10MB `.heapsnapshot` file containing the full Node.js memory heap.
4. Grep for `picoCTF{...}` pattern in the binary snapshot — flag is present as a plaintext string.

```bash
curl -sL "http://verbal-sleep.picoctf.net:50394/heapdump" | grep -oaE "picoCTF\{[^}]+\}"
```

## 🚩 Flag

```
picoCTF{Pat!3nt_15_Th3_K3y_a485f162}
```
