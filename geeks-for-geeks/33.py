"""
http://www.geeksforgeeks.org/check-weather-given-binary-tree-perfect-not/
"""


class Node:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None


def find_a_depth(root):
    count = 0

    while root is not None:
        count += 1
        root = root._left

    return count


def is_perfect_binary_tree(root):
    depth = find_a_depth(root)
    return is_perfect_binary_tree_util(root, depth)


def is_perfect_binary_tree_util(root, depth):
    if root is None and depth == 0:
        return True

    if root._left is None and root._right is None and depth == 1:
        return True

    if root._left is None or root._right is None:
        return False

    return is_perfect_binary_tree_util(root._left, depth - 1) and is_perfect_binary_tree_util(root._right, depth - 1)


if __name__ == '__main__':
    root = Node(10)
    root._left = Node(20)
    root._right = Node(30)

    root._left._left = Node(40)
    root._left._right = Node(50)

    root._right._left = Node(60)
    root._right._right = Node(70)

    print(is_perfect_binary_tree(root))
