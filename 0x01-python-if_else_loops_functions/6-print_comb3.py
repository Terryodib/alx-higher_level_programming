#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        endd = ", " if int(str(i) + str(j)) < 89 else "\n"
        print("{}{}".format(i, j), end=endd)
