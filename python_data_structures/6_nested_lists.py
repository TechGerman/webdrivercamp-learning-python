#!/usr/bin/python3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in matrix:
    for x in i:
        print(x, end=" ")
    if i:
        print()
