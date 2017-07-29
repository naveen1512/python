"""
http://www.artima.com/weblogs/viewpost.jsp?thread=236275
"""


class T():
    def __init__(self):
        self.a = 0


class A(T):
    def __init__(self):
        super().__init__()
        self.a = 1


class B(T):
    def __init__(self):
        T.__init__(self)
        self.a = 2


class C(A, B):
    pass


if __name__ == '__main__':
    c = C()
    print(c.a)
    print('MRO of C', C.__mro__)