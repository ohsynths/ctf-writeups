---
title: "Verify"
date: 2026-05-27
category: forensics
description: "People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate."
---

# Verify

## 🎯 Summary
SSH into a server, find the file matching a given SHA-256 checksum, then decrypt it with the provided script to reveal the flag.

## 🧩 Solution

1. SSH into the server with the given password.
2. Search through the `files/` directory for the file whose SHA-256 matches `b09c99c555e2b39a7e97849181e8996bc6a62501f0149c32447d8e65e205d6d2`.
3. Run `./decrypt.sh files/<match>` to decrypt the file and get the flag.

```bash
ssh -p 51717 ctf-player@rhea.picoctf.net
# password: 6abf4a82
cd drop-in
sha256sum files/* | grep b09c99c555e2b39a7e97849181e8996bc6a62501f0149c32447d8e65e205d6d2
# -> 451fd69b
./decrypt.sh files/451fd69b
```

## 🚩 Flag

```
picoCTF{trust_but_verify_451fd69b}
```
