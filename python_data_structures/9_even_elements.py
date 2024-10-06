#!/usr/bin/python3

my_list = [5, 4, 3, 2, 1]
boolean_my_list = []

for i in my_list:
    if i % 2 == 0:
        boolean_my_list.append(True)
    else:
        boolean_my_list.append(False)
boolean = tuple(boolean_my_list)
print(f'{my_list} \n{boolean}')
