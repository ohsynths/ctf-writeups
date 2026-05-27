---
title: "Secret of the Polyglot"
date: 2026-05-27
category: forensics
description: "The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file?"
---

# Secret of the Polyglot

## 🎯 Summary
A PNG/PDF polyglot file — the PNG image shows the first half of the flag, and extracting the PDF text reveals the second half.

## 🧩 Solution

The file `flag2of2-final.pdf` is a polyglot: it's both a valid PNG and a valid PDF. The PNG ends at offset 0x392 where the PDF begins. The PNG displays the first half of the flag (`f1u3n7_`), and the PDF text contains the second half (`1n_pn9_&_pdf_1f991f77}`).

```python
# Split the polyglot
data = open('flag2of2-final.pdf', 'rb').read()
png_end = data.find(b'IEND') + 8
png = data[:png_end]   # -> flag.png
pdf = data[png_end:]   # -> flag.pdf
# PNG shows: f1u3n7_
# PDF text shows: 1n_pn9_&_pdf_1f991f77}
```

## 🚩 Flag

```
picoCTF{f1u3n7_1n_pn9_&_pdf_1f991f77}
```
