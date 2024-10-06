#!/usr/bin/python3

list_ = [5, 4, 3, 2, 1]
index = 2


def get_element():
    if index < 0 or index >= len(list_):
        return None
    else:
        print(f'The element is retrived is {list_[index]}')


get_element()
