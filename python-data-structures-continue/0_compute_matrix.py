#!/usr/bin/python3

def compute_matrix(matrix=[]):
    result = []
    for i in matrix:
        result.append(list(map(lambda x: x**2, i)))
    return result


if __name__ == "__main__":
    matrix = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
    print(f"Original: {matrix}")
    print(f"Modified: {compute_matrix(matrix)}")
