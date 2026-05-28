#!/bin/bash
# Unminify - Solve Script
# The flag is in the minified HTML source as a CSS class name

HOST="http://titan.picoctf.net:55492"

# Fetch the page and extract the flag
curl -sL "$HOST/" | grep -oP 'picoCTF\{[^}]+\}'
