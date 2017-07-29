def min_contiguous_sum(arr, k):
    size = len(arr)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        if i != min_index and k > 0:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            k -= 1

    min_sum = arr[0]
    for i in range(1, size):
        if min_sum + arr[i] < min_sum:
            min_sum + arr[i]
        else:
            break

    return min_sum


if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    print(min_contiguous_sum(arr, 1))
