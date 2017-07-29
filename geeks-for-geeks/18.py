"""
http://practice.geeksforgeeks.org/problems/geek-and-coffee-shop/0
"""

import math


def mth_refill(N, M):
    mth_refill_coffee_count = N * (0.5 ** (M - 1))
    return math.floor(mth_refill_coffee_count)


if __name__ == '__main__':
    t = int(input().strip())
    index = 0
    while index < t:
        N, M = input().strip().split(' ')
        N = int(N)
        M = int(M)
        print(mth_refill(N, M))
        index += 1
