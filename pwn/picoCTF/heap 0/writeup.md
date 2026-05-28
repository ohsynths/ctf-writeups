---
title: "heap 0"
date: 2026-05-28
category: pwn
description: "Heap buffer overflow — scanf(%s) with no size limit overflows input_data into adjacent safe_var"
---

# heap 0

## 🎯 Summary

A heap-based overflow: `input_data` and `safe_var` are 5-byte buffers allocated adjacently on the heap. `write_buffer()` uses `scanf("%s")` with no bounds check, allowing overflow into `safe_var`.

## 🧩 Solution

The printed heap addresses show `safe_var` is at `input_data + 0x20`. Writing 33+ bytes into `input_data` overwrites `safe_var`'s first byte, changing it from `"bico"` to something else, which triggers the win condition.

```python
# Overflow: 32 bytes padding + 1 byte to corrupt safe_var
s.sendall(b"A" * 32 + b"x")
```

## 🚩 Flag

```
picoCTF{my_first_heap_overflow_0c473fe8}
```
