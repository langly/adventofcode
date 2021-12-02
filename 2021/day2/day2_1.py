#!/usr/bin/env python3

with open("input.txt") as fh: 
    aim = 0
    fwd = 0
    depth = 0

    for line in fh: 
        (c,v) = line.strip().split()
        v = int(v)

        if c == "forward":
            fwd += v
            depth += v * aim
        elif c == "down": 
            aim += v
        elif c == "up": 
            aim -= v
        else: 
            printf("Ops")

    print(depth, fwd)
    print(depth*fwd)

