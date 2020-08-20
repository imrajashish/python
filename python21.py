#Write a Python program to find path refers to a file or directory when you encounter a path name.
import os.path
for file in[__file__,os.path.dirname(__file__), '/', './broken_link']:
    print('File        :', file)
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))


#Write a Python program to check if a number is positive, negative or zero.
n = float(input("Input a number: "))
if n>0:
    print("psssative")
elif(n==0):
    print("Is Zero")
else:
    print("negitive")


#Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.
n = float(input("Enter the number"))
if(n%15==0):
    print("divisable by 15:",n)
else:
    print("is not divisible")
#or
num_list = [45, 55, 60, 37, 100, 105, 220]
# use anonymous function to filter
result = list(filter(lambda x: (x % 15 == 0), num_list))
print("Numbers divisible by 15 are",result)
