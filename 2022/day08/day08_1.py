#!/usr/bin/env python3

import numpy as np

forrest = []

def isTallest(l,val):
    lst = list((filter(lambda x: x >= val,l)))
    res = len(lst) ==0
    return res


## Just get the text file into an 2D array to play with
with open("input.txt") as fh:
    for line in fh: 
        line = line.strip()
        s = [ int(x) for x in line]
        forrest.append(s)

array = np.array(forrest)

sY, sX = array.shape

interior = 0

for y in range(1, sY-1):
    for x in range(1, sX-1):
        height = array[y,x]
        row = array[y,:]
        col = array[:,x]

        tall = (isTallest(row[:x], height) or 
                isTallest(row[x+1:], height) or 
                isTallest(col[:y], height) or 
                isTallest(col[y+1:], height))

        if tall:
            interior += 1 

exterior = 2*sX + 2*sY -4

print(exterior, interior, exterior+interior)
