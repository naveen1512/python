__author__ = 'Naveen'

import sys

fsock = open('stderr.log', 'w')
sys.stderr = fsock

raise Exception('This error will be logged.')
