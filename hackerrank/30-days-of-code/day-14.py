class Difference:
    def __init__(self, elements):
        self.elements = elements

    def computeDifference(self):
        self.elements.sort()
        self.maximumDifference = abs(self.elements[0] - self.elements[len(self.elements) - 1])


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
