#!/usr/bin/env python3

with open("input.txt") as fh: 
    cnt = [0] * 12
    total = 0

    for line in fh:
        l = line.strip()
        total += 1

        for (idx,n) in enumerate(l):
            cnt[idx] += int(n)

        
    l = map( lambda x: str(1) if (x > total/2 ) else str(0), cnt)
    mask = ( 2^11) -1
    gamma = int("".join(l), 2)
    eps = (~gamma) & mask

    print(gamma*eps)
