---
title: Cookie Monster Secret Recipe
date: 2026-05-27
category: web
description: A login page that sets a base64-encoded cookie containing the flag.
---

## 🎯 Summary

A login form that sets a `secret_recipe` HTTP cookie on any login attempt. The cookie value is base64-encoded — decode it to get the flag.

## 🧩 Solution

1. POST to `login.php` with any credentials
2. Server responds with `Access Denied` and sets a `secret_recipe` cookie:
   ```
   Set-Cookie: secret_recipe=cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzc4QjRDMzkwfQ%3D%3D
   ```
3. The `%3D%3D` is URL-encoding for `==` — the value is base64
4. Decode:
   ```
   echo "cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzc4QjRDMzkwfQ==" | base64 -d
   ```

## 🚩 Flag

```
picoCTF{c00k1e_m0nster_l0ves_c00kies_78B4C390}
```
