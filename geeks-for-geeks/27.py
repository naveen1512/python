"""

http://www.geeksforgeeks.org/print-right-view-binary-tree-2/

"""


class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


def right_view_util(root, level, max_level):
    if root is None:
        return

    if max_level[0] < level:
        print(root.data)
        max_level[0] = level

    right_view_util(root.right, level + 1, max_level)

    right_view_util(root.left, level + 1, max_level)


def right_view(root):
    max_level = [0]
    right_view_util(root, 1, max_level)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.left.left = Node(9)
# root.right.left.right = Node(10)
root.right.right = Node(7)
root.right.left.right = Node(8)

right_view(root)

