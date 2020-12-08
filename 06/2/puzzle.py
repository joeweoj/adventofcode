#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:

    # questions answered 'yes' a-z, per line
    # groups separated by empty line
    # need to find which questions *everyone* answered in a group
    # sum the counts of each group

    # each group needs to be a list of sets
    # then once collated, can do an intersection on each group's sets
    groups=[[]]
    g=0
    for line in f:
        line=line.rstrip('\n')
        print(line)
        if line == '':
            g=g+1
            groups.append([])
            continue;

        groups[g].append(set([c for c in line]))

    intersected=[set.intersection(*g) for g in groups]

    print("Groups: {}".format(groups))
    print("Intersected: {}".format(intersected))
    print("Sizes: {}".format([len(g) for g in intersected]))
    print("Sum: {}".format(sum([len(g) for g in intersected])))
