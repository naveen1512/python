"""
http://www.geeksforgeeks.org/merge-sort/
"""


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    temp_arr_1 = [0] * n1
    temp_arr_2 = [0] * n2

    for i in range(0, n1):
        temp_arr_1[i] = arr[l + i]

    for j in range(0, n2):
        temp_arr_2[j] = arr[m + j + 1]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if temp_arr_1[i] < temp_arr_2[j]:
            arr[k] = temp_arr_1[i]
            i += 1
        else:
            arr[k] = temp_arr_2[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = temp_arr_1[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = temp_arr_2[j]
        j += 1
        k += 1


def merge_without_extra_space(arr, l, m, r):
    i = l
    j = m + 1

    for i in range(r, m, -1):
        last = arr[m]

        # Insertion sort
        j = m - 1
        while j >= l and arr[j] > arr[i]:
            arr[j + 1] = arr[j]
            j -= 1

        if j != m - 1 or last > arr[i]:
            arr[j + 1] = arr[i]
            arr[i] = last


def merge_sort_helper(arr, l, r):
    if l < r:
        mid = (l + r) // 2

        merge_sort_helper(arr, l, mid)
        merge_sort_helper(arr, mid + 1, r)

        merge_without_extra_space(arr, l, mid, r)


def merge_sort(arr):
    merge_sort_helper(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7, 0, -6, 11, -4]
    merge_sort(arr)
    print(arr)
