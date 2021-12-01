#!/usr/bin/env python3

with open("input.txt") as fh:
    lines = fh.readlines()

    cnt = 0 

    for (idx,line) in enumerate(lines[1:]):
        l = int(line.strip())
        p = int(lines[idx].strip())

        if l > p: 
            cnt += 1 

        print(idx, line)

    print(cnt)
