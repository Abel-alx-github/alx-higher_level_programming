#!/usr/bin/python3
def remove_char_at(str, n):
    while (str[n]):
        str[n] = str[n + 1]
        n +=1
print(f"{str}")
