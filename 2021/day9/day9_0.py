#!/usr/bin/env python3

m = []
with open("input.txt") as fh:

    for line in fh:
        tmp = []
        for n in line.strip(): 
           tmp.append(int(n))
        m.append(tmp)


print(m)

h = len(m)
w = len(m[0])

s = []
l = [(1,0),(0,1),(-1,0),(0,-1)]

for y in range(h):
    for x in range(w):
        me = m[y][x]
        fnord = []

        for pos in l:
            (i,j) = pos
            tY = y - i 
            tX = x - j 

            if (tX < 0 or tY < 0 or 
                (tX >= w  or tY >= h ) or
                (i == 0 and j == 0)) :
                continue

            fnord.append(m[tY][tX])

        foo = min(fnord)
        if foo > me:
            s.append(me+1)

print(sum(s))

