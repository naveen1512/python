class OnlyOne:
    class __OnlyOne:
        def __init__(self, val):
            self.val = val

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self, val):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(val)
        else:
            OnlyOne.instance.val = val

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __str__(self):
        return repr(self) + self.val


x = OnlyOne('sausage')
print(x)
y = OnlyOne('eggs')
print(y)
z = OnlyOne('spam')
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