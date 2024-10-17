#!/usr/bin/python3

def only_unique(list_=[]):
    sum_of_unique = 0
    unique = []
    for i in list_:
        if i not in unique:
            unique.append(i)
            sum_of_unique += i
        else:
            continue
    return sum_of_unique


if __name__ == "__main__":
    list_ = [0, 1, 6, 3, 6, 4, 0, 2, 5, 4, 4]
    result = only_unique(list_)
    print(f"Sum of unique: {result}")
