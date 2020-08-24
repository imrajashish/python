#Write a Python program to check whether multiple variables have the same value.
x = 20
y = 20
z = 20
if x == y == z ==20:
    print("All variabe is the same value!")

#Write a Python program to sum of all counts in a collections?
import collections
num = [2,2,4,6,6,8,6,10,4,3243]
print(sum(collections.Counter(num).values()))

#Write a Python program to check whether an integer fits in 64 bits.
int_val = 30
if int_val.bit_length() <= 63:
    print((-2 ** 63).bit_length())
    print((2 ** 63).bit_length())

#Write a Python program to get the actual module object for a given object.
from inspect import getmodule
from math import sqrt
print(getmodule(sqrt))

#Write a Python program to check whether lowercase letters exist in a string.
s = "Ashish"
print(any(c.islower() for c in s))

#Write a Python program to add trailing and leading zeroes to a string
str1='122.22'
print("Original String: ",str1)
print("\nAdded trailing zeros:")
str1 = str1.ljust(8, '0')
print(str1)
str1 = str1.ljust(10, '0')
print(str1)
print("\nAdded leading zeros:")
str1='122.22'
str1 = str1.rjust(8, '0')
print(str1)
str1 = str1.rjust(10, '0')
print(str1)


