"""
http://www.geeksforgeeks.org/minimum-sum-absolute-difference-pairs-two-arrays/

"""


def min_sum_abs_diff_of_pairs_of_two_array(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)

    if len1 == 0 or len2 == 0 or len1 != len2:
        return -1

    arr1.sort()
    arr2.sort()

    count = 0
    min_sum = 0
    while count < len1:
        min_sum += abs(arr1[count] - arr2[count])
        count += 1

    return min_sum


if __name__ == '__main__':
    arr1 = [4, 1, 8, 7]
    arr2 = [2, 3, 6, 5]
    print(min_sum_abs_diff_of_pairs_of_two_array(arr1, arr2))
