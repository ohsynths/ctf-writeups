#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
strings "$DIR/../src/ukn_reality.jpg" | grep -oE '[A-Za-z0-9+/]{10,}={0,2}' | base64 -d 2>/dev/null | grep -oE 'picoCTF\{[^}]+\}'
