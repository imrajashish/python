#Write a Python program to count the number of occurrence of a specific character in a string.
s = "this is a cir"
print(s.count("i"))

#Write a Python program to check whether a file path is a file or a directory.
import os
path = "abc.txt"
if os.path.isdir(path):
    print("\nIT is a directory")
elif os.path.isfile(path):
    print("\n It is a normal file")
else:
    print("it is a special file(socket,FIFo,device file)")
print()

#Write a Python program to get the ASCII value of a character.

print()
print(ord('A'))
print(ord('@'))
print(ord('h'))
print(ord('S'))

#Write a Python program to get the  size of a file.
import os
file_size = os.path.getsize("abc.txt")
print("\nThe size of abc.txt is :",file_size,"Bytes")
print()

#what is output of this code
a = 148
b = a * a + a
print(b % a < b / a)

#Given variables x=30 and y=20, write a Python program to print t "30+20=50"
x = 30
y = 20
print("\n%d+%d=%d" % (x, y, x+y)) #remark
print()

#Write a Python program to perform an action if a condition is true.
n=1
if n==1:
    print("\n First day of month")
print()
