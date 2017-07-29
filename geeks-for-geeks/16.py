"""
Find Index of 0 to be replaced with 1 to get longest continuous sequence of 1s in a binary array

http://www.geeksforgeeks.org/find-index-0-replaced-1-get-longest-continuous-sequence-1s-binary-array/

"""


def max_one_index(arr):
    max_one_count = 0
    max_index = 0
    pre_zero = -1
    pre_pre_zero = -1

    for curr in range(0, len(arr)):
        if arr[curr] == 0:
            if curr - pre_pre_zero > max_one_count:
                max_one_count = curr - pre_pre_zero
                max_index = pre_zero
            pre_pre_zero = pre_zero
            pre_zero = curr

    if len(arr) - pre_pre_zero > max_one_count:
        max_index = pre_zero

    return max_index


if __name__ == '__main__':
    arr = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
    print(max_one_index(arr))
