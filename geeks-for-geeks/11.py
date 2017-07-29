"""
http://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/

Design a stack that supports getMin() in O(1) time and O(1) extra space

"""


class SpecialStack(list):
    def __init__(self):
        super().__init__()
        self.min_element = None

    def is_empty(self):
        return not self

    def push(self, item):
        if self.is_empty():
            self.append(item)
            self.min_element = item
            return

        if item >= self.min_element:
            self.append(item)
            return

        # Insert 2 * item - self.min_element
        # Set self.min_element to new value item
        self.append(2 * item - self.min_element)
        self.min_element = item

    def pop(self):
        if self.is_empty():
            return -1

        element = super().pop()
        if element >= self.min_element:
            return element

        # Return min_element and reset self.min_element again
        new_min_element = 2 * self.min_element - element
        element = self.min_element
        self.min_element = new_min_element
        return element

    def get_min(self):
        if self.is_empty():
            return -1
        return self.min_element


if __name__ == '__main__':
    s_stack = SpecialStack()
    s_stack.push(18)
    s_stack.push(19)
    s_stack.push(29)
    print(s_stack.get_min())
    s_stack.push(15)
    print(s_stack.get_min())
    s_stack.push(16)
    print(s_stack.get_min())
    s_stack.push(5)
    print(s_stack.get_min())
    s_stack.pop()
    print(s_stack.get_min())
    s_stack.pop()
    print(s_stack.get_min())
    s_stack.pop()
    print(s_stack.get_min())
    s_stack.pop()
    print(s_stack.get_min())
    s_stack.pop()
    print(s_stack.get_min())
    s_stack.pop()
    print(s_stack.get_min())
    s_stack.pop()
    print(s_stack.get_min())
