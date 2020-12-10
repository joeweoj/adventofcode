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
    while instruction_counter not in executed_instructions:
        instruction = instructions[instruction_counter]
        op=instruction['opcode']
        arg=int(instruction['arg'])
        ops[op](arg)
        # time.sleep(1)

    print(f"Accumulator: {accumulator}")




with open(sys.argv[1], 'r') as f:
    for line in f:
        line=line.rstrip('\n').split(' ')
        instructions.append({'opcode':line[0], 'arg': line[1]})
        print(line)
    print('-------------')

run()
