#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:

    # questions answered 'yes' a-z, per line
    # groups separated by empty line
    # use a set to capture duplicate answers per group
    # sum the counts of each group
    groups=[set()]
    g=0
    for line in f:
        line=line.rstrip('\n')
        if line == '':
            g=g+1
            groups.append(set())
        else:
            groups[g].update([c for c in line])

    group_sizes=[len(s) for s in groups]

    # print("Groups: {}".format(groups))
    # print("Sizes: {}".format(group_sizes))
    print("Sum: {}".format(sum(group_sizes)))
