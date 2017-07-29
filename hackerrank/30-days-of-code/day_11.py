#!/bin/python3

import sys

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

ROW = COLUMN = 6
sumHourGlasses = [];

for r in range(0, ROW):
    if r + 3 > ROW:
        break
    for c in range(0, COLUMN):
        if c + 3 > COLUMN:
            break
        sumHourGlass = arr[r][c] + arr[r][c + 1] + arr[r][c + 2] + arr[r + 1][c + 1] + arr[r + 2][c] + arr[r + 2][
            c + 1] + arr[r + 2][c + 2]
        sumHourGlasses.append(sumHourGlass)

print(max(sumHourGlasses))
