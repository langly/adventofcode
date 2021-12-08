#!/usr/bin/env python3
from math import ceil,floor

## Gave up on solving this mathematically, although there should be a solution there as well. 

def intSeq(n):
    return int(n*(n+1) / 2)

with open("input.txt") as fh:
    levels = []
    for line in fh: 
        levels += map(lambda x: int(x),line.strip().split(","))

    levels.sort()


    best = float('inf')
    for move in range(min(levels),max(levels)+1):
        cost = 0 
        for n in levels:
            n = abs(n-move)
            cost += intSeq(n)

        best = min(cost,best)

    print(best)

