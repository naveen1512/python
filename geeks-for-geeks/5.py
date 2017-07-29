"""
http://www.geeksforgeeks.org/check-larger-number-divisible-36/

A number is divisible by 36 if the number is divisible by 4 and 9

    A number is divisible by 4 if the number formed by its last 2 digits is divisible by 4
    A number is divisible by 9 if the sum of the digits of the number is divisible by 9

"""


def is_divisible_by_36(num):
    num_len = len(num)

    if num_len == 0:
        return "No"

    if num_len == 1 and num[0] != '0':
        return "No"

    last_two_digit_num = int(num[num_len - 2]) * 10 + int(num[num_len - 1])
    if last_two_digit_num % 4 != 0:
        return "No"

    sum = 0
    for char in num:
        sum += int(char)

    if sum % 9 != 0:
        return  "No"

    return "Yes"


if __name__ == '__main__':
    num = "92567812197966231384"
    print(is_divisible_by_36(num))