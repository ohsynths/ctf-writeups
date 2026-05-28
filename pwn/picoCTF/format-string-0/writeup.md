---
title: "format string 0"
date: "2026-05-28"
category: "pwn"
description: "Two-phase format string exploitation — use %114d to exceed output threshold, then %s to trigger a SIGSEGV and leak the flag."
---

## 🎯 Summary

Two-stage binary exploitation challenge. Patrick requires an order that produces >64 characters of `printf` output to unlock Bob's menu. Bob's menu contains a format string with `%s` specifiers that read from the stack — hitting an invalid pointer triggers `SIGSEGV`, whose handler prints the flag.

## 🧩 Solution

**Patrick (Phase 1):**
- Menu includes `Gr%114d_Cheese` — the `%114d` format specifier prints an integer padded to width 114.
- Sending this exact string passes the `strcmp` menu check, then `printf(choice1)` produces ~123+ characters, exceeding the 64-char threshold.
- This triggers `serve_bob()`.

**Bob (Phase 2):**
- Menu includes `Cla%sic_Che%s%steak` — contains two `%s` format specifiers.
- Sending this exact string passes the menu check, then `printf(choice2)` tries to read string pointers from the stack.
- The first `%s` dereferences whatever is on the stack (likely invalid/null) → segfault → `sigsegv_handler` prints `flag`.

**Solve:**
```python
r.sendline(b"Gr%114d_Cheese")    # Phase 1: exceed printf threshold
r.sendline(b"Cla%sic_Che%s%steak") # Phase 2: %s → segfault → flag
```

## 🚩 Flag

```
picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_dc0f36c4}
```
