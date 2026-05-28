#!/bin/bash
# StegoRSA - picoCTF
# Extract RSA private key from JPEG comment, decrypt flag.enc

cd "$(dirname "$0")/../src"

# Extract hex-encoded private key from JPEG comment
python3 -c "
import struct
with open('image.jpg', 'rb') as f:
    data = f.read()
start = data.find(b'\xff\xfe')
length = struct.unpack('>H', data[start+2:start+4])[0]
comment_data = data[start+4:start+4+length-2]
decoded = bytes.fromhex(comment_data.decode())
with open('private.pem', 'wb') as out:
    out.write(decoded)
print('Private key extracted')
"

# Decrypt the flag using the extracted key
openssl pkeyutl -decrypt -inkey private.pem -in flag.enc -out ../solve/flag.txt

echo "Flag:"
cat ../solve/flag.txt
