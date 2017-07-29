class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = Borg.__shared_state


class Singleton(Borg):
    def __init__(self, val):
        Borg.__init__(self)
        self.val = val

    def __str__(self):
        return repr(self) + self.val


x = Singleton('sausage')
print(x)
y = Singleton('eggs')
print(y)
z = Singleton('spam')
print(z)

print('===================================================')

print(x.val)
print(y.val)
print(z.val)

print('===================================================')

print(x)
print(y)
print(z)

print('===================================================')

x.val = 'naveen'

print(x.val)
print(y.val)
print(z.val)

print('===================================================')

print(x == y == z)