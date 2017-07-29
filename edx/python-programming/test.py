#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 23:06:01 2017

@author: Naveen
"""
s = 'azcbobobegghakl'
count = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count += 1
        
print("Number of vowels:",count)