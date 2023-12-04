#!/usr/bin/env python3

input = []

with open("input.txt") as fh:
    linenum = None

    for line in fh:
        line = line.strip()
        if not linenum:
            ## Pad the input matrix with ..
            linenum = len(line)
            foo = "".join(['.'] * (linenum+2))
            input.append(foo)

        input.append("."+line+".")

    ## Pad the input matrix with ..
    foo = "".join(['.'] * (linenum+2))
    input.append(foo)

for l in input:
    print(l)

## Now go look for the numbers.
sum = 0

for y in range(1,len(input)-1):
    number = []

    for x in range(1,len(input[0])-1):
        current = input[y][x]
        next = input[y][x+1]

        if current.isdigit():
            number.append(current)

        if ( not next.isdigit() or (x+1 == len(input[0])-1 )):
            n = "".join(number)
            if len(n) > 0:
                border = []
                min_x = x-len(n)
                max_x = x+1

                border += input[y][min_x]
                border += input[y][max_x]
                border += input[y-1][min_x:max_x+1]
                border += input[y+1][min_x:max_x+1]

                l = [ x for x in border if not x == "." ]
                if len(l) > 0:
                    sum += int(n)

                number = []

print(sum)
