#!/usr/bin/env python3

res =[]

with open("input.txt") as fh:
    acc = 1
    cycle = 1

    for line in fh:
        line = line.strip()

        s = line.split()

        print(cycle, acc, line)

        cycle += 1
        if ( cycle == 20 ) or ( (cycle-20) %40 ==0):
            print("\t", cycle, acc)
            res.append(acc*cycle)

        ## We have an add instruction consuming two cycles
        if len(s) == 2:
            acc += int(s[1])
            cycle += 1
            if ( cycle == 20 ) or ( (cycle-20) %40 == 0):
                print("\t",cycle, acc, s[1])
                res.append(acc*cycle)

        
print(sum(res))
