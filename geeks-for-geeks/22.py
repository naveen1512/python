"""
http://www.geeksforgeeks.org/dynamic-programming-set-12-longest-palindromic-subsequence/
"""


def recursive(string):
    length = len(string)

    # Base case 1 - if there is one char
    if length == 1:
        return 1

    # Base case 2 - if there is two chars and both are same
    if length == 2 and string[0] == string[1]:
        return 2

    # If 1st and last chars match
    if string[0] == string[-1]:
        return recursive(string[1:length - 1]) + 2

    # If 1st and last chars do not match
    return max(recursive(string[1:length]), recursive(string[0: length - 1]))


def dynamic(string):
    length = len(string)

    # table to store result of sub-problem
    result_table = [[0 for j in range(length)] for i in range(length)]

    # strings of length 1 are palindrome of length 1
    # here i, i represent substring of string from index i to index i.
    for i in range(length):
        result_table[i][i] = 1

    # Build the table. Note that the lower diagonal values of table are
    # useless and not filled in the process. The values are filled in a
    # manner similar to Matrix Chain Multiplication DP solution (See
    # http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
    # cl is length of substring
    # i, j represent substring of given string from index i to index j.
    for cl in range(2, length + 1):
        for i in range(length - cl + 1):
            j = i + cl - 1
            if string[i] == string[j] and cl == 2:
                result_table[i][j] = 2
            elif string[i] == string[j]:
                result_table[i][j] = 2 + result_table[i + 1][j - 1]
            else:
                result_table[i][j] = max(result_table[i + 1][j], result_table[i][j - 1])

    return result_table[0][length - 1]


if __name__ == '__main__':
    string = 'GEEKSFORGEEKS'
    # string = 'BBABCBCAB'

    print(dynamic(string))
    print(recursive(string))
