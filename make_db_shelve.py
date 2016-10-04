import shelve

__author__ = 'Naveen'


from initdata import bob, sue

db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()