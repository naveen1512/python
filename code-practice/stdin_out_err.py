__author__ = 'Naveen'

import sys

"""
STDOUT
"""

for i in range(3):
    print('Dive in 1')

for i in range(3):
    sys.stdout.write('Dive in 2\n');

"""
STDERR
"""

for i in range(3):
    sys.stderr.write('Error Dive in 3\n');
