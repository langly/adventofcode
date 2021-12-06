#!/usr/bin/env python3

fishes = []

with open("input.txt") as fh:
    for line in fh:
        fishes += list(map(lambda x: int(x), line.split(",")))

    print(line)


days = 80
for day in range(days):
    ## To avoid double count
    new_fish = []
    for x in range(len(fishes)):
        if fishes[x] == 0:
            fishes[x] = 6
            new_fish.append(8)
        else:
            fishes[x] -= 1

    fishes += new_fish
    print(day, fishes)

print(len(fishes))


