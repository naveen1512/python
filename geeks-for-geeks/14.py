"""
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

http://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/
"""


def recursive(total, arr):
    length = len(arr)

    # base case 1
    if total == 0:
        return True

    # base case 1
    if length == 0 and total != 0:
        return False

    # If last element is graeter than the total, ignore it
    if arr[length - 1] > total:
        return recursive(total, arr[0:length - 1])

    # else, check if sum can be obtained by any of the following
    #   (a) including the last element
    #   (b) excluding the last element

    return recursive(total, arr[0:length - 1]) or recursive(total - arr[length - 1], arr[0:length - 1])


"""
We create a boolean 2D table subset[][] and fill it in bottom up manner. The value of subset[i][j]
will be true if there is a subset of set[0..j-1] with sum equal to i., otherwise false.
Finally, we return subset[sum][n]
"""


def pseudo_polynomial_time(total, arr):
    length = len(arr)
    result_arr = [[None for i in range(length + 1)] for j in range(total + 1)]

    # Base case 1 if total is 0
    for j in range(0, length + 1):
        result_arr[0][j] = True

    # Base case 2 if arr => length is not 0 and total is also not 0
    for i in range(1, total + 1):
        result_arr[i][0] = False

    # Fill the subset table in botton up manner
    for i in range(1, total + 1):
        for j in range(1, length + 1):
            result_arr[i][j] = result_arr[i][j - 1]
            if i >= arr[j - 1]:
                result_arr[i][j] = result_arr[i][j - 1] or result_arr[i - arr[j - 1]][j - 1]

    for i in range(0, total + 1):
        for j in range(0, length + 1):
            print(result_arr[i][j], end=' ')
        print()

    return result_arr[total][length]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(pseudo_polynomial_time(10, arr))
