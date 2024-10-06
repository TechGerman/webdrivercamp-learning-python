#!/usr/bin/python3

import sys
n = 0
for i in range(1, len(sys.argv)):
    n += int(sys.argv[i])
print(n)
