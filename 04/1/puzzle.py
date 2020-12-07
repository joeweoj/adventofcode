#!/usr/bin/env python3

import sys


def is_valid_passport(passport):
    expected=set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    return expected.issubset(passport.keys())



# read file in
i=0
passports={}
# this is all pretty shonky :/
with open(sys.argv[1], 'r') as f:
    # transform input into passport dicts
    for line in f:
        # split on empty line
        if line == '\n':
            i=i+1
            continue

        # get existing or new pp
        pp=passports[i] if i in passports else {}
        # split into kv fieldss
        for field in [l.rstrip('\n') for l in line.split(' ')]:
            kv=field.split(':')
            pp[kv[0]] = kv[1]

        # upsert passport
        passports[i]=pp



valid=0
for k,v in passports.items():
    print("{}".format(v), end='')
    if is_valid_passport(v):
        valid=valid+1
        print(" Valid!")
    else:
        print(' Invalid')

print("Valid: {}".format(valid))
