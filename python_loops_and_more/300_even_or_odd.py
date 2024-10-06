#!/usr/bin/python3

import random
random_num = random.randint(-10000, 10000)

if random_num > 0:
    last_digit = random_num % 10
else:
    last_digit = random_num % -10

if last_digit == 0:
    print(f'{random_num} the last digit {last_digit} is zero')
elif last_digit % 2 == 0:
    even_status = 'even'
    print(f'{random_num} the last digit {last_digit} is {even_status}')
else:
    even_status = 'odd'
    print(f'{random_num} the last digit {last_digit} is {even_status}')
