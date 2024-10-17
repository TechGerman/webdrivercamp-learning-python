#!/usr/bin/python3
def not_common_elements(a, b):
    not_common_elements = []
    for i in a:
        if i not in b:
            not_common_elements.append(i)
        else:
            continue
    for i in b:
        if i not in a:
            not_common_elements.append(i)
        else:
            continue
    return not_common_elements


if __name__ == "__main__":
    set_a = {"API", "requests", "Selenium", "Python", "Behave"}
    set_b = {"Selenium", "Java", "Cucumber", "Maven", "API"}
    elements = not_common_elements(set_a, set_b)
    [print(x) for x in sorted(list(elements))]
