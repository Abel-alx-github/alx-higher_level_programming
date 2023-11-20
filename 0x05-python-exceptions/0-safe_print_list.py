#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            count += 1
        if x > count:
            for i in range(count):
                print(my_list[i], end='')
            print()
        else:
            for i in range(x):
                print(my_list[i], end='')
            print()
        return (i + 1)
    except IndexError as err:
        print(err)
