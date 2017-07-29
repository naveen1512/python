from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    # __metaclass__ = ABCMeta

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def abstractMethod(self):
        print("Abstract in Parent")


# 1st way of inheriting
class MyBook(Book):
    def __init__(self, title, author, price):
        self.price = price
        super(MyBook, self).__init__(title, author)

    def display(self):
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Price: " + str(self.price))

    def abstractMethod(self):
        super(MyBook, self).abstractMethod()
        print("Abstract in Child")


class MyBookRegister():
    def __init__(self, title, author, price):
        self.price = price
        self.author = author
        self.title = title
        # super(MyBookRegister, self).__init__(title, author) Can't be called

    def display(self):
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Price: " + str(self.price))


# 2nd way of inheriting
Book.register(MyBookRegister)

if __name__ == '__main__':

    # title = input()
    # author = input()
    # price = int(input())
    title = 'My Love'
    author = 'Naveen Prakash Singh'
    price = 12.00

    new_novel = MyBook(title, author, price)
    new_novel.display()
    new_novel.abstractMethod()

    # new_novel_register = MyBookRegister(title, author, price)
    # new_novel_register.display()
    # new_novel_register.abstractMethod()

    print("Subclass: ", issubclass(MyBook, Book))
    print("Isinstance: ", isinstance(new_novel, Book))

    # Side-effect of using direct subclassing is it is possible to get list of classes derived from base one.
    for subClass in Book.__subclasses__():
        print("Sub class: " + subClass.__name__)
