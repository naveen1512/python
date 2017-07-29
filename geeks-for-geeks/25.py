"""
http://www.geeksforgeeks.org/minimum-number-deletions-make-string-palindrome/
"""


def longest_palindrome_str(string):
    length = len(string)

    result_table = [[0 for j in range(length)] for i in range(length)]

    for i in range(length):
        result_table[i][i] = 1

    for curr_str_len in range(2, length + 1):
        for i in range(0, length - curr_str_len + 1):
            j = i + curr_str_len - 1

            if string[i] == string[j] and curr_str_len == 2:
                result_table[i][j] = 2
            elif string[i] == string[j]:
                result_table[i][j] = 2 + result_table[i + 1][j - 1]
            else:
                result_table[i][j] = max(result_table[i + 1][j], result_table[i][j - 1])

    return result_table[0][length - 1]


def min_delete_to_make_string_palindrome(string):
    return len(string) - longest_palindrome_str(string)


if __name__ == '__main__':
    string = 'naveenprakashnaveen'
    print(min_delete_to_make_string_palindrome(string))
