#!/usr/bin/env python3
#
# This is the brute force approach to the problem...
# More time would allow for a slightly better algorithmic approach
#
# However, allows for some playing around with numpy :D
# 

import numpy as np

forrest = []

def viewDistance(lst, val):
    lst = list(lst)

    distance = 0
    for l in lst:
        distance += 1
        if l >= val:
            break

    return distance
        
## Just get the text file into an 2D array to play with
with open("input.txt") as fh:
    for line in fh: 
        line = line.strip()
        s = [ int(x) for x in line]
        forrest.append(s)

array = np.array(forrest)

sY, sX = array.shape

interior = 0

mx = 0

for l in forrest:
    print(*l)
print()

for y in range(1, sY-1):
    for x in range(1, sX-1):
        height = array[y,x]
        row = array[y,:]
        col = array[:,x]

        dist = ( viewDistance(np.flip(row[:x]), height) *
               viewDistance(row[x+1:], height) *
               viewDistance(np.flip(col[:y]), height) * 
               viewDistance(col[y+1:], height) )

        mx = max(dist,mx)


print(mx)
