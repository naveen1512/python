"""
http://www.geeksforgeeks.org/print-left-view-binary-tree/

"""


class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


def left_view_helper(root, level, max_level):
    if root is None:
        return

    if max_level[0] < level:
        print(root.data)
        max_level[0] = level

    left_view_helper(root.left, level + 1, max_level)
    left_view_helper(root.right, level + 1, max_level)


def left_view(root):
    max_level = [0]
    left_view_helper(root, 1, max_level)


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

left_view(root)
