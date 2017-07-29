class OnlyOne:
    class __OnlyOne:
        def __init__(self, val):
            self.val = val

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __new__(cls, val):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(val)
        return OnlyOne.instance

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr__(self, key, value):
        setattr(OnlyOne.instance, key, value)


x = OnlyOne('sausage')
y = OnlyOne('eggs')
z = OnlyOne('spam')

print(x.val)
print(y.val)
print(z.val)

print(x)
print(y)
print(z)

x.val = 'naveen'

print(x.val)
print(y.val)
print(z.val)

print(x == y == z)