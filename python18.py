#Write a Python program to create a copy of its own source code.
print()
print((lambda str='print(lambda str = %r: (str %% str))()': (str % str))())
print()

#Write a Python program to swap two variables.
a = 30
b = 20
print("\nBefore swap a = %d and b = %d" %(a, b))
a, b = b, a
print("\nAfter swaping a = %d and b = %d" %(a, b))
print()

#Write a Python program to define a string containing special characters in various forms.
print()
print("\#{'}${\"}@/")
print("\#{'}${"'"'"}@/")
print(r"""\#{'}${"}@/""")
print('\#{\'}${"}@/')
print('\#{'"'"'}${"}@/')
print(r'''\#{'}${"}@/''')
print()

#Write a Python program to get the identity of an object.
obj1 = object()
obj1_address = id(obj1)
print()
print(obj1_address)
print()
