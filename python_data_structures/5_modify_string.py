#!/usr/bin/python3

string = """AbraCadabra
A new string voila!"""
some_string = ""


def remove_char(some_string):
    for i in string:
        if i != 'A' and i != 'a':
            some_string += i
    print(some_string)


remove_char(some_string)
