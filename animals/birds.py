__author__ = 'Naveen'

class Birds:
    def __init__(self):
        '''Constructure for this class'''
        self.members = ['Sparrow', 'Robin', 'Duck']

    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
            print('\t%s' %member)
