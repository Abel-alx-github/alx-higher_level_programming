#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    combine = set_1.union(set_2)
    for char in set_1:
        if char in set_2:
            combine.remove(char)
    return combine
