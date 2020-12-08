#!/usr/bin/env python3

import sys

# for each line
# calculate the row and column id
# seat id = (row * 8)+column
# find highest seat id

def partition(start, end, half):
    # calculate total size i.e. 0, 127 == 128
    print('*********')
    print(half)
    print(start)
    print(end)
    # halve the size
    size=(end - start)+1
    hsize=size//2
    print(size)
    print(hsize)

    if half == 'lower':
        end=start+(hsize-1)
    if half == 'upper':
        start=end-(hsize-1)
    print('out:')
    print(start)
    print(end)
    # return updated start,end
    return (start,end)

def boarding_pass_to_seat_id(boarding_pass):
    # calculate row
    row_start=0
    row_end=127
    row_data=boarding_pass[:7]
    print(row_data)
    for c in row_data:
        half='lower' if c == 'F' else 'upper'
        row_start, row_end = partition(row_start, row_end, half)
    row=row_start

    # calculate column
    col_data=boarding_pass[7:]
    print(col_data)
    col_start=0
    col_end=7
    for c in col_data:
        half='lower' if c == 'L' else 'upper'
        col_start, col_end = partition(col_start, col_end, half)
    col=col_start

    return (row*8)+col


seat_ids=[]
highest_seat_id=0
with open(sys.argv[1], 'r') as f:
    for line in f:
        bp=line.rstrip('\n')
        seat_id=boarding_pass_to_seat_id(bp)
        seat_ids.append(seat_id)
        if seat_id > highest_seat_id: highest_seat_id = seat_id

print("highest seat id: {}".format(highest_seat_id))
