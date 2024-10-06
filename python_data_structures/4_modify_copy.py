#!/usr/bin/python3

list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5

list_new = list_.copy()


def replace_element():
    if index < 0 or index >= len(list_new):
        return None
    else:
        list_new[index] = element_to_replace
        print(f'Copy:     {list_new}')
        print(f'Original: {list_}')


replace_element()
