---
title: "EVEN RSA CAN BE BROKEN"
date: 2026-05-28
category: crypto
description: "RSA with a broken prime generator that produces an even N — factor N = 2 × (N/2) and decrypt"
---

# EVEN RSA CAN BE BROKEN

## 🎯 Summary

An RSA encryption service provides N, e, and the ciphertext. The prime generation is fatally broken — N is even, meaning one of the "primes" is 2. With p=2, computing the private key is trivial.

## 🧩 Solution

### Step 1: Connect and inspect

The server outputs N, e, and the encrypted ciphertext. Spot the problem immediately — N is even:

```
N = 13625712633977910266381273726288996340432681072368980643440471939480677106577072551343837160202236830758497654156837605062931863200391993598663813279277874
```

An even N that is meant to be the product of two primes can only mean **p = 2**.

### Step 2: Factor and decrypt

- If N is even, one factor is 2.
- Set `p = 2`, `q = N // 2`
- Compute `phi = (2-1) × (q-1) = q - 1`
- Compute `d = e⁻¹ mod phi`
- Decrypt: `m = c^d mod N`

### Step 3: Convert to bytes

```
picoCTF{tw0_1$_pr!m375129bb1}
```

## 🚩 Flag

```
picoCTF{tw0_1$_pr!m375129bb1}
```
