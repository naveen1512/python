"""
http://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/
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
        while temp is not None:
            print(temp._data, end=' ')
            temp = temp._next

        print()

    def reverse_by_k(self, k):
        self._head = self._reverse_by_k_helper(self._head, k)

    def _reverse_by_k_helper(self, head, k):
        curr = head
        prev = None
        nxt = None
        count = 0

        # Reverse first k nodes of the linked list
        while curr is not None and count < k:
            nxt = curr._next
            curr._next = prev
            prev = curr
            curr = nxt

            count += 1

        if nxt is not None:
            head._next = self._reverse_by_k_helper(nxt, k)

        return prev


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(9)
    llist.push(8)
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)

    print('Given Linked List.')
    llist.print_list()

    llist.reverse_by_k(3)

    print('Reversed Linked List.')
    llist.print_list()
