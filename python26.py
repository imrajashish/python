# Write a Python program to convert an integer to binary keep leading zeros.
x = 50
print(format(x,'08b'))
print(format(x,'010b'))

#Write a python program to convert decimal to hexadecimal.
x = 30
print(format(x,'02x'))
x = 4
print(format(x,'02x'))

#Write a Python program to find the operating system name, platform and platform release date
import os, platform
print("Operating system name:")
print(os.name)
print("Platform name:")
print(platform.system())
print("Platform release:")
print(platform.release())

#Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system.
import struct
print(struct.calcsize("p")*8)

#Write a Python program to check whether variable is of integer or string
x = ("Ashish",5,"suman")
print(type(x[1]))

#Write a Python program to test if a variable is a list or tuple or a set.
#x = ['a', 'b', 'c', 'd']
#x = {'a', 'b', 'c', 'd'}
x = ('tuple', False, 3.2, 1)
if type(x) is list:
    print('x is a list')
elif type(x) is set:
    print('x is a set')
elif type(x) is tuple:
    print('x is a tuple')    
else:
    print('Neither a list or a set or a tuple.')
