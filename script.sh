#!/bin/bash
for subnet in `bash main.py 2>/dev/null`; do ufw deny from $subnet; done
