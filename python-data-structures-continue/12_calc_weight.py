#!/usr/bin/python3

def calc_weight(list_=[]):
    multiply = sum(map(lambda x: x[0] * x[1], list_))
    sum_ = sum(map(lambda x: x[1], list_))
    if len(list_) == 0:
        return 0
    else:
        return multiply/sum_


if __name__ == "__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
