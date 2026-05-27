#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
pdfinfo "$DIR/../src/confidential.pdf" 2>/dev/null | grep "^Author:" | awk -F':[[:space:]]*' '{print $2}' | base64 -d 2>/dev/null || echo "Try: strings ../src/confidential.pdf | grep Author"
