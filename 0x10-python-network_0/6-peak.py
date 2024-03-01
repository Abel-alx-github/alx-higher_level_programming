#!/usr/bin/python3
#find the pick from the given list

def find_peak(list_of_integers):
  if list_of_integers is None:
    return None
  if list_of_integers:
    return max(list_of_integers)
