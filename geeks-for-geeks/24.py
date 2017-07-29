"""
http://www.geeksforgeeks.org/longest-palindromic-substring-set-2/
"""


def longest_palindrome(string):
    length = len(string)
    longest_substring_palindrome = ''
    longest_substring_palindrome_len = 0

    # One by one consider each element as center of even and odd length palindrome.
    for i in range(1, length):
        # Find even length palindrome with center points as i-1 and i.
        start = i - 1
        end = i
        while start >= 0 and end < length and string[start] == string[end]:
            if end - start + 1 > longest_substring_palindrome_len:
                longest_substring_palindrome_len = end - start + 1
                longest_substring_palindrome = string[start: end + 1]

            start -= 1
            end += 1

        # Find odd length palindrome with center point as i.
        start = i - 1
        end = i + 1
        while start >= 0 and end < length and string[start] == string[end]:
            if end - start + 1 > longest_substring_palindrome_len:
                longest_substring_palindrome_len = end - start + 1
                longest_substring_palindrome = string[start: end + 1]

            start -= 1
            end += 1

    return  longest_substring_palindrome

if __name__ == '__main__':
    string = 'forgeeksskeegfor'
    print(longest_palindrome(string))