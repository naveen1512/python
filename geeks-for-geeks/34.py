"""
http://www.geeksforgeeks.org/check-binary-string-0-between-1s-not/
"""


def check_string(string):
    first = string.find('1')
    last = string.rfind('1')

    for index in range(first, last + 1):
        if string[index] is not '1':
            return False

    return True

if __name__ == '__main__':
    # string = '1111'
    string = '01111011110000'
    print(check_string(string))
