#!/usr/bin/env python3

lmt = 100000
fnord = 0
sizes = []

class Entry:
    def __init__(self, parent):
        self.parent = parent
        self.children = {}
        self.isdir = True
        self.size = -1  ## Size of -1 means directory

    def printOut(self,indent):
        for (k,v) in self.children.items():
            print("  "*indent, k,v.isdir, v.size)
            v.printOut(indent+1)

    def calculateSize(self):
        global fnord
        size = 0
        for k,v in self.children.items():
            if v.isdir == True:
                v.calculateSize()

            size += int(v.size)

        if size < lmt:
            fnord += size

        self.size = size
        sizes.append(size)
        return self.size


root = Entry(None)
cwd = None


def handleCommand(cmd):
    global root
    global cwd

    s = cmd.split()

    if ( s[0] == 'cd' and s[1] == ".." ):
        cwd = cwd.parent
    elif ( s[0] == 'cd' and s[1] == "/"):
        cwd = root
    elif ( s[0] == 'cd'): ## Normal CD here.. 
        if not s[1] in cwd.children:
            cwd.children[s[1]] = Entry(cwd)
        cwd = cwd.children[s[1]]

def handleLS(line):
    size,name = line.split()

    if ( size.isnumeric() ):
        cwd.children[name] = Entry(cwd)
        cwd.children[name].size = size
        cwd.children[name].isdir = False
    else: 
        if not name in cwd.children:
            cwd.children[name] = Entry(cwd)
    

with open("input.txt") as fh: 
    for line in fh:
        if line.startswith("$"):
            handleCommand(line[2:])
        else: 
            handleLS(line)

root.printOut(0)
root.calculateSize()

total = 70000000
free  = 30000000

remove = free - (total - root.size)
sizes.sort()

for s in sizes: 
    if  s > remove:
        print(s)
        break
