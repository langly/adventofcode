#!/usr/bin/env python3

lines = [ None ] * 9


### Painfully parse the initial stack
def parseLine(line):
    for n,c in enumerate(line):
        if  c.isalpha(): 
            q = int(n / 4)
            if not lines[q]: 
                lines[q] = []

            lines[q].append(c)

with open("input.txt") as fh:
    for line in fh: 

        if line.strip().startswith("["):
            parseLine(line)

        line = line.strip()

        if line.startswith("move"):
            s = line.split()
            cnt,fm,to = int(s[1]),int(s[3])-1,int(s[5])-1

            a = lines[fm][:cnt]
            a.reverse()

            lines[fm] = lines[fm][cnt:]
            lines[to] = a + lines[to]


## Output the answer
    s = ""
    for l in lines: 
        s += l[0]

    print(s)
