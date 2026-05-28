#!/usr/bin/env python3
"""vault-door-training - picoCTF
Password is hardcoded in the checkPassword method."""

import re

src = open(__file__).parent.parent / "src" / "VaultDoorTraining.java"
content = src.read_text()
match = re.search(r'password\.equals\("([^"]+)"\)', content)
flag = f"picoCTF{{{match.group(1)}}}"
print(f"Flag: {flag}")
