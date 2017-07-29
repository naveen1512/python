"""
http://www.geeksforgeeks.org/bottom-view-binary-tree/
"""
from collections import deque


class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


def bottom_view(root):
    if root is None:
        return

    # This will store the result
    hash_map = {}

    # This will store tree in level order traversal
    queue = deque()

    # Initialize root horizontal distance as 0
    hd = 0

    root.hd = hd
    queue.append(root)

    while len(queue) != 0:
        temp_node = queue.popleft()
        hd = temp_node.hd

        hash_map[hd] = temp_node.data

        if temp_node.left is not None:
            temp_node.left.hd = hd - 1
            queue.append(temp_node.left)

        if temp_node.right is not None:
            temp_node.right.hd = hd + 1
            queue.append(temp_node.right)

    for key, value in sorted(hash_map.items()):
        print(value, end=' ')


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

bottom_view(root)
