#!/usr/bin/env python3

import sys
import re


def is_valid_passport(passport):
    # check required fields exist
    # ignore missing cid
    expected=set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    if not expected.issubset(passport.keys()):
        return False

    # validation
    # pretty crappy
    if len(passport['byr']) < 4 or not 1920 <= int(passport['byr']) <= 2002:
        # print('failed byr `{}`'.format(passport['byr']))
        return False

    if len(passport['iyr']) < 4 or not 2010 <= int(passport['iyr']) <= 2020:
        # print('failed iyr `{}`'.format(passport['iyr']))
        return False

    if len(passport['eyr']) < 4 or not 2020 <= int(passport['eyr']) <= 2030:
        # print('failed eyr `{}`'.format(passport['eyr']))
        return False

    if not passport['hgt'].endswith(('cm', 'in')):
        # print('failed hgt `{}`'.format(passport['hgt']))
        return False

    if passport['hgt'][-2:] == 'cm' and not 150 <= int(passport['hgt'][:-2]) <= 193:
        # print('failed hgt `{}`'.format(passport['hgt']))
        return False

    if passport['hgt'][-2:] == 'in' and not 59 <= int(passport['hgt'][:-2]) <= 76:
        return False

    if not re.search('^#[0-9a-f]{6}$', passport['hcl']):
        return False

    if not re.search('^(amb|blu|brn|gry|grn|hzl|oth)$', passport['ecl']):
        return False

    if not re.search('^[0-9]{9}$', passport['pid']):
        return False

    # otherwise, valid
    return True


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
    # print("{}".format(v))
    if is_valid_passport(v):
        valid=valid+1

print("Valid: {}".format(valid))
