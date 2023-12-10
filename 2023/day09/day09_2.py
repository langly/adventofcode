#!/usr/bin/env python3

import numpy as np

input = []

with open('input.txt') as fh:
    for line in fh:
        line = line.strip()
        x = [ int(x.strip()) for x in line.split(" ") ]
        input.append(x)

def find_compressed(i, end:bool):

    a = np.diff(i)

    cnt = np.count_nonzero(a)
    index = -1 if end else 0

    if cnt != 0:
        return a[index] + find_compressed(a,end)
    else:
        return 0


e = []
f = []

for i in input:
    n = np.array(i)
    bar = find_compressed(n,True)

    e.append(n[-1] + bar)

    ## Now do the reverse
    n = np.flip(n)

    f.append(n[-1] + find_compressed(n,True))

print("End", sum(e))
print("Front",sum(f))
