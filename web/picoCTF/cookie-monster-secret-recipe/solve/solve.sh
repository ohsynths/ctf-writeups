#!/bin/bash
# Cookie Monster Secret Recipe - Solve Script
# The flag is hidden in a "secret_recipe" cookie set on login

HOST="http://verbal-sleep.picoctf.net:62257"

# POST to login.php - any credentials work, server always returns a cookie
response=$(curl -s -X POST "$HOST/login.php" \
  -d "username=admin&password=admin" \
  -c -)

# Extract the secret_recipe cookie value, URL-decode, base64-decode
cookie=$(echo "$response" | grep secret_recipe | awk '{print $NF}' | python3 -c "import sys,urllib.parse; print(urllib.parse.unquote(sys.stdin.read().strip()))")
flag=$(echo "$cookie" | cut -d= -f2 | python3 -c "import sys,base64; print(base64.b64decode(sys.stdin.read().strip()).decode())")
echo "$flag"
