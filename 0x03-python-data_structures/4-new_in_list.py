#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    if idx >= length or idx < 0:
        return my_list
    for i in range(length):
        if i == idx:
            my_list[i] = element
            return my_list
