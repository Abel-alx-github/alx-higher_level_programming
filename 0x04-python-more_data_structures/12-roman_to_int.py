#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    dic_key_value = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    length = len(roman_string) - 1
    intger = 0
    for i in range(length, -1, -1):
        last_r = dic_key_value[roman_string[i]]
        if i < length and last_r < dic_key_value[roman_string[i + 1]]:
            intger -= last_r
        else:
            intger += last_r
    return intger
