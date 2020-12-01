#!/usr/bin/env python3

import sys, os

# read numbers in from file
numbers=[]
with open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt', 'r') as f:
    for line in f:
        numbers.append(int(line))

# iterate through list
# find 2x entries that added together == 2020
# multiply together

for i in numbers:
    for j in numbers:
        if i + j == 2020:
            print("{} + {} == {}".format(i, j, i + j))
            print("{} * {} == {}".format(i, j, i * j))
            sys.exit(0)
