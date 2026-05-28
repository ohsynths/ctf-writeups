---
title: WebDecode
date: 2026-05-27
category: web
description: Base64-encoded flag hidden in a custom HTML attribute on the About page.
---

## 🎯 Summary

The `/about.html` page contains a custom attribute `notify_true` on a `<section>` element with a base64-encoded value. Decoding it reveals the flag.

## 🧩 Solution

1. Inspect `about.html` — a custom attribute `notify_true` is visible on the section element:
   ```html
   <section class="about" notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMjgzZTYyZmV9">
   ```
2. The value is base64 — decode it:
   ```
   echo "cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMjgzZTYyZmV9" | base64 -d
   ```

## 🚩 Flag

```
picoCTF{web_succ3ssfully_d3c0ded_283e62fe}
```
