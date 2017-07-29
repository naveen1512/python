"""
http://www.geeksforgeeks.org/level-order-tree-traversal/
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_level_order(root):
    height = tree_height(root)
    for level in range(height + 1):
        print_given_level(root, level)


def print_given_level(root, level):
    if root is None:
        return

    if level == 1:
        print(root.data, end=' ')
    else:
        print_given_level(root.left, level - 1)
        print_given_level(root.right, level - 1)


def tree_height(root):
    if root is None:
        return 0

    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    if left_height < right_height:
        return right_height + 1
    else:
        return left_height + 1


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)
    root.right.right.left = Node(6)

    print_level_order(root)
