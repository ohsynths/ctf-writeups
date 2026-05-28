---
title: "vault-door-training"
date: 2026-05-28
category: rev
description: "Java source code with the password hardcoded in checkPassword() — reading comprehension challenge"
---

# vault-door-training

## 🎯 Summary

A Java program checks the vault password against a hardcoded string. The source code is provided, making this trivial.

## 🧩 Solution

The `checkPassword` method directly compares the input against a string literal:

```java
return password.equals("w4rm1ng_Up_w1tH_jAv4_000uMfhzBuS");
```

## 🚩 Flag

```
picoCTF{w4rm1ng_Up_w1tH_jAv4_000uMfhzBuS}
```
