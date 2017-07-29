"""
http://www.geeksforgeeks.org/check-if-total-number-of-divisors-are-even-or-odd/

"""


def count_divisors(num):
    count = 0
    sqrt = int(num ** 0.5) + 1
    i = 1
    while i <= sqrt:
        if num % i == 0:
            count += 1 if num / i == i else 2  # (2, 1) [num / i == i]
        i += 1
    if count % 2 == 0:
        print("Even")
    else:
        print("Odd")


"""
We can observe that the number of divisors is odd only in case of perfect squares. Hence the best solution would be
to check if the given number is perfect square or not. If it’s a perfect square, then the number of divisors would
be odd, else it’d be even.
"""


def count_divisors_optimized(num):
    if num < 1:
        return

    sqrt = int(num ** 0.5)
    if sqrt * sqrt == num:
        print("Odd")
    else:
        print("Even")


if __name__ == '__main__':
    num = int(input('Enter a number :: ').strip())
    count_divisors_optimized(num)
