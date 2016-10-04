__author__ = 'Naveen'


class Mammals:
    def __init__(self):
        '''Constructure for this class.'''
        self.members = ['Tiger', 'Elephant', 'Wild Cat']


    def printMembers(self):
        print('Printing members of mammals class')
        for member in self.members:
            print('\t%s' % member)
