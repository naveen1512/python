"""
http://www.geeksforgeeks.org/count-number-ways-reach-given-score-game/
http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
"""


def count_recursive(coins, m, n):
    if n == 0:
        return 1

    if n < 0:
        return 0

    if m <= 0 and n >= 1:
        return 0

    return count_recursive(coins, m, n - coins[m - 1]) + count_recursive(coins, m - 1, n)


def count_DP(coins, m, n):
    table = [0] * (n + 1)
    table[0] = 1

    for i in range(m):
        for j in range(coins[i], n + 1):
            table[j] += table[j - coins[i]]

    return table[n]


def no_of_ways(A, S):
    table = [0] * (A + 1)

    table[0] = 1

    count_of_no_can_be_used = A - S + 1

    if count_of_no_can_be_used <= 0:
        return 0

    for i in range(count_of_no_can_be_used):
        num = S + i
        for j in range(num, A + 1):
            table[j] += table[j - num]

    return table[A] % (10 ^ 9 + 9)


if __name__ == '__main__':
    coins = [3, 5, 10]
    print(count_DP(coins, 3, 20))

# if __name__ == '__main__':
#     T = int(input().strip())
#     index = 0
#     while index < T:
#         A, S = input().strip().split(' ')
#         A = int(A)
#         S = int(S)
#         print(no_of_ways(A, S))
#         index += 1
