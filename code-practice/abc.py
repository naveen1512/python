from abc import ABCMeta, abstractmethod


class Foo:
    pass

class MyABC(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, C):
        return NotImplemented



MyABC.register(Foo)

print(issubclass(Foo, MyABC))
print(isinstance(Foo(), MyABC))
