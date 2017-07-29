
n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]


def swap(i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


totalNoOfSwaps = 0

for i in range(n):
    noOfSwaps = 0

    for j in range(n-1):
        if a[j] > a[j+1]:
            swap(j, j+1)
            noOfSwaps+=1

    totalNoOfSwaps += noOfSwaps
    if noOfSwaps == 0:
        break


print('Array is sorted in ' + str(totalNoOfSwaps) + ' swaps.')
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[n-1]))