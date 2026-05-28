---
title: Unminify
date: 2026-05-27
category: web
description: Flag hidden in a minified HTML page as a CSS class name on an empty <p> element.
---

## 🎯 Summary

The website serves a heavily minified HTML page. The flag is not hidden in text content but is used as a `class` attribute value on an empty `<p>` element in the page source.

## 🧩 Solution

1. Fetch the page source — it's one long minified line
2. Grep for `picoCTF{` reveals the flag:
   ```html
   <p class="picoCTF{pr3tty_c0d3_622b2c88}"></p>
   ```

"Unminify" was a red herring — you don't need to pretty-print it, just CTRL+F.

## 🚩 Flag

```
picoCTF{pr3tty_c0d3_622b2c88}
```
