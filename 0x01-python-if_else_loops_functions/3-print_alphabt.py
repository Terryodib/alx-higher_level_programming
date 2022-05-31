#!/usr/bin/python3
for chr in "abcdefghijklmnopqrstuvwxyz":
    if chr == "q" or chr == "e":
        continue
    print('{}'.format(chr), end="")
