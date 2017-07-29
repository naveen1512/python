"""
http://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
"""

INT_MIN = -4294967296
INT_MAX = 4294967296


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_bst(root):
    return is_bst_util(root, INT_MIN, INT_MAX)


def is_bst_util(root, min_val, max_val):
    if root is None:
        return True

    if root.data < min_val or root.data > max_val:
        return False

    return (is_bst_util(root.left, min_val, root.data - 1)) and (is_bst_util(root.right, root.data + 1, max_val))


def is_bst_efficient(root):
    prev_node = [None]
    return is_bst_efficient_util(root, prev_node)


def is_bst_efficient_util(root, prev_node):
    if root:
        if not is_bst_efficient_util(root.left, prev_node):
            return False

        if prev_node[0] is not None and root.data <= prev_node[0].data:
            return False

        prev_node[0] = root

        return is_bst_efficient_util(root.right, prev_node)

    return True


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(10)

    # print(is_bst(root))
    print(is_bst_efficient(root))
