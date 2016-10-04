__author__ = 'Naveen'

import sys

print('Dive in')

saveStdout = sys.stdout
fsock = open('stdout.log', 'w')
sys.stdout = fsock

print('This message will be logged instaed of display')

sys.stdout = saveStdout;
fsock.close()
