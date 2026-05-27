#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
strings "$DIR/../src/cat.jpg" | grep -oE '[A-Za-z0-9+/]{10,}={0,2}' | while read b64; do
    echo "$b64" | base64 -d 2>/dev/null | grep -oE 'picoCTF\{[^}]+\}' && break
done
