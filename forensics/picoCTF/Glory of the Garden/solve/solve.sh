#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
python3 -c "
data = open('$DIR/../src/garden.jpg', 'rb').read()
eoi = data.find(b'\xff\xd9')
print(data[eoi+2:].decode())
"