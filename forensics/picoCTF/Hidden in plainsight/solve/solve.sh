#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
steghide extract -sf "$DIR/../src/img.jpg" -p "pAzzword" -f -xf "$DIR/flag.txt"
cat "$DIR/flag.txt"
