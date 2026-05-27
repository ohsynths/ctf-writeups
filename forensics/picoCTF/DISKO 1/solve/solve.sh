#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
strings "$DIR/../src/disko-1.dd" | grep -oE "picoCTF\{[^}]+\}"
