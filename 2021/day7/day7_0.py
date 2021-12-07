#!/usr/bin/env python3

with open("input.txt") as fh:
    levels = []
    for line in fh: 
        levels += map(lambda x: int(x),line.strip().split(","))

    levels.sort()
    elm = int(len(levels)/2)

    median = levels[elm]
    l = list(map(lambda x: abs(x-median), levels))
    print(sum(l))
