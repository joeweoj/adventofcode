#!/usr/bin/env python3

import sys
from functools import reduce

# slopes
slopes=[[1,1], [3,1], [5,1], [7,1], [1,2]]

# read file in
with open(sys.argv[1], 'r') as f:
    rows=[l.rstrip('\n') for l in f.readlines()]

def is_tree(line, col):
    """
    need to loop round line, if index > len(line) i.e. modulo
    look at line[col]
    if '#' return true,
    otherwise return false
    """
    mcol=col % len(line)
    char=line[mcol]
    print("{} : {}({}) = {} {}".format(line, col, mcol, char, ('tree!' if char == '#' else '')))
    if char == '#':
        return True
    else:
        return False

def traverse_slope(right, down):
    print("Traversing slope: {}:{}".format(right, down))
    row=down
    col=right
    trees=0
    while row < len(rows):
        if is_tree(rows[row], col):
            trees = trees + 1
        row = row + down
        col = col + right
    return trees

slope_trees=[]
for s in slopes:
    trees=traverse_slope(s[0], s[1])
    slope_trees.append(trees)
    print("Trees: {}".format(trees))

print("Product: {}".format(reduce(lambda x, y: x*y, slope_trees)))
