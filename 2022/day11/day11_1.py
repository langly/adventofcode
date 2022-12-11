#!/usr/bin/env python3

class Monkey:
    def __init__(self):
        self.ident          = None
        self.items          = None
        self.operation      = None
        self.test           = None
        self.action_true    = None
        self.action_false   = None
        self.inspected      = 0

    def __str__(self):
        return "Monkey: "+" "+ str(self.ident) +" "+ str(self.operation)+" "+ str(self.test)+" "+ str(self.action_true)+" "+ str(self.action_false)+" "+ str(self.items)

    def act(self):
        old_list = self.items

        redistribute = []
        self.items = []

        for item in old_list:
            self.inspected += 1
            new = 0
            old = item
            s = self.operation.split("=")[1]
            new =  eval(s)
            bored = int(new/3)

            if bored % self.test == 0: 
                redistribute.append (( int(self.action_true), bored ))
            else: 
                redistribute.append (( int(self.action_false), bored ))


        return redistribute
    
monkeys = []

## First parse the input file into an array of monkeys
with open("input.txt") as fh:

    state = 0
    cur_monkey = None

    for line in fh:
        line = line.strip()

        ## Ignore blank lines
        if len(line) == 0:
            continue

        if state == 0:
            cur_monkey = Monkey()
            cur_monkey.ident = int(line.split()[1][:-1])
            state +=1 
        elif state == 1:
            s = [int(x) for x in line.split(":")[1].split(",")]
            cur_monkey.items = s
            state +=1 
        elif state == 2:
            cur_monkey.operation = line.split(":")[1]
            state +=1 
        elif state == 3:
            cur_monkey.test =  (int(line.split()[-1]))
            state +=1 
        elif state == 4:
            cur_monkey.action_true = line.split()[-1]
            state +=1 
        elif state == 5:
            cur_monkey.action_false = line.split()[-1]
            monkeys.append(cur_monkey)
            state  = 0

## 20 Rounds
for r in range(20):
    for m in monkeys:
        redistribute = m.act()
        for (target,v) in redistribute:
            monkeys[target].items.append(v)

inspected = []
for m in monkeys:
   inspected.append(m.inspected) 

from functools import reduce
inspected.sort()
print(reduce(lambda a,b: a*b, inspected[-2:]))
