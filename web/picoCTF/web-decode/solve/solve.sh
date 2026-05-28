#!/bin/bash
# WebDecode - Solve Script
# The flag is base64-encoded in a custom attribute on about.html

HOST="http://titan.picoctf.net:59117"

# Extract the notify_true attribute value from about.html
encoded=$(curl -sL "$HOST/about.html" | grep -oP 'notify_true="\K[^"]+')
# Decode base64
echo "$encoded" | base64 -d
echo
