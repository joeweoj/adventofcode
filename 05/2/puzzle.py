#!/usr/bin/env python3

import sys

# for each line
# calculate the row and column id
# seat id = (row * 8)+column
# find highest seat id

def partition(start, end, half):
    # calculate total size i.e. 0, 127 == 128
    # halve the size
    size=(end - start)+1
    hsize=size//2
    if half == 'lower':
        end=start+(hsize-1)
    if half == 'upper':
        start=end-(hsize-1)
    # return updated start,end
    return (start,end)

def boarding_pass_to_row_col(boarding_pass):
    # calculate row
    row_start=0
    row_end=127
    row_data=boarding_pass[:7]
    for c in row_data:
        half='lower' if c == 'F' else 'upper'
        row_start, row_end = partition(row_start, row_end, half)
    row=row_start

    # calculate column
    col_data=boarding_pass[7:]
    col_start=0
    col_end=7
    for c in col_data:
        half='lower' if c == 'L' else 'upper'
        col_start, col_end = partition(col_start, col_end, half)
    col=col_start

    return (row,col)


seat_ids=[]
info=[]
highest=0
with open(sys.argv[1], 'r') as f:
    for line in f:
        bp=line.rstrip('\n')
        row,col=boarding_pass_to_row_col(bp)
        seat_id=(row*8)+col
        seat_ids.append(seat_id)
        # store everything for future lookup
        info.append({'bp':bp, 'id':seat_id, 'row':row, 'col':col})


prev=None
for seat in sorted(info, key=lambda rc : (rc['id'])):
    if prev != None and seat['id'] != prev['id']+1:
        print('Missing seat id: {}'.format(prev['id']+1))
        break
    else:
        prev=seat
