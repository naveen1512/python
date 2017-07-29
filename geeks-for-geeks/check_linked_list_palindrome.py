"""
http://www.geeksforgeeks.org/check-linked-list-strings-form-palindrome/
http://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def init(self, data_list):
        while len(data_list):
            node = Node(data_list.pop())
            node.next = self.head
            self.head = node

        return self.head

    def print_list(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

    # Construct a string out of given linked list and check if the constructed string is palindrome or not.
    def is_palindrome_using_temp_string(self):
        str_list = []

        temp = self.head
        while temp:
            str_list.append(temp.data)
            temp = temp.next

        string = ''.join(str_list)
        return string == string[::-1]

    # Construct a stack and the compare each poped element with list.
    def is_palindrome_using_stack(self):
        temp_stack = []

        temp = self.head
        while temp:
            temp_stack.append(temp.data)
            temp = temp.next

        # Compare with the poped element of stack
        temp = self.head
        while temp:
            if temp.data != temp_stack.pop():
                return False

            temp = temp.next

        return True

    def reverse(self, head):
        prev_node = None
        current_node = head
        next_node = None

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node

    def is_palindrome_by_reversing_half_the_list(self):
        if self.head is None or self.head.next is None:
            return False

        slow_temp = self.head
        fast_temp = self.head
        prev_slow_temp = self.head
        mid_temp = None

        while fast_temp is not None and fast_temp.next is not None:
            prev_slow_temp = slow_temp
            slow_temp = slow_temp.next
            fast_temp = fast_temp.next.next

        if fast_temp is not None:
            mid_temp = slow_temp
            slow_temp = slow_temp.next

        second_half = slow_temp
        prev_slow_temp.next = None  # Close the 1st half here

        second_half = self.reverse(second_half)
        response = self.compare_lists(self.head, second_half)
        second_half = self.reverse(second_half)

        if mid_temp is not None:
            prev_slow_temp.next = mid_temp
            mid_temp = second_half
        else:
            prev_slow_temp.next = second_half

        return response

    def compare_lists(self, head_1, head_2):

        while head_1 and head_2:
            if head_1.data != head_2.data:
                return False

            head_1 = head_1.next
            head_2 = head_2.next

        if head_1 is None and head_2 is None:
            return True

        return False


if __name__ == '__main__':
    linked_list = LinkedList()
    # linked_list.init(['a', 'b', 'c', 'd', 'c', 'b', 'a'])
    linked_list.init(['a', 'b', 'a', 'a'])
    # linked_list.reverse()
    # linked_list.print_list()
    # print(linked_list.get_middle_node().data)

    # print(linked_list.is_palindrome_using_temp_string())
    # print(linked_list.is_palindrome_using_stack())
    print(linked_list.is_palindrome_by_reversing_half_the_list())
