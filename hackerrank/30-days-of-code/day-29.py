#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 21:36:23 2017

@author: Naveen
"""

"""
import sys


t = int(input().strip())

max = []
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    
    if n % 2 == 1:
        maxAnd = n-1
    else:
        maxAnd = n -2
    
    if k >= n:
        max.append(maxAnd)
    else:
        maxAnd = 0
        for a in range(1, n+1):
            for b in range(a+1, n+1):
                bitAnd = a & b 
                if bitAnd > maxAnd and bitAnd < k:
                    maxAnd = bitAnd
        max.append(maxAnd)
    
for m in max:
    print(m)
"""
x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))