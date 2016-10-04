import pickle

__author__ = 'Naveen'


from initdata import db


dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()