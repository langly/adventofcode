#!/usr/bin/env python3

with open("input.txt") as fh:

    ## To lazy, so finding max dimensions first
    x_max = 0
    y_max = 0

    lines = []

    for l in fh:
        (fro, to) = l.split("->")
        fro = fro.strip().split(",")
        to  = to.strip().split(",")

        lines.append((fro,to))

        l = [int(fro[0]), int(to[0]), x_max]
        x_max = max(l)
        y_max = max([int(fro[1]), int(to[1]), y_max])

    x_max += 1
    y_max += 1

    board = [ [0]*x_max for x in range(y_max) ]

    for line in lines:
        (fro, to) = line

        if ( fro[0] == to[0] or fro[1] == to[1] ):
            (xFrom, xTo ) = (fro[0], to[0]) if int(fro[0]) < int(to[0]) else (to[0], fro[0])
            (yFrom, yTo ) = (fro[1], to[1]) if int(fro[1]) < int(to[1]) else (to[1], fro[1])

            xFrom = int(xFrom)
            xTo = int(xTo)
            yFrom = int(yFrom)
            yTo = int(yTo)

            assert(xFrom <= xTo)
            assert(yFrom <= yTo)

            for y in range(yFrom, yTo+1):
                for x in range(xFrom, xTo+1):
                    board[y][x] += 1

    total = 0
    for y in range(y_max):
        for x in range(x_max):
            if board[y][x] >= 2:
                total += 1

    print(total)
