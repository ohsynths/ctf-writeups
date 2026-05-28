---
title: "Quizploit"
date: 2026-05-28
category: pwn
description: "ELF binary analysis quiz — answer 13 questions about the binary to get the flag"
---

# Quizploit

## 🎯 Summary

A 13-question quiz testing knowledge of ELF binary analysis: architecture, linking, protections, vulnerability analysis, and exploitation concepts.

## 🧩 Solution

Use `readelf`, analysis of the provided C source, and basic binary exploitation knowledge to answer:

| # | Question | Answer |
|---|----------|--------|
| 1 | 32-bit or 64-bit? | `64-bit` |
| 2 | Linking type? | `dynamic` |
| 3 | Stripped or not? | `not stripped` |
| 4 | Buffer size? | `0x15` |
| 5 | Bytes read? | `0x90` |
| 6 | Buffer overflow? | `yes` |
| 7 | Vulnerable function? | `fgets` |
| 8 | Uncalled function? | `win` |
| 9 | Attack type? | `buffer overflow` |
| 10 | Overflow bytes? | `0x7B` |
| 11 | Protection enabled? | `NX` |
| 12 | NX bypass? | `ROP` |
| 13 | win() address? | `0x401176` |

## 🚩 Flag

```
picoCTF{my_bIn@4y_3xpl0it_fL@g_58c7b379}
```
