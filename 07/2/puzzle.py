#!/usr/bin/env python3

import sys
import re
import pprint

# parse each line; split by , then regex to get bag colour
# dict of each bag colour -> [contained bag colour, ]

# for given input (bag colour)
# 1. lookup the root bag
# 2. recursively count down all contained bags
# 3. sum up the counts



def contains_count(bag):
    """
    return contained bags count
    """
    total=0
    for b in bags_dict[bag]:
        bcount=b['count']
        # add number of this bag type
        total += bcount

        # add number of this bag type * child bags
        contains=contains_count(b['colour'])
        total += (bcount * contains)

    print(f'{bag} contains {bags_dict[bag]} with a total of {total} bags')
    return total



bags_dict={}
with open(sys.argv[1], 'r') as f:
    for line in f:
        # ewww, but my regex is awful
        line=line.rstrip('\n').replace('contain no other bags.', '')
        matches = re.finditer(r"(\d?)([a-z ]*)(bag[s]?)", line)
        m=next(matches)
        bag_colour=m.group(2).strip()
        bags_dict[bag_colour] = [{'colour': m.group(2).strip(), 'count': int(m.group(1))} for m in matches]


pprint.pprint(bags_dict)


# count total bags contained
print(contains_count('shiny gold'))
