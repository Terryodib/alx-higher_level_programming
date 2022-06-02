#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    summ = add(a, b)
    sub = sub(a, b)
    mul = mul(a, b)
    div = div(a, b)
    print("{} + {} = {}".format(a, b, summ))
    print("{} - {} = {}".format(a, b, sub))
    print("{} * {} = {}".format(a, b, mul))
    print("{} / {} = {}".format(a, b, div))
