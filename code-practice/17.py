"""
http://www.geeksforgeeks.org/count-pairs-with-given-sum/

Count pairs with given sum in an array.

"""


# Using sorting.
# Will fail if multiple duplicate pairs exist.
def count_pairs_with_given_sum(arr, total):
    arr.sort()
    left_index = 0
    right_index = len(arr) - 1
    count_pairs = 0

    while left_index < right_index:
        current_pair_total = arr[left_index] + arr[right_index]

        if current_pair_total == total:
            count_pairs += 1
            left_index += 1
        elif current_pair_total < total:
            left_index += 1
        else:
            right_index -= 1

    return count_pairs


def count_pairs_with_given_sum_using_hash(arr, total):
    map = {}
    pair_count = 0

    for index in range(0, len(arr)):
        temp = total - arr[index]
        if temp in map:
            pair_count += 1
            print(str(temp) + ', ' + str(arr[index]))
        map[arr[index]] = True

    return pair_count


if __name__ == '__main__':
    arr = [7, 1, 5, 7, -1, 5, -1]
    total = 6
    print(count_pairs_with_given_sum_using_hash(arr, total))
