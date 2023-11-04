#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        length = len(my_list) - 1
        if idx > length or idx < 0:
            cp_list = my_list.copy()
            return cp_list
        for i in range(length + 1):
            if i == idx:
                new_list = list(my_list)
                new_list[i] = element
                return new_list
