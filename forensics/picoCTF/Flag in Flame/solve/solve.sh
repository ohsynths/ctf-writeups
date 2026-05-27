#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
base64 -d "$DIR/../src/logs.txt" > "$DIR/output.png"
echo "Decoded to output.png"
