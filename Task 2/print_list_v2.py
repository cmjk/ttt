from typing import List


def print_list(a_list: List) -> None:
    for index, item in enumerate(a_list):
        print(f'Element {index + 1} = {item}')


l = [1, 2, 3, 5, 7, 9]
print_list(l)
