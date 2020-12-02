#!/usr/bin/env python3

import sys


def is_valid(bounds, character, password):
    return bounds[0] <= password.count(character) <= bounds[1]

valid=0

with open(sys.argv[1], 'r') as f:
    for line in f:
        # 3-11 z: zzzzzdzzzzlzz
        # split into parts; <range> <required character> <password>

        # range
        parts = line.rstrip('\n').split(' ')
        range = [int(p) for p in parts[0].split('-')]

        # required char (ignore :)
        character = parts[1][0]

        # password
        password = parts[2]

        if is_valid(range, character, password):
            print("{} {} {}".format(range, character, password))
            valid += 1

print('Valid: ', valid)
