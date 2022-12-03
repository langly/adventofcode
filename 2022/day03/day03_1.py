#!/usr/bin/env python3

with open("input.txt") as fh: 
    s = 0

    for line in fh: 
        line = line.strip()
        splitat = int(len(line)/2)
        l,r = line[:splitat], line[splitat:]
        assert(len(l)+len(r) == len(line))

        r = set(filter(lambda x: x in r, l))
        f = list(map(lambda x: ord(x)-ord('a'), r))
        f = list(map(lambda x: x+1 if x>=0 else x + 32+26+1,f))

        s += sum(f)

    print(s)
