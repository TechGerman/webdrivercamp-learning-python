#!/usr/bin/python3

def calc_weight(list_=[]):
    result = []
    for tuple_ in list_:
        for x, y in tuple_:
            result.append(x*y)
    if len(list_) == 0:
        return 0
    else:
        return result



if __name__ == "__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
