"""
http://www.geeksforgeeks.org/minimum-rotations-required-get-string/
"""


def no_of_rotation_to_get_same_str(string):
    temp_str = string + string
    str_len = len(string)

    count = 0
    for index in range(1, str_len + 1):
        sub_temp_str = temp_str[index:str_len + index]

        count += 1
        if sub_temp_str == string:
            break

    return count


if __name__ == '__main__':
    string = 'geek'
    print(no_of_rotation_to_get_same_str(string))
