import shelve

__author__ = 'Naveen'

from person import Person
from manager import Manager

bob = Person('Bob Smith', 42, 30000, 'Software')
sue = Person('Sue Jones', 45, 40000, 'Hardware')
tom = Manager('Tom Due', 50, 50000)

db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()