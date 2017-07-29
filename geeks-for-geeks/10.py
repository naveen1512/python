"""
http://www.geeksforgeeks.org/check-door-open-closed/
"""


def print_status_of_a_door(num):
    sqrt = num ** 0.5
    if sqrt * sqrt == num:
        print('Open', end=' ')
    else:
        print('Closed', end=' ')


def print_status_of_all_the_doors(num):
    for i in range(1, num + 1):
        print_status_of_a_door(i)


if __name__ == '__main__':
    num = int(input('Enter the not of doors :: ').strip())
    print_status_of_all_the_doors(num)
