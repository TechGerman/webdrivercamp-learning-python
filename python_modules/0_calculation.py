#!/usr/bin/python3

if __name__ == "__main__":
    import calculation

a = 4
b = 2
print(f'{a} + {b} = {calculation.add(a, b)}')
print(f'{a} - {b} = {calculation.sub(a, b)}')
print(f'{a} * {b} = {calculation.mul(a, b)}')
print(f'{a} / {b} = {calculation.div(a, b)}')
