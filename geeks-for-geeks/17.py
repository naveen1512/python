"""
Minimum distance between two numbers

http://practice.geeksforgeeks.org/problems/minimum-distance-between-two-numbers/1

"""


def min_dist_2_nums(arr, n, x, y):
    length = len(arr)

    if length <= 1:
        return -1

    x_index = -1
    y_index = -1

    for curr_index in range(0, length):
        if x_index != -1 and y_index != -1:
            break

        if x_index == -1 and x == arr[curr_index]:
            x_index = curr_index

        if y_index == -1 and y == arr[curr_index]:
            y_index = curr_index

    if x_index == -1 or y_index == -1:
        return -1

    start_index = y_index if x_index > y_index else x_index
    min_diff = abs(x_index - y_index)

    while start_index < length:
        if x == arr[start_index] and abs(start_index - y_index) <= min_diff:
            x_index = start_index
            min_diff = abs(x_index - y_index)

        if y == arr[start_index] and abs(start_index - x_index) <= min_diff:
            y_index = start_index
            min_diff = abs(y_index - x_index)

        start_index += 1

    return min_diff


if __name__ == '__main__':
    t = int(input().strip())
    index = 0
    while index < t:
        length = int(input().strip())
        arr = [int(temp) for temp in input().strip().split(' ')]
        x, y = input().strip().split(' ')
        x = int(x)
        y = int(y)
        print(min_dist_2_nums(arr,length, x, y))

        index += 1
