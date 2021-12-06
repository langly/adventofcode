#!/usr/bin/env python3

with open("input.txt") as fh:
    x_max = 0
    y_max = 0
    lines = []

    ## parse the input file and find max dimentions.
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

    ## Now draw the lines onto the board.
    for line in lines:
        (fro, to) = line

        fro  = list(map(lambda x: int(x), fro))
        to   = list(map(lambda x: int(x), to))

        (xFrom, xTo ) = (fro[0], to[0]) if fro[0] < to[0] else (to[0], fro[0])
        (yFrom, yTo ) = (fro[1], to[1]) if fro[1] < to[1] else (to[1], fro[1])

        assert(xFrom <= xTo)
        assert(yFrom <= yTo)

        ## handle the easy case
        if ( xFrom == xTo or yFrom == yTo ):
            for y in range(yFrom, yTo+1):
                for x in range(xFrom, xTo+1):
                    board[y][x] += 1
        else:
            dX = fro[0] - to[0]
            dY = fro[1] - to[1]

            assert(abs(dX) == abs(dY))
            steps = abs(dX) + 1
            x_dir = -1 if dX < 0 else 1
            y_dir = -1 if dY < 0 else 1

            tX = to[0]
            tY = to[1]

            for i in range(steps):
               board[tY][tX] +=1
               tX += x_dir
               tY += y_dir


    total = 0

## Print the board here.
#    for y in range(y_max):
#        for x in range(x_max):
#            print(board[y][x], "", end="")
#            if board[y][x] >= 2:
#                total += 1
#        print()
#
    print(total)
