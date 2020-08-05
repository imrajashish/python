#Write a Python program to locate Python site-packages.
import site; 
print(site.getsitepackages())

# Write a python program to call an external command in Python.
from subprocess import call
call(["ls", "-l"])   #REMARK

#Write a python program to get the path and name of the file that is currently executing. 
import os
print("Current File Name : ",os.path.realpath(__file__))