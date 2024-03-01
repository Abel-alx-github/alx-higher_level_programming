#!/usr/bin/python3
# find the pick from the given list

def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    high = len(list_of_integers)
    if high == 1:
        return list_of_integers[0]
    if high == 2:
        return max(list_of_integers)

    mid = high // 2
    if ((list_of_integers[mid] > list_of_integers[mid - 1]) and
       (list_of_integers[mid] > list_of_integers[mid + 1])):
        return list_of_integers[mid]
    elif list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])

    return None
