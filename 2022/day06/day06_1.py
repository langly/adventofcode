#!/usr/bin/env python3

with open("input.txt") as fh: 
    char = 0
    arr = []
    while c := fh.read(1):
        if len(arr) == 4:
            arr.pop(0)
            
        arr.append(c)
        char += 1 

        print(arr)

        ## Do stuff.
        found = False
        if len(arr) == 4:
            for z, i in enumerate(arr):
                if i in arr[z+1:]:
                    found = True
                    break

        if not found and len(arr) ==4:
            print(arr)
            print("Found something at ", char)
            break
                

        assert(len(arr) <= 4)
