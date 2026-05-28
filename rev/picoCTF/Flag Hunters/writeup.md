---
title: "Flag Hunters"
date: 2026-05-28
category: rev
description: "Python lyric reader with a CROWD input injection — semicolon in crowd input gets parsed as a command separator on subsequent REFRAIN visits"
---

# Flag Hunters

## 🎯 Summary

A Python program reads through song lyrics with a subroutine-like REFRAIN mechanism. The flag is hidden in `secret_intro` at line 0, which is never printed in normal flow. The CROWD input handler allows injecting arbitrary text into a song line, and the `;` command separator lets us inject a `RETURN 0` jump.

## 🧩 Solution

### Step 1: Analyze the reader

The `reader()` function processes lyrics line by line. Key commands:
- `REFRAIN` — jumps to the `[REFRAIN]` section (subroutine call)
- `RETURN <n>` — jumps to line `n` (subroutine return)
- `CROWD ...` — prompts for user input, stores it in the current line as `Crowd: <input>`
- `;` — splits a line into multiple commands

The flag is stored in `secret_intro` at `song_lines[0]`, but the reader starts at `[VERSE1]`.

### Step 2: Inject a RETURN 0

When the REFRAIN hits the `CROWD` prompt, the input is stored in `song_lines[lip]` with the prefix `Crowd: `. On the *next* visit to the REFRAIN section, this modified line is split by `;`:

```
Crowd: hello;RETURN 0
```
→ `['Crowd: hello', 'RETURN 0']`
→ `RETURN 0` sets `lip = 0`, jumping to the secret intro.

### Step 3: Flag printed

Line 0 containing `secret_intro` + flag is printed to stdout.

## 🚩 Flag

```
picoCTF{70637h3r_f0r3v3r_0099cf61}
```
