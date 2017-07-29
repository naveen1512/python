"""
http://www.geeksforgeeks.org/dynamic-programming-set-11-egg-dropping-puzzle/
"""
import sys


def egg_drop_recursive(egg, floor):
    if floor == 0 or floor == 1:
        return floor

    if egg == 1:
        return floor

    min_attempts = sys.maxsize

    for x in range(1, floor + 1):
        res = max(egg_drop_recursive(egg - 1, x - 1), egg_drop_recursive(egg, floor - x))
        if res < min_attempts:
            min_attempts = res

    return 1 + min_attempts


def egg_drop_dynamic(egg, floor):
    # A 2D table where entery eggFloor[i][j] will represent minimum
    # number of trials needed for i eggs and j floors.
    egg_floor = [[0 for i in range(floor + 1)] for j in range(egg + 1)]

    # We need 1 trial for 1 floor and 0 trials for 0 floors
    for i in range(1, egg + 1):
        egg_floor[i][1] = 1

    # We need j trails for j floors and one eggs
    for j in range(1, floor + 1):
        egg_floor[1][j] = j

    # Fill rest of the entries in table using optimal substructure property
    for i in range(2, egg + 1):
        for j in range(2, floor + 1):
            egg_floor[i][j] = sys.maxsize
            for x in range(1, j + 1):
                max_trails = 1 + max(egg_floor[i - 1][x - 1], egg_floor[i][j - x])
                if max_trails < egg_floor[i][j]:
                    egg_floor[i][j] = max_trails

    return egg_floor[egg][floor]


if __name__ == '__main__':
    print(egg_drop_dynamic(2, 36))
