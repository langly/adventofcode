#!/usr/bin/env python3

d = {'A': 0, 'B': 1, 'C':2, 
     'X': 0, 'Y': 1, 'Z':2}

with open("input.txt") as fh:
    points = 0

    for line in fh:
        line = line.strip().split()

        ## Bias here to let the if work later
        line = list(map(lambda x: d[x], line))
        points += line[1] + 1

        if ( (line[0] + 1)%3 == line[1] ):
            points += 6
        elif (line[0] == line[1]):
            points += 3


print(points)
