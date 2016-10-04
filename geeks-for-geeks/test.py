__author__ = 'Naveen'

# Different way of importing a file.
# 1
# import minimum_cost_to_make_two_string_identical

# 2
# moduleName = input('Enter the module name :: ');
# moduleImport = __import__(moduleName);
#
# print('Module info :: ')
# print(dir(moduleName));

# 3
# import sys
# sys.path.insert(0, '../system') # Put folder path into Python path
# import import_file


# 4
# Make dir to package by creating __init__.py and import that dir as module anywhere.
# import  animals
# myBird = animals.Birds()
# myMammal = animals.Mammals()
# myBird.printMembers()
# myMammal.printMembers()

# 5
from animals import *
myMammal = Mammals()
myMammal.printMembers()
# Following Symbol is not available since __all__ in animals module does not have Birds symbol.
# myBird = Birds()
# myBird.printMembers()

print("__name__ :: " + __name__);



