#!/usr/bin/env python3

def contained(r,l):
    con =  (r[0] <= l[0]) and (r[1] >= l[0])
    return con


with open("input.txt") as fh:
    sum = 0
    for line in fh:
        line = line.strip()
        s = line.split(",")

        r = list(map(lambda x: int(x),s[0].split("-")))
        l = list(map(lambda x: int(x),s[1].split("-")))

        b = contained(r,l) or  contained(l,r)
        if b == True: 
            sum += 1

    print(sum)
