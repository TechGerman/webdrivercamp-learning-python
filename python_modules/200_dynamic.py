#!/usr/bin/python3

import sys

n = 1
len_arg = len(sys.argv) - 1

if len_arg == 0:
    print(f'{len_arg} arguments.')
elif len_arg == n:
    print(f'{len_arg} argument:')
elif len_arg > n:
    print(f'{len_arg} arguments:')

for i in range(1, len(sys.argv)):
    print(f'{i}: {sys.argv[i]}')
