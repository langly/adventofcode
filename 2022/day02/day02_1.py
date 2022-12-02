#!/usr/bin/env python3

d = {'A': 1, 'B': 2, 'C':3, 
     'X': 1, 'Y': 2, 'Z':3}

with open("input.txt") as fh:
    points = 0

    for line in fh:
        line = line.strip().split()

        ## Bias here to let the if work later
        line = list(map(lambda x: d[x]-1, line))
        points += line[1] + 1

        if ( (line[0] + 1)%3 == line[1] ):
            points += 6
        elif (line[0] == line[1]):
            points += 3


print(points)
