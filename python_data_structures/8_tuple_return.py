#!/usr/bin/python3


def tuple_return(list_):
    list_len = len(list_)
    if len(list_) == 0:
        first_element = None
    else:
        first_element = list_[0]
    return (list_len, first_element)
