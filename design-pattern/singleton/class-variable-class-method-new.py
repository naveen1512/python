class Singleton:
    __instance = None

    def __new__(cls, val):
        if not Singleton.__instance:
            Singleton.__instance = object.__new__(cls)
        Singleton.__instance.val = val
        return Singleton.__instance

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
