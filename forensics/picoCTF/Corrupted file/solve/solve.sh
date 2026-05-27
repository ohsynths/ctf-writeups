#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
python3 -c "
data = open('$DIR/../src/file', 'rb').read()
fixed = b'\xff\xd8' + data[2:]
open('$DIR/fixed.jpg', 'wb').write(fixed)
print('Fixed JPEG written to fixed.jpg')
"