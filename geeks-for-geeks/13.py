"""
http://www.geeksforgeeks.org/dynamic-programming-set-1/

Dynamic Programming | Set 1 (Overlapping Subproblems Property)

Fibonacci number

"""


# Recursive
def recursive(num):
    if num == 0 or num == 1:
        return num

    return recursive(num - 1) + recursive(num - 2)


def memoization_fib(num, lookup_table):
    if num == 0 or num == 1:
        lookup_table[num] = num

    if lookup_table[num] is None:
        lookup_table[num] = memoization_fib(num - 1, lookup_table) + memoization_fib(num - 2, lookup_table)

    return lookup_table[num]


# Top down (Memoization)
def memoization(num):
    lookup_table = [None] * (num + 1)
    return memoization_fib(num, lookup_table)


# Bottom up (Tabulation)
def tabulation(num):
    lookup_table = [0] * (num + 1)
    # Base case assignment
    lookup_table[1] = 1

    for i in range(2, num + 1):
        lookup_table[i] = lookup_table[i - 1] + lookup_table[i - 2]

    return lookup_table[num]


if __name__ == '__main__':
    print(recursive(7))
    print(memoization(7))
    print(tabulation(7))
