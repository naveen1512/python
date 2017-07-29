#!/bin/python3

import sys


n = int(input().strip())

arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

strArr = ''
for i in range(0, n):
    strArr += str(arr[n - 1]) + ' '
    n -= 1
print(strArr)