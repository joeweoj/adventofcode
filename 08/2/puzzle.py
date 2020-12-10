#!/usr/bin/env python3

import sys
import time

instructions=[]
instruction_counter=0
executed_instructions={}
accumulator=0

def info():
    print(f"ic:{instruction_counter} ac:{accumulator}")

def acc(arg):
    global instruction_counter
    global accumulator
    executed_instructions[instruction_counter]=instruction_counter
    print(f'acc {arg}')
    accumulator+=arg
    instruction_counter+=1
    info()

def jmp(arg):
    global instruction_counter
    executed_instructions[instruction_counter]=instruction_counter
    print(f'jmp {arg}')
    instruction_counter+=arg
    info()

def nop(arg):
    global instruction_counter
    executed_instructions[instruction_counter]=instruction_counter
    print(f'nop {arg}')
    instruction_counter+=1
    info()

ops = {
    'acc': acc,
    'jmp': jmp,
    'nop': nop
}







def run():
    global instruction_counter
    global executed_instructions
    global accumulator

    # just going to brute force it
    # try each instruction
    # if jmp or nop, swap
    # try executing program
    # if infinite loop, break and try next instruction
    # if not jmp or nop, continue
    for i in instructions:
        print(f"*****running program for {i}")
        # reset
        instruction_counter=0
        executed_instructions={}
        accumulator=0
        original_opcode=i['opcode']


        if i['opcode'] == 'jmp':
            i['opcode'] = 'nop'
        elif i['opcode'] == 'nop':
            i['opcode'] = 'jmp'
        else:
            continue

        while instruction_counter < len(instructions):
            if instruction_counter in executed_instructions:
                print("Infinite Loop! exiting")
                break
            instruction = instructions[instruction_counter]
            op=instruction['opcode']
            arg=int(instruction['arg'])
            ops[op](arg)
            # time.sleep(1)

        # reset instruction
        i['opcode'] = original_opcode

        # success condition
        if instruction_counter not in executed_instructions:
            print("Completed!!!!!")
            print(f"Accumulator: {accumulator}")
            break




with open(sys.argv[1], 'r') as f:
    for line in f:
        line=line.rstrip('\n').split(' ')
        instructions.append({'opcode':line[0], 'arg': line[1]})
        print(line)
    print('-------------')

run()
