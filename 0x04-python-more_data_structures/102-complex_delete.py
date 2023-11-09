#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    else:
        new_dic = {key: val for key, val in a_dictionary.items()
                   if val != value}
        return new_dic
