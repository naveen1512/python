#!/bin/python3

import sys

n = int(input().strip())

binaryArr = []

while n > 0:
    binaryArr.insert(0, n % 2)
    n = (int)(n / 2)

count = 0
countArr = []
length = len(binaryArr)

for i in range(0, length):
    if binaryArr[i] == 1:
        count += 1
    elif count != 0:
        countArr.append(count)
        count = 0

if count != 0:
    countArr.append(count)

print(max(countArr))
