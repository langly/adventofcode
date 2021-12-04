#!/usr/bin/env python3

## This one calculates both part 0 and 1 in the same go.

def parseBoard(board, numbers):
    ## Sum the board
    board_sum = 0
    b = []

    for row in board:
        f = []
        for r in row.split():
            r = int(r)
            f.append(r)
            board_sum += r
        b.append(f)

    h = len(b)
    w = len(b[0])

    bT = [ [0]*h for i in range(w)]

    ## Transpose the board
    for x in range(h):
        for y in range(w):
            bT[x][y] = b[y][x]

    for (idx,number) in enumerate(numbers):
        found = False
        done  = False

        for row in b:
            if number in row:
                row.remove(number)
                done |= len(row) == 0
                found = True

        for row in bT:
            if number in row:
                row.remove(number)
                done |= len(row) == 0
                found = True

        if found:
            board_sum -= number

        if done:
            return (idx, board_sum*number)

with open("input.txt") as fh:
    numbers = list(map(lambda x: int(x),fh.readline().split(",")))
    fh.readline()

    a = []
    res = []

    for line in fh:
        line = line.strip()

        if len(line) == 0:
            (num, s) = parseBoard(a, numbers)
            res.append((num,s))
            a = []
        else:
            a.append(line)

    (num, s) = parseBoard(a, numbers)
    res.append((num,s))

    winners = sorted(res, key=lambda x: x[0])
    print("Part one:", winners[0][1])
    print("Part two:", winners[-1][1])
