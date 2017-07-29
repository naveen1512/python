"""
http://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/

"""


class Node:
    def __init__(self, item):
        self._data = item
        self._next = None


class LinkedList:
    def __init__(self):
        self._head = None

    def push(self, data):
        node = Node(data)
        node._next = self._head
        self._head = node

    def detect_and_break_loop(self):
        if self._head is None or self._head._next is None:
            return

        slow = self._head
        fast = self._head

        while fast is not None and fast._next is not None:
            slow = slow._next
            fast = fast._next._next

            if slow == fast:
                break

        if slow == fast:
            slow = self._head
            while slow._next != fast._next:
                slow = slow._next
                fast = fast._next
            fast._next = None

    def print_list(self):
        temp = self._head
        while temp is not None:
            print(temp._data, end=' ')
            temp = temp._next

        print()


if __name__ == '__main__':
    llist = LinkedList()
    llist._head = Node(50)
    llist._head._next = Node(20)
    llist._head._next._next = Node(15)
    llist._head._next._next._next = Node(4)
    llist._head._next._next._next._next = Node(10)

    # llist.print_list()

    # Create a loop for testing
    llist._head._next._next._next._next._next = llist._head._next._next

    # llist.print_list()

    llist.detect_and_break_loop()

    llist.print_list()
