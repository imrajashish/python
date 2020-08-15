#Write a Python program to test whether the system is a big-endian platform or little-endian platform.
import sys
print()
if sys.byteorder == "little":
    print("Little-endian platform.")
else:
    print("little-endian platform.")
print()

#Write a Python program to find the available built-in modules. 
import sys
import textwrap
module_name = ' , '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name,width=70))

#Write a Python program to get the size of an object in bytes.
import sys
str1 = "three"
str2 = "four"
str3 = "one"
print()
print("Memory size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " bytes")
print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " bytes")
print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " bytes")
print()

#Write a Python program to get the current value of the recursion limit.
import sys
print()
print("current value of the recursion limit:")
print(sys.getrecursionlimit())
print()

#Write a Python program to concatenate N strings.
list_of_colors = ['Red', 'White', 'Black']  
colors = '-'.join(list_of_colors)
print()
print("All Colors: "+colors)
print()

#Write a Python program to calculate the sum over a container.
s = sum([10,20,30,40,50])
print("\n sum of continer",s)
print()

#Write a Python program to test whether all numbers of a list is greater than a certain number.
num = [3,4,5,6]
print()
print(all(x>1 for x in num))
print(all(x>5 for x in num))
print()













