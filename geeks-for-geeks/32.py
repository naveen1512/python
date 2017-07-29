"""
http://www.geeksforgeeks.org/sorted-array-to-balanced-bst/
http://www.geeksforgeeks.org/?p=17063
"""


class LinkedListNode:
    def __init__(self, data):
        self._data = data
        self._next = None


def create_linked_list(data_list):
    head = None

    while len(data_list):
        node = LinkedListNode(data_list.pop())
        node._next = head
        head = node

    return head


def print_list(temp):
    while temp:
        print(temp._data)
        temp = temp._next


def linked_list_len(head):
    count = 0
    while head:
        head = head._next
        count += 1

    return count


class Node:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None


def sorted_list_to_balanced_BST(sorted_list):
    size = len(sorted_list)

    if size == 0:
        return None

    return sorted_list_to_balanced_BST_util(sorted_list, 0, size - 1)


def sorted_list_to_balanced_BST_util(sorted_list, start, end):
    if start > end:
        return None

    # Get the mid element and make it root
    mid_index = (start + end) // 2
    root = Node(sorted_list[mid_index])

    root._left = sorted_list_to_balanced_BST_util(sorted_list, start, mid_index - 1)
    root._right = sorted_list_to_balanced_BST_util(sorted_list, mid_index + 1, end)

    return root


def sorted_linked_list_to_balanced_BST(head):
    size = linked_list_len(head)
    head_pointer = [head]  # Keep current head pointer here to construct the root node.

    return sorted_linked_list_to_balanced_BST_util(head_pointer, size)


def sorted_linked_list_to_balanced_BST_util(head_pointer, size):
    if size <= 0:
        return None

    mid_size = size // 2

    left_tree = sorted_linked_list_to_balanced_BST_util(head_pointer, mid_size)

    root = Node(head_pointer[0]._data)
    root._left = left_tree

    head_pointer[0] = head_pointer[0]._next  # update the head pointer

    root._right = sorted_linked_list_to_balanced_BST_util(head_pointer, (size - mid_size - 1))

    return root


def in_order_traversal(root):
    if root:
        in_order_traversal(root._left)
        print(root._data)
        in_order_traversal(root._right)


if __name__ == '__main__':
    sorted_list = [1, 10, 18, 30, 45, 67, 89, 167]
    # root = sorted_list_to_balanced_BST(sorted_list)
    # in_order_traversal(root)

    # print_list(create_linked_list(sorted_list))
    head = create_linked_list(sorted_list)
    root = sorted_linked_list_to_balanced_BST(head)
    in_order_traversal(root)
    # print(linked_list_len(create_linked_list(sorted_list)))
