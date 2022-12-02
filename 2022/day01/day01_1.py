#!/usr/bin/env python3

### This is a bit slow, can include the max into the first loop..
with open("input.txt") as fh:
    cnt = 0
    arr = []
    for line in fh: 
        line = line.strip()

        if ( len(line) == 0 ):
            arr.append(cnt)
            cnt = 0
        else:
            cnt += int(line)
    ## We want the last one as well
    arr.append(cnt)
        
print( max(arr))
