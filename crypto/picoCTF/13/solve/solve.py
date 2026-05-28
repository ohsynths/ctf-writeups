#!/usr/bin/env python3
"""13 - picoCTF
ROT13 Caesar cipher."""

import codecs

s = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
print(f"Flag: {codecs.decode(s, 'rot13')}")
