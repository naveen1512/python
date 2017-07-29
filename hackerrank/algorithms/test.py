# def min_bribe_using_bubble_sort(queue):
#     bribe = 0
#
#     while True:
#         swap = False
#         for i in range(1, len(queue)):
#             if queue[i - 1] - i > 2:
#                 return -1
#
#             if queue[i - 1] > queue[i]:
#                 swap = True
#                 bribe += 1
#                 cache = queue[i - 1]
#                 queue[i - 1] = queue[i]
#                 queue[i] = cache
#
#         if swap is False:
#             return bribe
#
#
# T = int(input().strip())
# for a0 in range(T):
#     n = int(input().strip())
#     q = [int(q_temp) for q_temp in input().strip().split(' ')]
#     min_bribe = min_bribe_using_bubble_sort(q)
#     if min_bribe != -1:
#         print(min_bribe)
#     else:
#         print('Too chaotic')

from operator import attrgetter


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


if __name__ == '__main__':
    student_objects = [Student('John', 'A', 15), Student('jane', 'B', 12), Student('dave', 'B', 10)]
    # print(sorted(student_objects, key=lambda student: student.age))
    # print(sorted(student_objects, key=attrgetter('grade', 'age')))
    print(sorted(student_objects, key=attrgetter('age'), reverse=True))