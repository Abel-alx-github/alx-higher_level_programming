#!/usr/bin/python3
def remove_char_at(string, n):
    length = len(string)
    new_string = ""
    for i in range(length):
        if i == n:
            continue
        else:
            new_string += string[i]
    return new_string
