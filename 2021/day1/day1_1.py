#!/usr/bin/env python3

## Correct is 1344

with open("input.txt") as fh:
    lines = fh.readlines()

    lines = list(map( lambda x: int(x), lines))

    window_size = 3

    foo = []

    for l in range(len(lines)-2): 
        l = lines[l : l + window_size]
        s = sum(l)
        foo.append(s)


    ## Sum it up
    cnt = 0 
    
    for i in range(len(foo)-1):
        l = foo[i]
        n = foo[i+1]
    
        if l < n: 
            cnt += 1 
    
    print(cnt)
