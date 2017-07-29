class MyClass():
    class_var = 1
    data = []
    
    i = 0

    def __init__(self, inst_var):
        self.inst_var = inst_var

    def add(self):
        print('i', self.i)
        self.i += 1

foo = MyClass(10)
boo = MyClass(20)

foo.add()

print('Foo i', foo.i)
print('Class i', MyClass.i)

# print('Class variable using Class', MyClass.class_var)
# print('Class variable', foo.class_var, boo.class_var)
# print('Instance variable', foo.inst_var, boo.inst_var)

# setattr(MyClass, 'class_var', 20)
# setattr(foo, 'inst_var', 30)

# MyClass.__dict__['class_var'] = 10 # Read only proxy object, can't be reassigned

# foo.class_var = 20

foo.data.append(10)
MyClass.data.append(20)

print('Class data', MyClass.data)
print('Instance data', foo.data)

print('Class namespace', MyClass.__dict__)
print('Instance namespace', foo.__dict__)


print('=================================================')


class Bar():
    def __init__(self):
        self.__zap = 1
    def add(self):
        self.__zap += 1

a = Bar()
a.add()
a.add()
print('Inst variable', a._Bar__zap)

print('Bar instance class namespace', a.__dict__)


print('=================================================')

def called_class():
    print('Class assignment')
    return 2

class Bar():
    y = called_class()

    def __init__(self, x):
        self.x = x


def called_inst():
    print('Inst assignment')
    return 3

class Foo():
    def __init__(self, x):
        self.y = called_inst()
        self.x = x

Bar(1)
Bar(2)

Foo(1)
Foo(2)
