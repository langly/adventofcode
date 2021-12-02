#!/usr/bin/env python3

with open("input.txt") as fh: 
    depth = 0
    fwd = 0

    for line in fh: 
        (c,v) = line.strip().split()
        v = int(v)

        if c == "forward":
            fwd += v
        elif c == "down": 
            depth += v
        elif c == "up": 
            depth -= v
        else: 
            printf("Ops")

        #print(c,v)
    print(depth, fwd)
    print(depth*fwd)

