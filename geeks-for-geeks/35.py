"""
http://www.geeksforgeeks.org/largest-number-bst-less-equal-n/
"""


class Node:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None


def max_less_than_or_equal_to_N_recursive(root, N):
    if root is None:
        return -1

    if root._left is None and root._right is None and root._data > N:
        return -1

    if (root._data <= N and root._right is None) or (
                        root._data < N and root._right is not None and root._right._data > N):
        return root._data

    if root._data > N:
        return max_less_than_or_equal_to_N_recursive(root._left, N)
    else:
        return max_less_than_or_equal_to_N_recursive(root._right, N)


def max_less_than_or_equal_to_N_iterative(root, N):
    while root is not None:
        if root._left is None and root._right is None and root._data > N:
            return -1

        if (root._data <= N and root._right is None) or (
                            root._data < N and root._right is not None and root._right._data > N):
            return root._data

        if root._data > N:
            root = root._left
        else:
            root = root._right

    return -1


if __name__ == '__main__':
    root = Node(5)
    root._left = Node(2)
    root._right = Node(12)

    root._left._left = Node(1)
    root._left._right = Node(3)

    root._right._left = Node(9)
    root._right._right = Node(21)

    root._right._right._left = Node(19)
    root._right._right._right = Node(25)

    print(max_less_than_or_equal_to_N_iterative(root, 4))
