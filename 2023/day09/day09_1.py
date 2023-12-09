#!/usr/bin/env python3

import numpy as np

input = []

with open('input.txt') as fh:
    for line in fh:
        line = line.strip()
        x = [ int(x.strip()) for x in line.split(" ") ]
        input.append(x)

def find_compressed(i):

    a = np.diff(i)

    cnt = np.count_nonzero(a)
    print(a)

    if cnt != 0:
        return a[-1] + find_compressed(a)
    else:
        return 0


s = []

for i in input:
    print(i)
    n = np.array(i)
    s.append(n[-1] + find_compressed(n))

print(sum(s))
