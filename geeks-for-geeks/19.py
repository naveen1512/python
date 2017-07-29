"""
http://www.geeksforgeeks.org/multiply-large-numbers-represented-as-strings/
"""


def multipy_string(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)

    if str1_len == 0 or str2_len == 0:
        return "0"

    result = [0] * (str1_len + str2_len)
    index_str1 = 0

    for i in reversed(range(0, str1_len)):

        carry = 0
        index_str2 = 0
        n1 = int(str1[i])
        for j in reversed(range(0, str2_len)):
            n2 = int(str2[j])
            final_sum = n1 * n2 + result[index_str1 + index_str2] + carry

            carry = final_sum // 10
            result[index_str1 + index_str2] = final_sum % 10

            index_str2 += 1

            if carry > 0:
                result[index_str1 + index_str2] += carry

        index_str1 += 1

    # ignore zero and find start position in result
    result_start_index = str1_len + str2_len - 1
    for i in reversed(range(0, result_start_index + 1)):
        if result[i] == 0:
            result_start_index -= 1
            continue
        break

    # If result_start_index is -1, mean either of the string was "0"
    if result_start_index == -1:
        return "0"

    result_str = ''.join(str(e) for e in result[0:result_start_index + 1])
    return result_str[::-1]


if __name__ == '__main__':
    test_case_no = int(input().strip())
    index = 0
    while index < test_case_no:
        str1, str2 = input().strip().split(' ')
        print(multipy_string(str1, str2))
        index += 1
