#Write a Python program to determine profiling of Python programs.
import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')

#Write a Python program to print to stderr.
'''from __future__ import print_function
import sys
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

eprint("abc", "efg", "xyz", sep="--")'''

#Write a python program to access environment variables.

import os
print('*____________________*')
print(os.environ)
print('*____________________*')
print(os.environ['HOME'])
print('*____________________*')
print(os.environ['PATH'])