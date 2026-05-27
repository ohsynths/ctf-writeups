#!/bin/bash
ssh -o StrictHostKeyChecking=accept-new -p 51717 ctf-player@rhea.picoctf.net << 'EOF'
6abf4a82
cd dropin/files
sha256sum * | grep b09c99c555e2b39a7e97849181e8996bc6a62501f0149c32447d8e65e205d6d2 | awk '{print $2}'
EOF
# Then run: ./decrypt.sh files/<match>
