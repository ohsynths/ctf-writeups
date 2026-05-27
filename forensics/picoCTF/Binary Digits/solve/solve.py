from pathlib import Path
BASE = Path(__file__).resolve().parent.parent
bits = (BASE / 'src' / 'digits.bin').read_text().strip()

data = bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))

with open('output.jpg', 'wb') as f:
    f.write(data)

print('Written to output.jpg')
