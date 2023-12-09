#!/usr/bin/env python3

from math import pow

with open('input.txt') as fh:
    sum = 0
    for line in fh:
        line = line.strip()

        (winning,mine) = [x.strip() for x in line.split(":")[1].split("|")]

        winning = [x for x in winning.split(" ") if len(x) > 0]
        mine    = [x for x in mine.split(" ") if len(x) > 0]

        res = [0] * len(winning)
        w = dict(zip(winning,res))

        l = [ x for x in mine if x in w]

        d = pow(2, len(l)-1) if len(l) > 0 else 0
        sum += d

    print(int(sum))
