import shelve

__author__ = 'Naveen'


db = shelve.open('class-shelve')
for key in db:
    print(key, ' => \n', db[key].name, db[key].pay)

db.close()