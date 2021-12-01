#!/usr/bin/env python3
##########################
#
# Simple brute force approach on this one. Could probably do better
# with some graph theory. I could also reduce the number of combinations
# I try...
#
##########################

program = []

def runProgram(minPC):
    pc  = 0
    acc = 0

    ## Reset the visited state.
    for i in range(len(program)):
        program[i][0] = 0

    while True:
        ## We have terminated the program by reaching the end of the boot loader section
        if pc == len(program):
            print(acc)
            return True

        visited, op, imm = program[pc]

        if ( minPC == pc ):
            if ( op == 'jmp' ):
                op = 'nop'
            elif ( op == 'nop' ):
                op == 'jmp'

        if visited == 1:
            return False

        program[pc][0] = 1

        if op == "jmp":
            pc = pc + int(imm)
            continue
        elif op  == "acc":
            acc = acc + int(imm)

        pc = pc + 1

with open("input.txt") as fh:
    for line in fh:
        line = line.strip()

        op = line.split()

        program.append( [0] + op )


for i in range(len(program)):
    v = runProgram(i)
    if ( v ):
        print("Found")
