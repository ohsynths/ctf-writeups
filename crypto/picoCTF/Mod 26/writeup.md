---
title: "Mod 26"
date: 2026-05-28
category: crypto
description: "ROT13 Caesar cipher — shift each letter by 13 positions"
---

# Mod 26

## 🎯 Summary

A classic ROT13 substitution cipher. Each letter is shifted by 13 positions in the alphabet (26 letters, hence "Mod 26").

## 🧩 Solution

### Step 1: Read the ciphertext

```
cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_45559noq}
```

### Step 2: Apply ROT13

ROT13 is its own inverse — applying it twice returns the original. Each letter is shifted by 13:

```
picoCTF{next_time_I'll_try_2_rounds_of_rot13_45559abd}
```

## 🚩 Flag

```
picoCTF{next_time_I'll_try_2_rounds_of_rot13_45559abd}
```
