#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
    line = line.strip()
    fields = re.split(r'[-\[\]]+', line)
    if len(fields) >= 2:
        date = fields[1].split()[0]
        if "error" in fields[2].lower():
            print(date + "\terror\t1")
        else:
            print(date + "\notice\t1")
