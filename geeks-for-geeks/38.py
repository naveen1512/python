"""
 http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
"""


# Only valid if at least one element is positive
def max_subarray_sum_kadane(arr):
    size = len(arr)

    max_sum_so_far = 0
    curr_max_sum = 0

    for i in range(size):
        curr_max_sum += arr[i]
        if curr_max_sum < 0:
            curr_max_sum = 0
        elif curr_max_sum > max_sum_so_far:
            max_sum_so_far = curr_max_sum

    return max_sum_so_far


# This will works with even if all the elements are negative
def max_subarray_sum(arr):
    size = len(arr)
    curr_sum = arr[0]
    max_sum_so_far = arr[0]

    for i in range(1, size):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum_so_far = max(curr_sum, max_sum_so_far)

    return max_sum_so_far


if __name__ == '__main__':
    arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    # arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(max_subarray_sum(arr))
