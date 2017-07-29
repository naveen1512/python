#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 20:43:55 2017

@author: Naveen
"""


import sys
import re


N = int(input().strip())

gmailIdUsers = []
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    if re.match('[a-z]+@gmail.com$', emailID):
        gmailIdUsers.append(firstName)

gmailIdUsers.sort()
for user in gmailIdUsers:
    print(user)
    