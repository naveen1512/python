"""
http://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/
"""


class Stack(list):
    def push(self, item):
        self.append(item)

    def is_empty(self):
        return not self


class SpecialStack(Stack):
    def __init__(self):
        super().__init__()
        self.min_stack = Stack()

    def push(self, item):
        if self.is_empty():
            super().push(item)
            self.min_stack.push(item)
        else:
            super().push(item)
            min_item = self.min_stack.pop()
            self.min_stack.push(min_item)
            if min_item < item:
                self.min_stack.push(min_item)
            else:
                self.min_stack.push(item)

    def pop(self, index=None):
        if self.min_stack.is_empty():
            return -1
        self.min_stack.pop()
        return super().pop()

    def get_min(self):
        if self.min_stack.is_empty():
            return -1
        min_item = self.min_stack.pop()
        self.min_stack.push(min_item)
        return min_item


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
