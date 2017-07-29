"""
https://docs.python.org/3.0/library/heapq.html
"""

import heapq

heap = []
# data = [8, 5, 9, 1, 7, 19, 14, 33, 45, 41, 0, -2, -8, 10, 11]
data = [(1, 'J'), (4, 'N'), (3, 'H'), (2, 'O')]

for item in data:
    heapq.heappush(heap, item)

ordered = []
while heap:
    ordered.append(heapq.heappop(heap))

data.sort()


# print(ordered)
# print(data)

class MinHeap:
    def __init__(self):
        self._heap = []

    def parent(self, i):
        return (i - 1) // 2

    def insert(self, item):
        heapq.heappush(self._heap, item)

    def decrease_key(self, i, new_key):
        self._heap[i] = new_key
        while i != 0 and self._heap[self.parent(i)] > self._heap[i]:
            # Swap both
            self._heap[self.parent(i)], self._heap[i] = self._heap[i], self._heap[self.parent(i)]

    def extract_min(self):
        return heapq.heappop(self._heap)

    def get_min(self):
        return self._heap[0]

    def delete_key(self, i):
        # 1st set ith key to min infinite
        self.decrease_key(i, float('-inf'))
        self.extract_min()


if __name__ == '__main__':
    heap_obj = MinHeap()
    heap_obj.insert(3)
    heap_obj.insert(2)
    heap_obj.delete_key(1)
    heap_obj.insert(15)
    heap_obj.insert(5)
    heap_obj.insert(4)
    heap_obj.insert(45)

    print(heap_obj.extract_min())

    print(heap_obj.get_min())

    heap_obj.decrease_key(2, 1)

    print(heap_obj.get_min())
