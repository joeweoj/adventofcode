#!/usr/bin/env python3

import sys

def is_tree(line, row, col):
    """
    need to loop round line, if index > len(line) i.e. modulo
    look at line[col]
    if '#' return true,
    otherwise return false
    """
    mcol=col % len(line)
    char=line[mcol]
    print("{} : len={} {}:{}({}) = {}".format(line, len(line), row, col, mcol, char))
    if char == '#':
        return True
    else:
        return False




col=0
trees=0
with open(sys.argv[1], 'r') as f:
    for row, line in enumerate(f):
        if row == 0:
            continue

        col = col + 3

        if is_tree(line.rstrip('\n'), row, col):
            trees = trees + 1


print("Trees: {}".format(trees))
