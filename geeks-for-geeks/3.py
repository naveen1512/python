# http://www.geeksforgeeks.org/maximum-difference-between-two-elements/
# Maximum difference between two elements such that larger element appears after the smaller number


def max_diff(arr):
    max_diff_nums = arr[1] - arr[0]
    i = 0
    arr_len = len(arr)
    while i < arr_len:
        j = i + 1
        while j < arr_len:
            if arr[j] - arr[i] > max_diff_nums:
                max_diff_nums = arr[j] - arr[i]
            j += 1
        i += 1

    return max_diff_nums


"""
We need to keep track of 2 things:

1) Maximum difference found so far (max_diff).
2) Minimum number visited so far (min_element).

"""


def max_diff_optimized(input_arr):
    length = len(input_arr)
    if length < 3:
        raise Exception('Input array is length is less than 2');

    min_element = input_arr[0]
    max_diff_num = input_arr[1] - input_arr[0]

    index = 1
    while index < length:
        if input_arr[index] - min_element > max_diff_num:
            max_diff_num = input_arr[index] - min_element
        if input_arr[index] < min_element:
            min_element = input_arr[index]
        index += 1
    return max_diff_num


"""
First find the difference between the adjacent elements of the array and store all differences in an auxiliary
array diff[] of size n-1. Now this problems turns into finding the maximum sum subarray of this difference array.
"""


def max_diff_optimized_1(arr):
    length = len(arr)

    if length < 3:
        raise Exception('Input array is length is less than 2');

    index = 1
    diff_arr = []
    while index < length:
        diff_arr.append(arr[index] - arr[index - 1])
        index += 1

    # Find maximum sum subarray in diff array
    max_diff_num = diff_arr[0]
    index = 1
    while index < length - 1:
        if diff_arr[index - 1] > 0:
            diff_arr[index] += diff_arr[index - 1]

        if max_diff_num < diff_arr[index]:
            max_diff_num = diff_arr[index]
        index += 1

    return max_diff_num


if __name__ == '__main__':
    arr = [1, 2, 90, 10, 110]
    print(max_diff_optimized_1(arr))
