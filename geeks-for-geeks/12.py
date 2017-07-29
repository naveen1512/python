"""
Check if frequency of all characters can become same by one removal

http://www.geeksforgeeks.org/check-if-frequency-of-all-characters-can-become-same-by-one-removal/

"""


def all_same(freq):
    same = 0
    for char_count in freq:
        if char_count != 0:
            same = char_count
            break

    for char_count in freq:
        if char_count != 0 and char_count != same:
            return False

    return True


def is_possible_same_char_freq_after_one_removal(string):
    freq = [0] * 26
    base_ch = ord('a')
    for ch in string:
        freq[ord(ch) - base_ch] += 1

    if all_same(freq):
        return True

    ch_start = 0
    while ch_start < 26:
        if freq[ch_start] == 0:
            ch_start += 1
            continue

        freq[ch_start] -= 1

        if all_same(freq):
            return True

        freq[ch_start] += 1

        ch_start += 1

    return False


if __name__ == '__main__':
    string = 'abcc'
    print(is_possible_same_char_freq_after_one_removal(string))
