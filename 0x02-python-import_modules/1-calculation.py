#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    a = 10
    b = 5
    a_plus_b = add(a, b)
    a_minus_b = sub(a, b)
    a_times_b = mul(a, b)
    a_divide_b = div(a, b)
    print("{} + {} = {}".format(a, b, a_plus_b))
    print("{} - {} = {}".format(a, b, a_minus_b))
    print("{} * {} = {}".format(a, b, a_times_b))
    print("{} / {} = {}".format(a, b, a_divide_b))
