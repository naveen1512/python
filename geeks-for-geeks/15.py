"""
http://www.geeksforgeeks.org/perfect-sum-problem-print-subsets-given-sum/

Perfect Sum Problem (Print all subsets with given sum)

"""

"""
We create a boolean 2D table subset[][] and fill it in bottom up manner. The value of subset[i][j]
will be true if there is a subset of set[0..i-1] with sum equal to j., otherwise false.
Finally, we return subset[n][sum]
"""


def print_subset(total, arr, arr_current_index, subset_list, result_arr):
    # If we reached end and sum is non-zero. We print
    #  subset_list[] only if arr[0] is equal to total OR result_arr[total][0]
    #  is true.
    if arr_current_index == 0 and total != 0 and result_arr[arr_current_index][total] == True:
        subset_list.append(arr[arr_current_index])
        print(subset_list)
        return

    # If sum becomes 0
    if total == 0:
        print(subset_list)
        return

    # print(' List ' + str(subset_list))
    # print('arr_current_index ' + str(arr_current_index) + ' Total ' + str(total))

    # If given total can be achieved after ignoring current element
    if result_arr[arr_current_index - 1][total]:
        another_subset_list = list(subset_list)
        print_subset(total, arr, arr_current_index - 1, another_subset_list, result_arr)

    # If given total can be achieved after considering current element
    if arr[arr_current_index] <= total and result_arr[arr_current_index - 1][total - arr[arr_current_index]]:
        subset_list.append(arr[arr_current_index])
        # print('Appended ' + str(arr[arr_current_index]) + ' in ' + str(subset_list))
        # print('arr_current_index ' + str(arr_current_index) + ' Total ' + str(total))

        print_subset(total - arr[arr_current_index], arr, arr_current_index - 1, subset_list, result_arr)


def pseudo_polynomial_time(total, arr):
    arr_length = len(arr)
    result_arr = [[None for i in range(total + 1)] for j in range(arr_length)]

    # Base case 1 if total is 0
    for i in range(0, arr_length):
        result_arr[i][0] = True

    # Total arr[0] can be achieved with single element
    if arr[0] <= total:
        result_arr[0][arr[0]] = True

    # Fill the subset table in botton up manner
    for i in range(1, arr_length):
        for j in range(0, total + 1):
            result_arr[i][j] = result_arr[i - 1][j]
            if j >= arr[i - 1]:
                result_arr[i][j] = result_arr[i - 1][j] or result_arr[i - 1][j - arr[i]]

    # for i in range(0, arr_length):
    #     for j in range(0, total + 1):
    #         print(result_arr[i][j], end=' ')
    #     print()

    subset = []
    print_subset(total, arr, arr_length - 1, subset, result_arr)


if __name__ == '__main__':
    arr = [2, 3, 5, 6, 8, 10]
    pseudo_polynomial_time(10, arr)
