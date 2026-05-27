#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
python3 -c "
data = open('$DIR/../src/flag2of2-final.pdf', 'rb').read()
png_end = data.find(b'IEND') + 8
with open('$DIR/flag.png', 'wb') as f:
    f.write(data[:png_end])
with open('$DIR/flag.pdf', 'wb') as f:
    f.write(data[png_end:])
print('Extracted flag.png and flag.pdf')
"