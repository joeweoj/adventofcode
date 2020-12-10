#!/usr/bin/env python3

import sys
import re
import pprint

# parse each line; split by , then regex to get bag colour
# dict of each bag colour -> [contained bag colour, ]

# for given input (bag colour)
# 1. iterate over each dict key
# 2. if matches input, contain_counter++
# 3. recursively traverse dict value list (containers bags),
#    by looking up key, then #3...
# 4. if match found, contain_counter++


def contains(bags, criteria):
    # iterate through bags and see if there's a match
    found=False
    for b in bags:
        colour=b['colour']
        if colour == criteria:
            print(f'{colour} matches {criteria}!!!!')
            found=True
        else:
            print(f'{colour} does not match {criteria}...')
            found=contains(bags_dict[colour], criteria)

        if found: break

    return found

bags_dict={}
with open(sys.argv[1], 'r') as f:
    for line in f:
        # ewww, but my regex is awful
        line=line.rstrip('\n').replace('contain no other bags.', '')

        matches = re.finditer(r"(\d?)([a-z ]*)(bag[s]?)", line)
        m=next(matches)
        bag_colour=m.group(2).strip()
        bags_dict[bag_colour] = [{'colour': m.group(2).strip(), 'count': int(m.group(1))} for m in matches]


# pprint.pprint(bags_dict)

bag_to_find='shiny gold'
valid_bags=[]

for k,v in bags_dict.items():
    print('-----------------')
    # ignore if bag key matches criteria
    if bag_to_find == k:
        print(f'{k} matches {bag_to_find}!!!!')
        continue
    else:
        print(f'{k} does not match {bag_to_find}')


    if contains(v, bag_to_find):
        valid_bags.append(k)


print('**************')
pprint.pprint(valid_bags)
print(f'Size: {len(valid_bags)}')
