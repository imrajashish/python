#Write a Python program to prove that two string variables of same value point same memory location.
s = "Ashish"
r = "Ashish"
print("\nMemory location of s = ",hex(id(s)))
print("\nMemory location of r = ",hex(id(r)))

#Write a Python program to create a bytearray from a list. 
print()
nums = [10, 20, 56, 35, 17,6, 99]
# Create bytearray from list of integers.
values = bytearray(nums)
for x in values: print(x)
print()

#Write a Python program to display a floating number in specified numbers.
order_amt = 212.374
print('\nThe total order amount comes to %f' % order_amt)
print('The total order amount comes to %.2f' % order_amt)
print()

#Write a Python program to format a specified string to limit the number of characters to 6.
lst = "ASHISHRAJ"
print(lst[0:5])

#Write a Python program to determine whether variable is defined or not.
try:
    x = 1
except:
    print("Variable is not defined....!")
else:
    print("variable is defined.")
try:
    y
except:
    print("variable is not defined...!")
else:
    print("variable is defined!")

#Write a Python program to empty a variable without destroying it.
n = 20
d = {"x":200}
l = [1,3,5]
t= (5,7,8)
print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)()) 
