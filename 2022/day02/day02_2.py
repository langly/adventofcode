#!/usr/bin/env python3

d = {'A': 1, 'B': 2, 'C':3, 
     'X': 1, 'Y': 2, 'Z':3}

with open("input.txt") as fh:
    points = 0

    for line in fh:
        line = line.strip().split()

        ## Bias here to let the if work later
        line = list(map(lambda x: d[x]-1, line))

        opp = line[0]

        ## X loss
        ## Y draw
        ## Z win
        x = 0
        if ( line[1] == 0 ):
            ## Loss
            x = (opp - 1) %3 
        elif ( line[1] == 1 ):
            ## Draw
            x = opp
            points += 3
        else:
            ## Win
            points += 6
            x = (opp + 1) %3 

        points += x +1


print(points)
