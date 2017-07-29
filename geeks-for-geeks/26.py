"""
http://www.geeksforgeeks.org/given-a-sequence-of-words-print-all-anagrams-together/
"""


class Word():
    def __init__(self, string, index):
        self.string = string
        self.index = index


def create_duplicate_list(strings, size):
    duplicate_list = []

    for i in range(size):
        duplicate_list.append(Word(strings[i], i))

    return duplicate_list


# Create a duplicate list of words and their indexes and sort the words and then sort the duplicate list.
# Print the word from original list based on the duplicate sorted list indexes.
def print_anagram_together(strings):
    size = len(strings)

    duplicate_strings = create_duplicate_list(strings, size)

    for i in range(size):
        duplicate_strings[i].string = ''.join(sorted(duplicate_strings[i].string))

    duplicate_strings = sorted(duplicate_strings, key=lambda k: k.string)

    for word in duplicate_strings:
        print(strings[word.index], end=' ')


def anagram_hash(string):
    xor = 0
    for char in string:
        xor ^= ord(char)

    return xor


# Group all the anagram using the hash.
def print_anagram_together_using_hash(strings):
    anagram = {}

    for string in strings:
        str_hash = anagram_hash(string)
        if str_hash in anagram:
            anagram[str_hash].append(string)
        else:
            anagram[str_hash] = [string]

    for key, value in anagram.items():
        print(' '.join(value), end=' ')


if __name__ == '__main__':
    strings = ["cat", "dog", "tac", "god", "act"]
    print_anagram_together(strings)
    print()
    print_anagram_together_using_hash(strings)
