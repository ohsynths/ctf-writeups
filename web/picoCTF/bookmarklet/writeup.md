---
title: Bookmarklet
date: 2026-05-27
category: web
description: A bookmarklet with a Vigenère-style cipher that decrypts the flag in-browser.
---

## 🎯 Summary

The page contains a bookmarklet in a textarea — a JavaScript snippet that decrypts an encrypted flag using a Vigenère-style cipher. Extracting the JS and running the decryption logic locally reveals the flag.

## 🧩 Solution

1. The page source has a `<textarea>` containing:
   ```javascript
   javascript:(function() {
       var encryptedFlag = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓ¨ÍÕÄ¦í";
       var key = "picoctf";
       var decryptedFlag = "";
       for (var i = 0; i < encryptedFlag.length; i++) {
           decryptedFlag += String.fromCharCode((encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256);
       }
       alert(decryptedFlag);
   })();
   ```
2. Run the same decryption in Python — subtract each key char code from the encrypted char code mod 256.

## 🚩 Flag

```
picoCTF{p@g3_turn3r_18d2fa20}
```
