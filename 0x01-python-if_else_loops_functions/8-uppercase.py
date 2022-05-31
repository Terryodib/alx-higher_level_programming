#!/usr/bin/python3
def uppercase(str):
    letter = ""
    for i in str:
        c = ord(i)
        if ord('a') <= c <= ord('z'):
            c -= 32
        letter += chr(c)
    print("{}".format(letter))
