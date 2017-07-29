"""
http://www.geeksforgeeks.org/longest-palindrome-substring-set-1/

"""


def is_palindrome(string):
    j = len(string) - 1
    i = 0
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1

    return True


def brute_force(string):
    longest_substring_palindrome = ''
    longest_substring_palindrome_len = 0
    length = len(string)

    for i in range(0, length - 1):
        for j in range(i + 1, length):
            substring_len = j - i + 1
            substring = string[i:j + 1]
            if is_palindrome(substring) and longest_substring_palindrome_len < substring_len:
                longest_substring_palindrome_len = substring_len
                longest_substring_palindrome = substring

    if longest_substring_palindrome_len != 0:
        return longest_substring_palindrome

    return False


def dynamic(string):
    length = len(string)
    table = [[0 for j in range(length)] for i in range(length)]
    longest_substring_palindrome = ''
    longest_substring_palindrome_len = 0

    # All substring of length 1 is palindrome
    for i in range(length):
        table[i][i] = True

    # Check for substring of length 2
    for i in range(length - 1):
        if string[i] == string[i + 1]:
            table[i][i + 1] = True
            longest_substring_palindrome = string[i:i + 2]
            longest_substring_palindrome_len = 2

    # Check for length greater than 2, here k is lenth of the substring
    for k in range(3, length + 1):
        # Fix the starting index
        for i in range(0, length - k + 1):
            # Get the ending index of the substring from the starting index and length k
            j = i + k - 1
            if table[i + 1][j - 1] and string[i] == string[j]:
                table[i][j] = True
                if k > longest_substring_palindrome_len:
                    longest_substring_palindrome_len = k
                    longest_substring_palindrome = string[i:j + 1]

    # for i in range(length):
    #     print(table[i])

    return longest_substring_palindrome


if __name__ == '__main__':
    string = 'nan'
    print(brute_force(string))
    print(dynamic(string))
