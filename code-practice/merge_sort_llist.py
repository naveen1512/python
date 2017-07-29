"""
http://www.geeksforgeeks.org/merge-sort-for-linked-list/
"""


class Node:
    def __init__(self, data):
        self._data = data
        self._next = None


class LinkedList:
    def __init__(self):
        self._head = None

    def push(self, data):
        node = Node(data)
        node._next = self._head
        self._head = node

    def print_list(self):
        temp = self._head
        while temp:
            print(temp._data, end=' ')
            temp = temp._next

        print()


def merge_sort(head):
    if head is None or head._next is None:
        return head

    mid_node = get_middle_node(head)
    mid_node_next = mid_node._next

    mid_node._next = None

    left_list_head = merge_sort(head)
    right_list_head = merge_sort(mid_node_next)

    return merge_sorted_list(left_list_head, right_list_head)


def merge_sorted_list(head_1, head_2):
    if head_1 is None:
        return head_2

    if head_2 is None:
        return head_1

    sorted_list_head = None
    if head_1._data <= head_2._data:
        sorted_list_head = head_1
        sorted_list_head._next = merge_sorted_list(head_1._next, head_2)
    else:
        sorted_list_head = head_2
        sorted_list_head._next = merge_sorted_list(head_1, head_2._next)

    return sorted_list_head


def get_middle_node(head):
    if head is None:
        return None

    fast_node = head._next
    slow_node = head

    while fast_node is not None:
        fast_node = fast_node._next
        if fast_node is not None:
            slow_node = slow_node._next
            fast_node = fast_node._next

    return slow_node


if __name__ == '__main__':
    llist = LinkedList();

    llist.push(15)
    llist.push(10)
    llist.push(5)
    llist.push(20)
    llist.push(3)
    llist.push(2)

    llist.print_list()

    llist._head = merge_sort(llist._head)

    llist.print_list()
